from django.shortcuts import render

def index(request):
    context = {
        'title': 'Main page'
    }
    return render(request, 'index.html', context)

def home(request):
    context = {
        'title': 'Home page'
    }
    return render(request, 'home.html', context)