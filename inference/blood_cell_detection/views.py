from django.shortcuts import render, HttpResponse
from .models import File_Upload

def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = File_Upload.objects.create(file = file2)
        document.save()
        context = {}
        return render(request, "index.html", context)
    return render(request, "index.html")


# def home(request):
#     if request.method == "POST":
#         file2 = request.FILES["file"]
#         with open(f'{file2.name}.png','wb') as f:
#             f.write(file2.read())
#         # document = File_Upload.objects.create(file = file2)
#         # document.save()
#         # context = {}
#         return render(request, "index.html",)
#     return render(request, "index.html")
