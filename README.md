# Data Jobs Prediction
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.7](https://img.shields.io/badge/Python-3.7-blueviolet.svg) ![Seaborn](https://img.shields.io/badge/Library-Seaborn-success.svg) ![Scikit-learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)

## Web app

The **fully deployed** model built with **Flask** is available here on **Heroku** : https://data-jobs-prediction.herokuapp.com/

## Overview

In the field of Big Data, Internet is full of job advertisements by companies looking for different profiles at each level (**Junior**, **Middle**, **Senior**, **Tech lead**...) and different skills to take up a new position (**Data Analyst**, **Data Engineer**, **Data Scientist**, etc)

Based on **thousands** of job advertisements collected from employment websites, this Web App allow us to predict the **salary** of Data Science roles based on a few variables like **industry**, **location**, **company revenue**, **experience**, etc.

Under the hood, the app has been optimized with a machine learning algorithm called **Gradient Boosted Tree (Regressor)**, which performed the best after comparison with other regression techniques from **Linear Models**, **Decision Trees** or **Ensemble methods** like **Random Forest**.

Through this project, **4 datasets** have been combined for a total of **12 782 records**. The final dataset includes the following fields:

| **Field** | **Description** |
|-------|-------------|
|**Job Title**|*Position / Role that the hiring company is offering*|
|**Salary Estimate**|*Annual Salary or Salary per hour for the job*|
|**Job Description**|*Description of the missions, experience and skills required to get the job*|
|**Rating**|*Company rating out of 5, indicating the popularity*|
|**Company Name**|*Company Name*|
|**Location**|*Location of the hiring company*|
|**Headquarters**|*Location of the Headquarters*|
|**Size**|*Number of employees working in the company*|
|**Founded**|*Date of establishment*|
|**Type of ownership**|*Type of the business ownership*|
|**Industry**|*Describes a specific business producing a particular kind of goods or services*|
|**Sector**|*Describes a large segment of the economy*|
|**Revenue**|*Annual revenue of the company*|
|**Competitors**|*List of competitors / rivals of the company*|
|**Easy Apply**|*Yes / No*|

Working on this dataset, **data preprocessing** & **feature engineering** have been major steps before going to the **model selection** and **hyperparameter tuning**. Indeed, it was important to clean the dataset and to handle all the missing values, with the help of **statistical** and **machine learning imputation** methods. Then, regression algorithms have been selected using **K-fold Cross Validation** and the **MSE** metric to predict the salary.