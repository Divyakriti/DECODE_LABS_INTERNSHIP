# 🎓 Student Stress Analysis & Predictive Modeling

An end to end Data Science project developed during the Decodelabs Data Science Internship.  
This project focuses on analyzing student lifestyle, academic pressure, psychological health, and social conditions to identify stress patterns and build a predictive machine learning model capable of estimating student stress levels.

The project was designed to simulate a real-world analytics workflow by completing all 5 major phases of a professional data science pipeline — from raw data cleaning to predictive intelligence.

---

# 📌 Project Overview & Pipeline

This project combines statistical analysis, exploratory data visualization, and supervised machine learning to understand how different academic, psychological, and environmental factors influence stress among students.

The complete workflow is divided into 5 major engineering stages:

---

## ✅ Task 1 — Data Collection & Dataset Understanding

Performed detailed inspection and structural analysis of the student stress dataset containing multiple psychological, physiological, social, and academic indicators.

### Features Included:
- Anxiety Level
- Self Esteem
- Depression
- Sleep Quality
- Academic Performance
- Study Load
- Peer Pressure
- Social Support
- Bullying
- Future Career Concerns
- Living Conditions
- Safety
- Extracurricular Activities
- Blood Pressure
- Mental Health History

### Objective:
Understand how multiple real world student factors interact and contribute toward stress prediction.

---

# 🧼 Task 2 — Data Cleaning & Preprocessing

Real-world datasets are rarely clean. This phase focused on preparing the dataset for accurate machine learning analysis.

### Cleaning Operations Performed:
- Identified missing/null values
- Removed duplicate records
- Standardized column formatting
- Checked invalid numerical ranges
- Converted data into ML compatible format
- Prepared target labels for prediction

### Preprocessing Techniques:
- Feature Selection
- Label Encoding
- Data Normalization
- Train-Test Splitting

---

# 📊 Task 3 — Statistical Analysis & Pattern Discovery

Performed statistical computations to identify hidden trends and relationships within student behavior and stress patterns.

### Key Statistical Insights:
- Students with high academic load showed significantly higher stress levels
- Poor sleep quality strongly correlated with elevated anxiety
- Social support demonstrated inverse correlation with stress
- Bullying and peer pressure showed noticeable impact on emotional health

### Statistical Methods Used:
- Mean / Median Analysis
- Standard Deviation
- Correlation Analysis
- Outlier Detection
- Distribution Analysis

---

# 📈 Task 4 — Exploratory Data Visualization

Built visual analytics dashboards to uncover trends, distributions, and behavioral patterns using Seaborn and Matplotlib.

### Visualizations Created:
- Correlation Heatmaps
- Stress Distribution Charts
- Boxplots for Academic Pressure
- Sleep Quality vs Stress Analysis
- Anxiety & Depression Comparison Graphs
- Feature Correlation Matrix

### Major Findings:
- Anxiety Level emerged as one of the strongest stress indicators
- Academic Pressure and Sleep Quality formed clear stress clusters
- Students with better social support consistently showed lower stress patterns

---

# 🤖 Task 5 — Predictive Modeling & Machine Learning

Built a supervised machine learning classification model capable of predicting student stress levels using behavioral and psychological indicators.

### Machine Learning Algorithms Tested:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Final Model Performance:
| Algorithm | Accuracy |
|---|---|
| Logistic Regression | ~90% |
| Random Forest | ~89% |
| Decision Tree | ~91% |

### Selected Model:
Logistic Regression was selected as the final model due to its strong generalization capability, interpretability, and stable performance on unseen data.

Although Decision Tree achieved slightly higher accuracy, Logistic Regression provided more reliable and explainable predictions without overfitting, making it more suitable for real-world student stress analysis.
---

# 💡 Key Project Insights

### Major Stress Drivers Identified:
- Anxiety Level
- Depression
- Study Load
- Poor Sleep Quality
- Future Career Concerns
- Peer Pressure

### Important Observation:
Stress is influenced not only by academics, but also by emotional health, environment, and social conditions.

---

# 💻 Tech Stack & Libraries

### Language:
- Python 3

### Development Environment:
- VS Code
- Jupyter Notebook

### Libraries Used:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

