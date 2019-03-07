from django.http import HttpResponse
from django.shortcuts import render
import calculator
# Create your views here.


def default(request):
    return render(request, 'index.html')
