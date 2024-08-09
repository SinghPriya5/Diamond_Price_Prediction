<h1 style='color:blue'>𓂀 𝓓𝓲𝓪𝓶𝓸𝓷𝓭 𝓟𝓻𝓲𝓬𝓮 𝓟𝓻𝓮𝓭𝓲𝓬𝓽𝓲𝓸𝓷 𓂀</h1>
<img align="right" width="400" height="400" src="https://github.com/SinghPriya5/Diamond_Price_Prediction/blob/main/static/images/2acca69efdfafcd6e527edd2c024b204_w200.webp">

## Table of content
* [Problem Statement](#Problem-Statement)
* [Goal](#Goal)
* [Approach](#Approach)
* [Data Collection](#Data-Collection)
* [Project Various Step](#project-various-step)
    * [Data Visualization](#Data-Visualization)
    * [Model Training](#Model-Training)
    * [Model Evalution](#Model-Evaluation)
    * [Model Selection](#Model-Selection)
    * [Model Dump](#Model-Dump)
* [Idle used](#idle-used)
* [Model Accuracy](#Model-Accuracy)
* [Continuous Improvement](#Continuous-Improvement)
* [Deployed](#Deployed)
* [Model Interpretation](#Model-Interpretation)
* [Web View](#Web-View)
* [Bug or Feature Request](#Bug-or-Feature-Request)
* [Future Scope](#Future-Scope)
* [Conclusion](#Conclusion)

## Problem Statement:
<ul>
<li><b>Objective:</b> Predict the price of diamonds based on their characteristics.</li>
<li><b>Target Variable:</b> The price of the diamond.</li>
<li><b>Features:</b> Attributes like carat, cut, color, clarity, depth, table, dimensions (length, width, height), etc.</li>
</ul>

## Goal:
The main goals of diamond price prediction using machine learning are:

<b>1.Accurate Pricing:</b> Predict diamond prices based on features like carat, cut, color, and clarity,depth.

<b>2.Market Insights:</b> Understand how different attributes impact pricing to inform buying and selling decisions.

<b>3.Automation:</b> Automate the valuation process for quicker, more efficient pricing.

<b>4.Fair Trade:</b> Ensure transparent and fair pricing in the diamond market.

<b>5.Customer Guidance:</b> Provide buyers with price estimates to help them make informed purchasing decisions.

## Approach:
The classical machine learning tasks like Data Exploration, Data Cleaning,
Feature Engineering, Model Building and Model Testing. Try out different machine
learning algorithms that’s best fit for the above case.

## Data Collection:
<ul>
<li><b>Dataset link :</b></li> - [Dataset](https://github.com/SinghPriya5/Diamond_Price_Prediction/commit/e4dc6a257d6b35cb57e66826a7ac36eb393ff225#diff-39848c601d6cbb866f8bad5bbb176d61062a4169f64fd86a5fffbae77eff78e8)
<li><b>Dataset:</b></li> Obtain a dataset containing various diamond attributes and their corresponding prices.
<li><b>Example Features:</b></li>
   
<b>id :</b> unique identifier of each diamond

<b>carat :</b> Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.

<b>cut :</b> Quality of Diamond Cut

<b>color :</b> Color of Diamond

<b>clarity :</b> Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.

<b>depth :</b> The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)

<b>table :</b> A diamond's table is the facet which can be seen when the stone is viewed face up.

<b>x :</b> Diamond X dimension

<b>y :</b> Diamond Y dimension

<b>x :</b> Diamond Z dimension

<li><b>Target variable:</b></li>

<b>price:</b> Price of the given Diamond.
</ul>

## Project Various Step:
Data Exploration I started exploring datasets using pandas, NumPy,matplotlib and seaborn.

## Data Visualization
Ploted colleration matrix to get insights about dependend and independed variables. Made chats like( Boxplot,countplot,distplot,pairplot,violinplot,scatterplot).

## Model Training
<b>Split Data:</b> Divide the dataset into training and test sets (80% training, 20% testing).

<b>Model Training:</b> Train the selected models using the training data.

<b>Hyperparameter Tuning:</b> Using Randomizedsearch CV to select the best parameter for training the model.

## Model Evaluation
<b>Metrics:</b> Evaluate model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²).

## Model Selection
Made many models but selected Random Forest Regressor.

## Model Dump
As per selected trained model is dumped to joblib format for app development

## Idle used
Jupyter Notebook,VS Code,PyCham

## Model Accuracy
95%

## Continuous Improvement
<b>Model Monitoring:</b> Track the model’s performance over time to ensure it remains accurate.
<b>Retraining: Periodically retrain the model with new data to maintain accuracy as market conditions change.</b>

## Deployed:
Deployed on heroku -- [Link](https://flight-fare-prediction.herokuapp.com/)

<br> the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

<b>Model Deployment:</b> Deploy the model to a production environment where it can make real-time predictions.

<b>APIs:</b> Develop an API that allows users to input diamond features and receive a predicted price.

## Model Interpretation
<b>Feature Importance:</b>Identify which features most influence the price prediction using techniques like feature importance scores in tree-based models or SHAP values.

<b>Partial Dependence Plots:</b>Visualize how changes in a single feature affect the predicted price, holding other features constant.

## Web View:
<img align="center" width="300" height="400" src="https://github.com/SinghPriya5/Diamond_Price_Prediction/blob/main/static/images/Frontend.png"> &nbsp;&nbsp;&nbsp; <!-- Three non-breaking spaces --><img align="center" width="300" height="400" src="https://github.com/SinghPriya5/Diamond_Price_Prediction/blob/main/static/images/Frontend.png"> &nbsp;&nbsp;&nbsp; <!-- Three non-breaking spaces --><img align="center" width="300" height="400" src="https://github.com/SinghPriya5/Diamond_Price_Prediction/blob/main/static/images/Frontend.png">
## Bug or Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an 
[issue](https://github.com/maityanubhab/Flight_Fare_Prediction/issues) here by including your search query and the expected result

## Future Scope
* Use multiple Algorithm
* Optimize Flask app.py
* Front-End
* Sentiment Analysis

## Conclusion
Diamond price prediction using machine learning involves a comprehensive approach, from data collection and preprocessing to model training, evaluation, and deployment. By accurately predicting prices, such a model can provide valuable insights to jewelers, appraisers, and consumers, leading to more informed decision-making in the diamond market.

# Thanks!!!
