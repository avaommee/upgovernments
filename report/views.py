from django.shortcuts import render
from .models import patients
# Create your views here.

def index(request):
    return render(request, 'index.html')

def safe(request):
    if request.method == 'POST':
        name = request.POST['nm']
        place = request.POST['pl']
        clothe = request.POST['clo']
        radio = request.POST['gen']
        date = request.POST['dt']
        category = request.POST['cate']
        document = request.FILES['dc']
        photo = request.FILES['ph']
        if patients(name=name, place=place, clothe=clothe, gender=radio, date=date, category=category, document=document, photo=photo):
            if patients.objects.filter(photo=photo):
                return render(request, 'register.html', {'msg': 'This Photo is Already Exist'})
            else:
                patients(name=name, place=place, clothe=clothe, gender=radio, date=date, category=category, document=document, photo=photo).save()
                msg = "SUBMITTED SUCCESSFUL"
                return render(request, 'register.html', {'msg': msg})
        else:
            msg = "Please Fill Detail"
        return render(request, 'register.html', {'msg': msg})

def admin(request):
    return render(request, 'register.html')

def fetch(request):
    if request.method == 'POST':
        date = request.POST['dt']
        radio = request.POST['gen']
        category = request.POST['cate']
        if patients.objects.filter(date=date,gender=radio, category=category):
            data = patients.objects.filter(date=date, gender=radio, category=category).all()
            return render(request, 'index.html', {'data': data})
        else:
            msg = "Data Not Find"
            return render(request, 'index.html', {'msg': msg})


