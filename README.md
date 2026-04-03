# 💰 Finance Management CLI

A command-line based Finance and Budget Management system built using Python.
This project allows users to track expenses, analyze spending patterns, and compare against budget limits with structured data insights.

---

## 🚀 Features

* Add expenses by category
* View category-wise and total expenses
* Budget planning with minimum and maximum limits
* Percentage usage of budget
* Warning system when nearing budget limit (≥80%)
* 📊 Tabular data view using Pandas

---

## 🛠️ Tech Stack

* Python
* JSON (data storage)
* Pandas (data analysis & table view)

---

## 📂 Project Structure

* `main.py` → main application
* `Categories.json` → stores expense data
* `budget_planning.json` → stores budget limits

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/vinayak-5576/Finance-Management-CLI.git
```

2. Navigate into the folder:

```
cd Finance-Management-CLI
```

3. Install dependencies:

```
pip install pandas
```

4. Run the program:

```
python main.py
```

---

## 📊 Data Table Feature

The project now includes a tabular view of financial data:

| Category | Minimum | Maximum | Actual | Usage (%) | Difference |
| -------- | ------- | ------- | ------ | --------- | ---------- |
| Travel   | 100     | 500     | 300    | 60%       | 200        |

This helps in better understanding and analyzing expenses.

---

## 🔮 Future Improvements

* Graphs using matplotlib
* Dashboard interface (Streamlit)
* Web UI using HTML/CSS
* Monthly expense tracking

---

## 🙌 Author

Vinayak
