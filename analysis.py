
import pandas as pd
import os

# Project dataset path
file_path = "dataset/student-mat.csv"

# Load the dataset
df = pd.read_csv(file_path, sep=";")

# Display basic information
print("\n===== STUDENT PERFORMANCE DATASET =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

# Create folder for saving graphs
os.makedirs("visualizations", exist_ok=True)

# 1. Final Grade Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["G3"], bins=10, kde=True)
plt.title("Distribution of Final Student Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.savefig("visualizations/grade_distribution.png")
plt.show()

# 2. Gender-wise Student Count
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="sex")
plt.title("Student Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.savefig("visualizations/gender_distribution.png")
plt.show()

# 3. Study Time vs Final Grade
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="studytime", y="G3")
plt.title("Study Time vs Final Grade")
plt.xlabel("Weekly Study Time")
plt.ylabel("Final Grade")
plt.savefig("visualizations/studytime_vs_grade.png")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig("visualizations/correlation_heatmap.png")
plt.show()

print("\nEDA completed successfully!")
print("Graphs saved in visualizations folder.")
print("\nEDA completed successfully!")

print("\nGenerated Graphs:")
print(os.listdir("visualizations"))

# ==========================================
# EDA FINDINGS AND ANALYSIS
# ==========================================

print("\n========== EDA FINDINGS ==========")

# 1. Average grades
print("\nAverage Grades:")
print(df[["G1", "G2", "G3"]].mean())

# 2. Gender-wise performance
print("\nGender-wise Average Final Grade:")
print(df.groupby("sex")["G3"].mean())

# 3. Study time and performance
print("\nStudy Time vs Average Final Grade:")
print(df.groupby("studytime")["G3"].mean())

# 4. Previous grades correlation with final grade
print("\nCorrelation with Final Grade (G3):")
print(df.corr(numeric_only=True)["G3"].sort_values(ascending=False))

# 5. Failure count and performance
print("\nPrevious Failures vs Final Grade:")
print(df.groupby("failures")["G3"].mean())

# 6. Attendance analysis
print("\nAverage Absences:")
print(df["absences"].mean())

print("\nStudents with Zero Final Grade:")
print((df["G3"] == 0).sum())

print("\n========== ANALYSIS COMPLETED ==========")

# ==========================================
# ADDITIONAL RESEARCH ANALYSIS
# ==========================================

print("\n===== RESEARCH QUESTION ANALYSIS =====")

# Study time vs grades
print("\nStudy Time Analysis:")
print(df.groupby("studytime")["G3"].agg(["count", "mean"]))

# Absences vs final grade correlation
print("\nAbsences and Final Grade Correlation:")
print(df["absences"].corr(df["G3"]))

# Gender-wise performance
print("\nGender-wise Performance:")
print(df.groupby("sex")["G3"].agg(["count", "mean"]))

# Previous grades correlation
print("\nG1, G2 and G3 Correlation:")
print(df[["G1", "G2", "G3"]].corr())

print("\nResearch analysis completed!")

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, ttest_ind

# ==========================================
# 1. PROJECT FOLDER SETUP
# ==========================================

os.makedirs("visualizations", exist_ok=True)
os.makedirs("reports", exist_ok=True)

file_path = "dataset/student-mat.csv"

# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(file_path, sep=";")

print("\n===== STUDENT PERFORMANCE DATASET =====")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

print("\n========== EDA FINDINGS ==========")

# Average grades
print("\nAverage Grades:")
print(df[["G1", "G2", "G3"]].mean())

# Gender-wise average final grade
print("\nGender-wise Average Final Grade:")
print(df.groupby("sex")["G3"].mean())

# Study time vs average final grade
print("\nStudy Time vs Average Final Grade:")
print(df.groupby("studytime")["G3"].mean())

# Correlation with final grade
print("\nCorrelation with Final Grade (G3):")
print(
    df.select_dtypes(include="number")
      .corr()["G3"]
      .sort_values(ascending=False)
)

# Previous failures vs final grade
print("\nPrevious Failures vs Final Grade:")
print(df.groupby("failures")["G3"].mean())

# Average absences
print("\nAverage Absences:")
print(df["absences"].mean())

# Students with zero final grade
print("\nStudents with Zero Final Grade:")
print((df["G3"] == 0).sum())

# ==========================================
# 4. DATA VISUALIZATION
# ==========================================

sns.set_theme(style="whitegrid")

# Graph 1: Final Grade Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="G3", bins=10, kde=True)
plt.title("Distribution of Final Student Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/grade_distribution.png")
plt.close()

# Graph 2: Gender Distribution
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="sex")
plt.title("Student Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/gender_distribution.png")
plt.close()

# Graph 3: Study Time vs Final Grade
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="studytime", y="G3")
plt.title("Study Time vs Final Grade")
plt.xlabel("Weekly Study Time Category")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("visualizations/studytime_vs_grade.png")
plt.close()

# Graph 4: Correlation Heatmap
plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig("visualizations/correlation_heatmap.png")
plt.close()

print("\nEDA completed successfully!")
print("Graphs saved in visualizations folder.")

# ==========================================
# 5. RESEARCH QUESTION ANALYSIS
# ==========================================

print("\n===== RESEARCH QUESTION ANALYSIS =====")

# Study time analysis
print("\nStudy Time Analysis:")
print(df.groupby("studytime")["G3"].agg(["count", "mean"]))

# Absences and final grade correlation
print("\nAbsences and Final Grade Correlation:")
print(df["absences"].corr(df["G3"]))

# Gender-wise performance
print("\nGender-wise Performance:")
print(df.groupby("sex")["G3"].agg(["count", "mean"]))

# G1, G2 and G3 correlation
print("\nG1, G2 and G3 Correlation:")
print(df[["G1", "G2", "G3"]].corr())

# ==========================================
# 6. STATISTICAL TESTING
# ==========================================

print("\n===== STATISTICAL TESTING =====")

# Test 1: Gender-wise grade comparison
female_grades = df[df["sex"] == "F"]["G3"]
male_grades = df[df["sex"] == "M"]["G3"]

t_stat, p_value = ttest_ind(
    female_grades,
    male_grades,
    equal_var=False
)

print("\nGender-wise T-Test:")
print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

if p_value < 0.05:
    print("Result: Statistically significant difference found.")
else:
    print("Result: No statistically significant difference found.")

# Test 2: Study time and final grade correlation
study_corr, study_p = pearsonr(
    df["studytime"],
    df["G3"]
)

print("\nStudy Time Correlation:")
print("Correlation:", round(study_corr, 4))
print("P-value:", round(study_p, 6))

# Test 3: Absences and final grade correlation
absence_corr, absence_p = pearsonr(
    df["absences"],
    df["G3"]
)

print("\nAbsences Correlation:")
print("Correlation:", round(absence_corr, 4))
print("P-value:", round(absence_p, 6))

# ==========================================
# 7. SAVE REPORTS
# ==========================================

# Save descriptive statistics
summary = df.describe().round(2)
summary.to_csv("reports/summary_statistics.csv")

# Save correlation matrix
correlation_matrix = numeric_df.corr().round(3)
correlation_matrix.to_csv("reports/correlation_matrix.csv")

# Save key findings
findings = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Total Columns",
        "Missing Values",
        "Average Final Grade",
        "Average Absences",
        "Students with Zero Final Grade",
        "G1 and G3 Correlation",
        "G2 and G3 Correlation",
        "Study Time and G3 Correlation",
        "Absences and G3 Correlation",
        "Gender T-Test P-value"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        round(df["G3"].mean(), 3),
        round(df["absences"].mean(), 3),
        int((df["G3"] == 0).sum()),
        round(df["G1"].corr(df["G3"]), 3),
        round(df["G2"].corr(df["G3"]), 3),
        round(study_corr, 3),
        round(absence_corr, 3),
        round(p_value, 6)
    ]
})

findings.to_csv("reports/key_findings.csv", index=False)

# ==========================================
# 8. FINAL STATUS
# ==========================================

print("\n===== PROJECT OUTPUTS =====")

print("\nVisualizations:")
print(os.listdir("visualizations"))

print("\nReports:")
print(os.listdir("reports"))

print("\n========== ANALYSIS COMPLETED SUCCESSFULLY ==========")
