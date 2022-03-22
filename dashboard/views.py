from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login/')
def load_dashboard(request):
    return HttpResponse("вот тут будет дашборд")
