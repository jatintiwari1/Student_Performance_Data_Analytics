
# Student Performance Data Analytics

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Student Performance dataset to understand the factors associated with students' academic performance.

The analysis focuses on study time, previous academic failures, absences, gender, and previous examination grades to identify patterns and relationships with final grades.

## Dataset Information
- Dataset: Student Performance (Mathematics)
- Source: UCI Machine Learning Repository
- Total Records: 395 students
- Total Features: 33 columns
- Target Variable: G3 (Final Grade)
- Missing Values: 0

## Project Objectives
1. Explore student academic performance using Python.
2. Analyze the relationship between study time and final grades.
3. Examine how previous academic failures relate to performance.
4. Study the relationship between absences and final grades.
5. Compare G1, G2, and G3 academic grades.
6. Perform statistical tests and generate visual reports.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Visual Studio Code

## Project Structure

```text
Student_Performance_Data_Analytics/
│
├── dataset/
│   └── student-mat.csv
│
├── visualizations/
│   ├── grade_distribution.png
│   ├── gender_distribution.png
│   ├── studytime_vs_grade.png
│   └── correlation_heatmap.png
│
├── reports/
│   ├── summary_statistics.csv
│   ├── correlation_matrix.csv
│   └── key_findings.csv
│
├── analysis.py
├── README.md
└── requirements.txt
```

## Key Findings

- The average final grade (G3) is approximately 10.42 out of 20.
- The dataset contains 395 student records and 33 columns.
- No missing values were found.
- G2 has a strong positive correlation with G3 (approximately 0.905).
- G1 has a strong positive correlation with G3 (approximately 0.801).
- Previous academic failures show a negative correlation with final grades (approximately -0.360).
- Study time has a weak positive correlation with final grades (approximately 0.098).
- Absences have almost no linear correlation with final grades (approximately 0.034).

## Statistical Analysis

The project uses:
- Pearson correlation analysis
- Independent two-sample Welch's t-test for gender-wise grade comparison
- Descriptive statistics
- Group-wise performance analysis

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Student_Performance_Data_Analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python script

```bash
python analysis.py
```

The script generates visualizations and CSV reports automatically.

## Limitations

- The analysis is based on one dataset containing 395 students.
- Correlation does not establish causation.
- Some variables are categorical or ordinal.
- The results may not represent all schools or student populations.

## Future Improvements

- Build an interactive Power BI dashboard.
- Apply machine learning models to predict final grades.
- Explore additional student performance datasets.
- Perform more detailed statistical analysis.
- Improve visual reporting and insights.

## Conclusion

This project demonstrates how Python-based exploratory data analysis and statistical methods can be used to investigate student academic performance. Previous examination grades show particularly strong associations with final grades, while other factors show weaker or varying relationships.

## Dataset Reference

Cortez, P. and Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance.

UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/320/student+performance
