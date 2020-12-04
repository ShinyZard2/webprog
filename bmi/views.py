from django.http import HttpResponse
from django.shortcuts import render

def bmi(request):
    return render(request, 'bmi/bmi.html')

def yourbmi(request):
    val1 = int(request.GET['mass'])
    val2 = float(request.GET['height'])
    unit1 = request.GET['wUnit']
    unit2 = request.GET['hUnit']

    if unit1 == 'lb':
        val1 = val1 * 0.45359237
    else:
        val1 = val1

    if unit2 == 'in':
        val2 = val2 * 0.0254
    else:
        val2 = val2 / 100

    res = round(val1 / val2**2, 2)

    return render(request, 'bmi/yourbmi.html', {'result': res})
