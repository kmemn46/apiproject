from django.shortcuts import render
import requests

def rest(request):
    return render(request, 'index.html')

def callapi(request):

    path = '/image/sample/001.jpg'
    if request.POST['image_path']:
        path = request.POST.get('image_path')
    
    # API call (mock呼び出し)
    url = 'http://localhost:5000/api-mock'
    payload = { 'image_path': path }
    result = requests.post(url, data=payload)

    print(result.text)

    # Modelに登録
    return render(request, 'result.html', { 'result' : result.text })

