# 🛒 Flipkart Product Price Analysis & Prediction

## 📌 Project Overview

This project focuses on analyzing Flipkart product data to uncover pricing trends, discount strategies, brand performance, and category-wise product distribution. The project follows a complete Data Science workflow, including data preprocessing, exploratory data analysis (EDA), visualization, feature engineering, and machine learning model development.

---

## 📂 Dataset

📍 **Source:** Kaggle

📊 **Dataset Size:** ~20,000 Products

### Features Included:
- Product Name
-  Product Category
-  Retail Price
-  Discounted Price
-  Brand
-  FK Advantage Status
-  Product Description
-  Product Specifications

---

## Data Preprocessing

The following preprocessing steps were performed:

Removed duplicate records

Handled missing values using:
- Mean
- Median
- Mode

Removed unnecessary columns

Treated outliers in pricing features

Created new feature:
- Discount Percentage

Extracted:
- Main Product Category

Encoded categorical variables for machine learning

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

-  Price Distribution Analysis
-  Discount Distribution Analysis
-  Brand-wise Product Analysis
-  Category-wise Product Analysis
-  Retail Price vs Discounted Price Relationship
-  FK Advantage Product Comparison
-  Correlation Analysis

---

## 📊 Data Visualizations

Various visualizations were created to identify patterns and insights:

- Histograms
- Scatter Plots
- Box Plots
- Bar Charts
- Correlation Heatmaps

These visualizations helped reveal customer-facing pricing trends and promotional strategies.

---

## Machine Learning Models

### Linear Regression

Used as a baseline model for predicting product prices.

### Random Forest Regression

Implemented to capture complex and non-linear relationships among product attributes.

---

## 📏 Model Evaluation

Models were evaluated and compared using performance metrics such as:

- 🎯 R² Score
- 📊 Prediction Accuracy

###  Best Performing Model

**Random Forest Regression**

The Random Forest model outperformed Linear Regression and provided more accurate predictions.

---

## 💡 Key Insights

🔹 Most products belong to the low-to-mid price range.

🔹 Discounts are a major pricing strategy across multiple categories.

🔹 Product categories show significant variation in average pricing.

🔹 Retail Price strongly influences Discounted Price.

🔹 Brands follow different discounting and pricing strategies.

🔹 Random Forest effectively captures pricing behavior in e-commerce datasets.

---

##  Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 🎨 Seaborn
- 🤖 Scikit-Learn
- 📓 Jupyter Notebook

---

## 🎯 Conclusion

This project demonstrates a complete Data Science pipeline, starting from data cleaning and preprocessing to visualization, feature engineering, machine learning, and model evaluation.

The analysis provides valuable insights into Flipkart's pricing and discount strategies while showcasing the practical application of machine learning for product price prediction in an e-commerce environment.

🚀 A hands-on project highlighting data analysis, visualization, and predictive modeling skills.
