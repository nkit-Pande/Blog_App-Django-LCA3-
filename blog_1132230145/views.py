from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Service, PersonalInfo
from blog.forms import PersonalForm


def register(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PersonalForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    blogData = Service.objects.all()
    try:
        personalInfo = PersonalInfo.objects.all().first()
    except PersonalInfo.DoesNotExist:
        personalInfo = None
    data = {
        'blogData':blogData,
        'personalInfo':personalInfo
    }
    return render(request,'home.html',data)


def logOut(request):
    PersonalInfo.objects.all().delete()
    return redirect('home')


def detail(request, blog_id):
    blogData = Service.objects.get(id=blog_id)
    return render(request, 'detail.html', {'blogData': blogData})