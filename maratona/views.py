from django.shortcuts import render
from maratona.models import Class

def index(request):
    return render(
        request,
        'index.html'
    )

def class_list(request):
    classes = Class.objects.all()
    return render(
        request,
        'class_list.html',
        {
            'classes': classes
        }
    )