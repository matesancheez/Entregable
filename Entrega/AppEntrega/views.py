from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
def familiares(request):

    familiar1 = Familiar(nombre='Veronica', edad='52', nacimiento='31/07/1970')
    familiar2 = Familiar(nombre='Yosko', edad='57', nacimiento='22/05/1965')
    familiar3 = Familiar(nombre='Muny', edad='4', nacimiento='2/11/2017')

  
    return render(request, 'index.html', {'objetos':[familiar1, familiar2, familiar3]} )