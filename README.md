# Laptop Price Predictor - Random Forest Regressor

## Results:

Random Forest Regressor -
Parameters: {'model**bootstrap': True, 'model**max_depth': 10, 'model**max_features': 'auto', 'model**min_samples_leaf': 1, 'model**min_samples_split': 2, 'model**n_estimators': 100}

Performance
5 fold GridSearch Cross Validation -

- Mean R2: 0.7754
- STD of R2: 0.0359

Training set (validaiton set) -

- R^2: 0.7924
- ADJ R^2: 0.7826

Testing set (unseen dataset) -

- R^2: 0.7849
- ADJ R^2: 0.7748

## Web Application

<img width="1440" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/dd2a863f-4f86-4a05-ae72-7a19b6a2b720">

## Business implications

This project understands how the price of a laptop (Price) is affected by certain components such as RAM, Brand, Ghz, Resolution, etc. The main goal is to provide a usable web application for students, workers, gamers, and many more to find a proper budget for a laptop based on specific features/specs. The web application will provide an information card for nontech savvy people for each spec to provide a benchmark and specific knowledge.

Predictor Variable: Price ($)

Feature Variables used in the model:

- Ghz (ghz)
- Ram (GB)
- SSD (GB|TB)
- Graphics Quality (low, fair, high, very high)
- Resolution (LengthxWidth)
- Brand (Brand of Laptop)
- CPU (Brand of CPU)

## Table of Contents

1. [Obtaining Data](#obtaining-data)
2. [Data Cleaning](#data-cleaning)
3. [Data Exploration](#data-exploration)
4. [Data Transformation](#data-transformation)
5. [Model Selection & Tuning](#model-selection--tuning)
6. [Creating the Framework of the Web Application](#creating-the-framework-of-the-web-application)
7. [Creating React.js with Deployed Model](#creating-reactjs-with-deployed-model)

## 1. Obtaining Data

Data web scrapped off of newegg.com website using Beautiful Soup + basics of HTML.

Created a function where you input a link from Newegg that shows a listing of laptops from a thumbnail view.
Input: Website link
Output Two Dataframes

- First Dataframe: Will scrape the link, description, and brand of the computer
- Second Dataframe: Will run a for loop iterating through each link of First Dataframe to get more specific specs - Ghz, Ram, SSD, Graphics, panel, type, os, Cpu,
  Features

Problem: My web scraping technique created a lot of duplicates (2683 records) for my dataset. In the future, I will try to create a web scraper that doesn't take in duplicates.

## 2. Data Cleaning

Merged the First and Second Data Frame

Duplicates - There were a total of 2683 records to be dropped

Dealing with Null Values -

- Dropping Null values because I personally feel that I would fit my data on noise that's not generalizable. I am risking the purpose of putting synthetic information on certain laptops with null values in two or more features.
- When creating the holdout set, make sure not to use any input null values

## 3. Data Exploration & Data Preprocessing

Dataset shape: (924, 12)

Price

<img width="497" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/b2868ca5-e2f2-45e4-916c-26b3caa2c4da">

Visualizations:
Normally distributed with a slight right skew. I don't need to see the need to drop outliers because it is not an unnatural occurrence. Laptops with these high prices may be indicative of high specs. They exist but may not be in high production. These outliers may affect linear models with strong assumptions, such as Linear regression, because outliers can skew their best-fit line. It may need some regularization. Robust models such as Decision Trees, Random Forest, and XGBoost may generalize better.

Ghz
Preprocessing: Many records were in a format of EG: 10750H (2.60GHz).

- Goal was to extract what's in the parentheses
- Used a regular expression to extract values inside parentheses
- Used another function to extract float values (removing "Ghz")

<img width="468" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/06442ba3-ed1f-45f7-8122-24426f9b9662">

Visualizations:
Scatterplot with Regplot. The dataset shows a wide homoscedastic, slightly linear trend. Could be of use for prediction

Operating System

<img width="741" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/4f4a9b09-3210-4e03-8cf0-084eae6dbcca">

Windows 11 has a higher count and has a few records that are outliers. Overall, the prices for both operating systems are similar. It doesn't look like there would be any indications/correlations for regression.

SSD

Preprocessing: Removed GB|TB for SSD and Ram and converted TB to GB

- EG: converted 2TB -> 2000 GB
- Reason is that putting the features in one unit that's relative will create a better-fit line or help the model understand the nature of the records.

  <img width="744" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/86925826-cb6e-46d5-bf11-c92730b46bad">

The SSD of the laptop reveals to have a linear relationship. The shape of the scatterplot looks like this because there is low cardinality with numerical variables because SSD represents 8-bit.

Brand
Preprocessing: Dropped Brand names that didn't have a high count value

<img width="496" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/748e69d5-885a-4d77-bba9-25fa9bfd4cdd">

Razer - A laptop brand that is known for gaming. This could possess an indication that gaming brands may have a higher cost. All the other brands have similar means.

Cpu

<img width="491" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/7cf4130c-ed7c-4a32-9dc6-916952e4abdb">

The averages of Cpu types seem to have an ordinal pattern of quality based on a newer CPU generation. Overall, it seems that Intel > Ryzen in terms of costs based on data.

Ram

<img width="732" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/a34b7543-b895-48b4-9c6e-947d3cfe6d33">

Shows a steeper slope compared to the other numerical values. This could be quite indicative of a price. Has similar cardinality behavior with SSD.

Resolution

<img width="378" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/c3ab28df-b962-4a8e-abca-c971cb68780b">

Resolutions have a wide spread of data as it increases, but it shows a linear pattern.

Graphics

<img width="486" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/49d4a956-4817-4a71-8cf7-8c01f33dcd6a">

Cardinality Issue solved via Feature Engineering.

- Graphics Card - There are too many unique values for this specific feature
  - Reduced to 4 unique categorical variables based on the quality of the graphics card (Domain Knowledge and speculation). Low-Medium-High-Very High

Type

Had a Cardinality Issue where some of the records had a mixture of types

- Eg: one record was like Workstation/Gaming/Personal/School
- Tried to reduce as much as possible, which could've caused the lack of variability with feature

<img width="510" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/e48e5fbf-e15e-4f58-aae4-6164727e86f1">

## 4. Data Transformation

Explain any feature engineering or data transformation techniques applied to prepare the data for modeling.

Ordinal Encoding

- Resolution sorted from smallest to largest size (LengthxWidth)
- Graphics Quality from Low-Very high

Nominal -> Ordinal variable

- I Sorted the Brand and CPU via mean from least to greatest and used that order as ordinal encoding

Pearson Correlations

<img width="690" alt="image" src="https://github.com/Dionisio1013/ML_Laptop_Price_Prediction/assets/106797659/09b43932-2a0b-4716-a0c6-e39d837cca70">

- Features show positive correlations with Price
- Dropped Operating System and Type for having low correlations
- Kept Brand to add a feature for the web application

## 5. Model Preprocessing

Created Train, Validation, and Testing Set
70-15-15

For Training and Validation set

- Train-test-split
- Made sure to use a standard scaler to standardize the data putting into z-scores.
- Used fit_transform on the training set and then used transform for the testing set to be scaled based on the training set.

## 6. Model Selection & Tuning

Performed 5-fold grid search cross-validation and cross-validation
Best Parameters:

{'model**bootstrap': True, 'model**max_depth': 10, 'model**max_features': 'auto', 'model**min_samples_leaf': 1, 'model**min_samples_split': 2, 'model**n_estimators': 200}
The mean R2 is 0.7754795297176816 with a std of 0.03592573188792202

- R2 improved, and the std went down as well

Final model performance:

RandomForest Regressor with parameters
Testing set (unseen dataset) -

- R^2: 0.7884
- ADJ R^2: 0.7784

## 7. Creating the Framework of the Web Application

Created Pipeline to creating Web Application

1. Data Ingestion
2. Data Transformation
3. On my src tab, I created the Pipeline of inserting a CSV, Fitting model +, and then obtaining a pickle file.
   With the pickle file, I was able to

Outline the steps taken to create the web application's framework, backend setup, and necessary dependencies.

## 8. Creating React.js with Deployed Model

Explain how the model is integrated into the React.js front and how the deployed model is used to make predictions in the web application.

Note: This is a suggested format based on the information provided in the initial readme. Please fill in the actual content and details specific to your project as needed.
