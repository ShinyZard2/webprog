from django.shortcuts import render, redirect, get_object_or_404
from .models import Plan
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def uhome(request):
    plan = Plan.objects
    return render(request, 'users/uhome.html', {'plan': plan})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']:
            plan = Plan()
            plan.title = request.POST['title']
            plan.body = request.POST['body']
            plan.pub_date = timezone.datetime.now()
            plan.hunter = request.user
            plan.save()
            return redirect('/users/' + str(plan.id))
        else:
            return render(request, 'users/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'users/create.html')


def fitplan(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    return render(request, 'users/userfit.html', {'plan': plan})


@login_required(login_url="/accounts/signup")
def upvotes(request, plan_id):
    if request.method == 'POST':
        plan = get_object_or_404(Plan, pk=plan_id)
        plan.likes += 1
        plan.save()
        return redirect('/users/' + str(plan.id))