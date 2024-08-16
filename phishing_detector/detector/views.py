from django.shortcuts import render
from django.http import JsonResponse
from .api import get_prediction

def index(request):
    return render(request, 'detector/index.html')

def predict(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        model_path = r"C:\Users\LENOVO\Documents\Phishing-Attack-Domain-Detection\models\Malicious_URL_Prediction.h5"
        prediction = get_prediction(url, model_path)
        return JsonResponse({'prediction': prediction})
