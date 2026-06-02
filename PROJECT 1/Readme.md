# Flipkart Product Price Analysis and Prediction

## Project Overview

This project analyzes Flipkart product data to understand pricing patterns, discount strategies, brand distribution, and category-wise product trends. The project follows the complete Data Science workflow, including data preprocessing, exploratory data analysis (EDA), visualization, feature engineering, and machine learning model development.

## Dataset

- Source: Kaggle
- Records: ~20,000 products
- Features include:
  - Product Name
  - Product Category
  - Retail Price
  - Discounted Price
  - Brand
  - FK Advantage Status
  - Product Description
  - Product Specifications

## Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate records
- Handled missing values using mean, median, and mode where appropriate
- Removed unnecessary columns
- Treated outliers in price-related features
- Created derived features such as Discount Percentage
- Extracted Main Category from category hierarchy
- Encoded categorical variables for machine learning

## Exploratory Data Analysis

Key analyses performed:

- Price distribution analysis
- Discount percentage distribution
- Brand-wise product analysis
- Category-wise product analysis
- Retail Price vs Discounted Price relationship
- FK Advantage product comparison
- Correlation analysis

## Visualizations

The project includes:

- Histograms
- Scatter Plots
- Box Plots
- Bar Charts
- Correlation Heatmaps

These visualizations helped identify pricing trends, discount patterns, and category-level insights.

## Machine Learning Models

### Linear Regression
Used as a baseline model for price prediction.

### Random Forest Regression
Implemented to capture complex non-linear relationships within the dataset.

## Model Evaluation

Performance of both models was compared using R² score and prediction accuracy.

### Result

Random Forest Regression outperformed Linear Regression and was selected as the final model due to its superior predictive performance.

## Key Insights

- Most products belong to the low-to-mid price segment.
- Significant discounts are common across multiple categories.
- Product pricing varies considerably across categories and brands.
- Retail price strongly influences discounted price.
- Random Forest effectively captures pricing patterns in e-commerce data.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Conclusion

This project demonstrates an end-to-end Data Science pipeline, from data cleaning and visualization to predictive modeling. The analysis provides valuable insights into Flipkart's product pricing and discount strategies while showcasing machine learning techniques for price prediction.
