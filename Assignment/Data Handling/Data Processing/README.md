# Virat Kohli International Career Analysis

## Project Overview

This project performs a complete Exploratory Data Analysis (EDA) of Virat Kohli’s international cricket career across:

- ODI
- T20I
- Test

The analysis explores performance trends, consistency, strike rate evolution, dismissal patterns, and captaincy impact using Python.

---

## Dataset Used

The following datasets are used:

- virat_kohli_odi_innings_data.csv  
- virat_kohli_t20i_innings_data.csv  
- virat_kohli_test_innings_data.csv  
- Virat_Kohli_100s-Virat_Kohli_100s.csv  
- kohli_data.csv  

All datasets are placed inside the `data/` folder.

---

## Technologies & Libraries

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Plotly  
- Jupyter Notebook (VS Code)  

---

## Analysis Performed

### Full Career Analysis

- Total Runs (All Formats)
- Format-wise Comparison
- Highest Individual Scores
- Year-wise Run Trend

### Advanced Insights

- Rolling Average Trend
- Strike Rate Trend Over Years
- Consistency Metric (Standard Deviation per Format)
- Dismissal Type Analysis
- Performance Before vs After Captaincy

---

## Visualization Features

- Professional dark theme styling
- Bar charts
- Line charts
- Trend comparisons
- Statistical analysis visuals

---

## Key Insights

- ODI format shows highest consistency and peak performance.
- Strike rate improved over career phases.
- Captaincy period reflects increased responsibility and strong output.
- Rolling average confirms long-term stability.

---

## Project Structure

Data_Processing/
│
├── data/
│   ├── virat_kohli_odi_innings_data.csv
│   ├── virat_kohli_t20i_innings_data.csv
│   ├── virat_kohli_test_innings_data.csv
│   ├── Virat_Kohli_100s-Virat_Kohli_100s.csv
│   └── kohli_data.csv
│
├── main.ipynb
└── README.md

---

## How to Run the Project

### Step 1: Create Virtual Environment

python -m venv venv

### Step 2: Activate Environment (Windows)

venv\Scripts\activate

### Step 3: Install Required Libraries

pip install pandas numpy matplotlib plotly notebook nbconvert

### Step 4: Open Notebook

Open main.ipynb in VS Code and select the venv kernel.

---

## Learning Outcome

This project demonstrates:

- Real-world sports analytics
- Data preprocessing
- Advanced EDA techniques
- Statistical insight generation
- Professional data visualization