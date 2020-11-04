from django.shortcuts import render, HttpResponse
from .models import File_Upload
from django.template import loader
import os

def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        with open(f'media/{file2.name}','wb') as f:
            f.write(file2.read())

        os.system(f'python detect/detect.py --source media/{file2.name} --weights model_files/last.pt')
        context = {'detected_image' : f'inference/detect/inference/output/{file2.name}'}
        print(context)
        # return render(request,'output.html')
        template = loader.get_template('output.html')
        context = {'detected_image' : f'static/inference/output/{file2.name}'}
        response =  HttpResponse(template.render(context, request))
        return response

    return render(request, "index.html")



