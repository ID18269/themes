django-admin startproject HomeWorks
cd HomeWorks

python manage.py startapp Themes
python manage.py startapp Pupils

# lessons.txt
Math
Science
History
Literature
Geography

from django.shortcuts import render

def themes_list(request):
    with open('lessons.txt', 'r') as f:
        lessons = f.readlines()
    return render(request, 'themes_list.html', {'lessons': lessons})

from django.urls import path
from . import views

urlpatterns = [
    path('themes/', views.themes_list, name='themes_list'),
]

from django.shortcuts import render

def pupils_list(request):
    pupils = [
        {'name': 'John Doe', 'grades': {'Math': 90, 'Science': 85, 'History': 75}},
        {'name': 'Jane Smith', 'grades': {'Math': 95, 'Science': 88, 'History': 80}},
        {'name': 'Alice Johnson', 'grades': {'Math': 85, 'Science': 75, 'History': 70}},
        {'name': 'Bob Brown', 'grades': {'Math': 78, 'Science': 82, 'History': 77}},
        {'name': 'Eve Wilson', 'grades': {'Math': 92, 'Science': 90, 'History': 85}},
    ]
    return render(request, 'pupils_list.html', {'pupils': pupils})

from django.urls import path
from . import views

urlpatterns = [
    path('pupils/', views.pupils_list, name='pupils_list'),
]

