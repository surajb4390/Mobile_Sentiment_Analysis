# Mobile Sentiment Analysis

# Table of contents:
   1.  Overview
   2.  Website Link
   3.  Installation
   4.  Technical aspect
   5.  Technologies Used
   6.  Workflow
# Overview:
In this repository, we will learn step by step guide to create project on sentement analysis  using Machine Learning by using Random Forest Algorithm and deploy it on Heroku with Flask
# Website Link:
https://mobile-sentiment-analysis.herokuapp.com/
# Installation:
Entire code is written in Python 3.9. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install. To download all the packages used in the project, type the below command.
pip install -r requirements.txt

# Technical Aspect:
   1.  Python 3.9
   2.  Front-end: HTML
   3.  Back-end: Flask
   4.  IDE: Jupyter Notebook, VS Code
   5.  Deployment: Heroku

# Technologies Used:
   1.  Pandas
   2.  Numpy
   3.  Matplotlib
   4.  Seaborn
   5.  Sci-kit learn
   6.  Flask
   7.  Gunicorn
   8.  Heroku
   9.  NLTK


# Workflow:
   # Data Collection:
   Apple iPhone SE data set from Kaggle
 
 # Data Pre-processing:
   1.  Removed all stopwords
   2.  Removed all the numbers(0-9)
   3.  Converted all text data in lowercase
   4.  By using CountVectorizer converted data into features
   5.  Imbalanced dataset handled by SMOTE
   6.  Selected maximum 5000 features for model implementation
 
 # Model Implementation and Evaluation:
   1.  Naïve Bayes,Random Forest algorithm tested
   2.  Random Forest gives better result. So here Random Forest used for training and testing
   3.  Model performance evaluated based on accuracy, confusion matrix
   
 # Model Deployment:
 The final model is deployed on Heroku using Flask framework
