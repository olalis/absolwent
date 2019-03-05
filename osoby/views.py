from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
    return HttpResponse("<h1>Witaj w django</h1")


# Create your views here.
