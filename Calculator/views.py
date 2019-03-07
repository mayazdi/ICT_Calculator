from django.http import HttpResponse
from django.shortcuts import render
from py_expression_eval import Parser


# Create your views here.

def default_new(request):
    return render(request, 'index.html', {'result': ''})


def default(request, equ):
    expression = equ.replace("div", "/")
    parser = Parser()
    try :
        result = parser.parse(expression).evaluate({})
        parsed = True
    except :
        result = "Bad Expression"
        parsed = False
    return render(request, 'index.html', {'result': result, 'parsed': parsed})
