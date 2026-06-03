# Modern IBNR Reserving Tool

An actuarial tool that simulates modern insurance loss triangles from 2017-2016 and calculates **Incurred But Not Reported (IBNR)** reserves using the volume-averaged **Chainladder method**. 

---

## 📊 Sample Output

When executed, the tool analyzes the development patterns:

* **Accident Years:** 2017 – 2026
* **Reserving Dynamic:** Older accident years exhibit mature trends requiring minimal IBNR, whereas the most recent accident years show higher IBNR.
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/cfcbf120-9cd5-471e-a735-3e45c4ccb138" />

---

## 🚀 Features

- Bypasses old database and evaluates up to the current year.
- Used Chainladder method to establish developments.
- Negative IBNR occurrences in mature years are clipped to zero.

---

## 🛠️ Installation & Prerequisites
Ensure you have a recent Python environment, and install packages using pip:
```pip install chainladder pandas matplotlib```
