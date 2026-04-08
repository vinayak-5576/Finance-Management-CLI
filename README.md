# 💰 Finance Management CLI

A command-line based Finance and Budget Management system built using Python.
This project allows users to track expenses, analyze spending patterns, and compare against budget limits with structured data insights.

---

## 🚀 Features

* 📌 Add expenses category-wise for each month
* 📊 View total and category-wise expenses
* 💸 Budget planning with **min/max limits**
* ⚠️ Smart insights:
  * Over budget alerts
  * Remaining budget tracking
  * Usage percentage calculation
* 🧾 Tabular data visualization using **Pandas**
* 📅 Monthly expense tracking (January → December)
* 📊 Data visualization using Matplotlib:
  * Line Graph (trend over months)
  * Bar Graph (comparison between months)
* 🔄 Multi-month comparison support
* 🧠 Intelligent handling of missing data


---

## 🛠️ Tech Stack

* Python
* JSON (data storage)
* Pandas (data analysis & table view)
* Matplotlib (for graphs)

---
## 🧠 How It Works
* NOTE
  It already has some data sets of All months so you can eitehr delete the entries or just create a new new json file with similar sort of info.

* Data is stored in:

  * `Categories.json` → stores expenses
  * `budget_planning.json` → stores budget limits

* User selects:

  1. Action (Add / View / Budget / Table / Graph)
  2. Month
  3. Category
  
* System:
  1. Stores in Json
  2. Calculate totals
  3. Compares with Your budget plan for that Month
  4. Display Insights



## 🗂️ Project Structure

```
Finance-Management/
│
├── main.py                  # Main program
├── Categories.json         # Expense data
├── budget_planning.json    # Budget limits
└── README.md               # Project documentation
```

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
python -m pip install matplotlib

```

4. Run the program:

```
python main.py
```

---
## 📊 Current Capabilities

* Monthly expense tracking
* Category-based analysis
* Budget comparison (Actual vs Max)
* Usage percentage calculation
* Table view using Pandas
 📊 Data Table Feature

The project now includes a tabular view of financial data:

| Category | Minimum | Maximum | Actual | Usage (%) | Difference |
| -------- | ------- | ------- | ------ | --------- | ---------- |
| Travel   | 100     | 500     | 300    | 60%       | 200        |
| ......   | ...     | ...     | ...    | ...       | ...        |

This helps in better understanding and analyzing expenses.
* Graphs:
  1. Compare spending across months
  2. Category-wise visualization

---

## 🔮 Future Improvements

* 📊 Interactive dashboards
* 🌐 Web UI using HTML, CSS, Streamlit
* 📅 Monthly comparison trends
* 🔔 Smart spending recommendations
* Moblie friendly UI

---

* Motivation

 This project was built to strengthen problem-solving skills, understand real-world data handling, and implement core Python concepts in a practical scenario.

## 🙌 Author

Built by **Vinayak**
First step into building real-world Python projects 🚀

---

## ⭐ Note

This is a beginner-to-intermediate level project focused on:

* Learning data structures
* Building real logic
* Improving problem-solving

More features and improvements coming soon!

