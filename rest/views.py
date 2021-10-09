from django.db import models
from django.shortcuts import render
from rest.models import AnalysisModel
import requests, time

def rest(request):
    return render(request, 'index.html')

def callapi(request):

    path = '/image/sample/001.jpg'
    if request.POST['image_path']:
        path = request.POST.get('image_path')
    
    request_time = int(time.time())

    url = 'http://localhost:5000/api-mock'
    payload = { 'image_path': path }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return render(request, 'result.html', { 'result' : e })

    analysis_json = response.json()

    print('★★★')
    print(analysis_json)
    print(path)
    print(analysis_json['success'])
    print(analysis_json['message'])
    estimate_data = analysis_json['estimated_data']
    print(estimate_data)

    analysis_class = 0
    confidence = 0.0000
    if 'class' in estimate_data:
        print(estimate_data['class'])
        analysis_class = estimate_data['class']
    
    if 'confidence' in estimate_data:
        print(estimate_data['confidence'])
        confidence = estimate_data['confidence']
    
    response_time = int(time.time())

    print(request_time)
    print(response_time)

    create_data = AnalysisModel.objects.create(
       image_path = path,
       success = analysis_json['success'],
       message = analysis_json['message'],
       class_ai = analysis_class,
       confidence = confidence,
       request_timestamp = request_time,
       response_timestamp = response_time
    )

    return render(request, 'result.html', { 'result' : analysis_json })

