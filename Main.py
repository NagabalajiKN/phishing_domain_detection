
from API import get_prediction

# path to trained model
model_path = r"C:\Users\LENOVO\Documents\Phishing-Attack-Domain-Detection\models\Malicious_URL_Prediction.h5"

# input url
url = "http://www.amaz0n-support.com"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)
