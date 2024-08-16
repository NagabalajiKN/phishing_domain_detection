import numpy as np
from tensorflow import keras
from .Feature_Extractor import extract_features

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    # Convert the list to a numpy array and reshape it
    url_features_array = np.array(url_features).reshape(1, -1)
    prediction = model.predict(url_features_array)

    i = prediction[0][0] * 100
    i = round(i, 3)
    print(f"There is {i}% chance the URL is malicious!")

    return i