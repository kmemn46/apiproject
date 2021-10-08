from django.shortcuts import render

# Create your views here.

def rest(request):
    return render(request, 'index.html')

def callapi(request):

    print("callapi entered")
    # path = '/image/sample/001.jpg'
    # if request.POST['image_path']:
    #     path = request.POST.get('image_path')

    # 処理を書きます
    #object_list = {"sucsess" : "true" }
    return render(request, 'result.html')

