from django.http import HttpResponse
from django.shortcuts import render


def bmi(request):
    return render(request, 'bmi/bmi.html')


def yourbmi(request):
    val1 = int(request.GET['mass'])
    val2 = int(request.GET['height'])
    res = val1 / val2**2
    return render(request, 'bmi/yourbmi.html', {'result': res})
