from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class Class_view(TemplateView):
    template_name = 'second_task/class_template.html'


def func_view(request):
    return render(request, 'second_task/func_template.html')


def index(request):
    return render(request, 'index.html')