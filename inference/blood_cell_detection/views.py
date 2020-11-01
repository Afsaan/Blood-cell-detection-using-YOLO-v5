from django.shortcuts import render, HttpResponse
from .models import FilesUpload

def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = documents.objects.create(file = file2)
        documen.save()
        return HttpResponse("you file was uploaded")
    return render(request, "index.html")
