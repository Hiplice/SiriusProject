from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .api_handler import *


@login_required(login_url='login/')
def load_dashboard(request):
    return HttpResponse('тут будет дашборд')


@login_required(login_url='login/')
def get_consent(request):
    return HttpResponse('ok')
