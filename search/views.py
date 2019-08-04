from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import logging
from .models import WordBank


def index(request, template_name='index.html'):
    return render(request, template_name)

def configure(request, template_name='configure.html'):
    return render(request, template_name)
