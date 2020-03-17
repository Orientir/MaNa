from django.shortcuts import render

def home(request):
    return TemplateResponse(request, "home.html")
