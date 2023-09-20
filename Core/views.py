from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_us_view(request):
    return render(request, 'about_us.html')

