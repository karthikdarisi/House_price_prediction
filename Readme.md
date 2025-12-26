House Price Prediction
Project Overview
This project delves into the machine learning workflow by predicting housing prices based on a fabricated dataset. I created this to comprehend how the different featuressuch as size, age, and locationaffect the market value of a house by means of Linear Regression.
Project Structure
The local repository is set up to be in line with the industry standards for data science projects:
data/: The raw CSV dataset (1, 000 entries) is included here.
notebooks/: Jupyter notebooks for Exploratory Data Analysis (EDA) and model prototyping.
src/: Python scripts for data preprocessing, model training, and evaluation.
requirements.txt: The file lists all the Python libraries needed to execute the project.
Dataset Features
The model considers the following characteristics:
Area (sqft): Total square footage of the house.
Bathrooms/Bedrooms: Number of rooms.
Distance from City (km): Proximity to the city center.
Age of the House: Years since construction.
Key Insights & Model Results
The model employed Linear Regression to figure out the price influencers most:
* Top Positive Driver: Bathrooms had the highest positive coefficient ($+325, 659$), indicating that they are the main medium of luxury demonstration in this dataset.
* The "Location" Penalty: The price goes down by around $\7, 022$ for every kilometer away from the city.
* Depreciation:Each year, the value of the house decreases by approximately $25,186.
