# Phishing Domain Detection with Machine Learning

## 🔍 Overview

This project aims to detect whether a given domain URL is legitimate or a phishing website. Phishing is a common cyber-attack where attackers disguise as trustworthy entities to trick victims into revealing sensitive information like login credentials and account details. This system uses machine learning models to identify and classify URLs as either legitimate or malicious, helping to prevent phishing attacks.

## 🎯 Objective

The objective of this project is to develop a domain authentication system that can accurately classify URLs as either legitimate or malicious. The system leverages machine learning models trained on features extracted from URLs to distinguish between real and fraudulent domains.

## 🚀 Project Workflow

The project follows a standard machine learning workflow:
1. **Data Collection**
2. **Feature Extraction**
3. **Model Training and Evaluation**
4. **Deployment of the Trained Model**

### 1. Data Collection

The dataset for this project contains approximately 450k domain URLs, where 345k are legitimate and 104k are malicious. Since the dataset is imbalanced, the SMOTE (Synthetic Minority Oversampling Technique) technique is used to oversample the minority class, increasing the dataset size to around 600k samples.

### 2. Feature Extraction

The dataset initially consists of only legitimate and malicious URLs. To improve its usefulness for machine learning, several features are extracted from the URLs. These features fall into three main categories:

- **Length-based Features**: 5 features related to the length of the URL and its components.
- **Count-based Features**: 11 features based on the counts of specific characters or patterns (e.g., dots, slashes).
- **Binary Features**: 2 binary features that indicate the presence or absence of certain elements (e.g., "https" protocol).

In total, 18 features are extracted from each URL.

### 3. Model Training and Evaluation

This is a binary classification problem. The extracted features are used to train multiple machine learning models, and the model with the best performance is selected. The models tested in this project include:

- **Decision Tree**
- **Random Forest**
- **Multilayer Perceptron (MLP)**

Among these, the Multilayer Perceptron (MLP) provided the highest accuracy of 99%, with a well-balanced precision and recall. The trained model is saved for further use.

### 4. Deployment

After training and evaluating the models, the best-performing model is saved and can be used for predictions.

## 👨‍💻 Running the Project Locally

To run the project locally, follow these steps:

1. Clone the repository using Git:
   ```bash
   git clone https://github.com/NagabalajiKN/phishing_detector_model
2. Install the required dependencies in a virtual environment:
   ```bash
   pip install -r requirements.txt
3. Import the get_prediction() function from API.py and pass the required arguments to make predictions.
   ```bash
   from API import get_prediction
   # path to the trained model
   model_path = r"/models/Malicious_URL_Prediction.h5"

   # input URL for prediction
   url = "www.example.com/"

   # get the prediction result
   prediction = get_prediction(url, model_path)
   print(prediction)
