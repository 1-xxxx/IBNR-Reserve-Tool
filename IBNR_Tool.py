import pandas as pd
import chainladder as cl
import matplotlib.pyplot as plt

data = []
for origin in range(2017, 2027):
    for dev in range(origin, 2027):
        lag = dev - origin + 1
        loss = 100000 + (origin - 2017) * 5000  
        factor = 1.0 - (0.5 / lag)               
        data.append({
            'origin_year': origin,
            'dev_year': dev,
            'losses': loss * factor
        })

df = pd.DataFrame(data)

modern_triangle = cl.Triangle(
    df, 
    origin='origin_year', 
    development='dev_year', 
    columns='losses', 
    cumulative=True
)

dev_pattern = cl.Development(average='volume').fit(modern_triangle)
cl_model = cl.Chainladder().fit(modern_triangle, dev_pattern)

incurred_ibnr = cl_model.ibnr_.to_frame()
ibnr_floored = incurred_ibnr.clip(lower=0)
ibnr_floored.index = ibnr_floored.index.astype(str).str[:4]

fig, ax = plt.subplots(figsize=(10, 6))
ibnr_floored.plot(kind='bar', ax=ax, color='tab:blue', legend=False, 
                  title='Required Incurred IBNR Reserves')

ax.set_xlabel("Accident Year")
ax.set_ylabel("Reserve Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
