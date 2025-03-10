from django.shortcuts import render

def accueil(request):
    return render(request, 'APP/index.html')
