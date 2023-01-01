from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def VW_home(request):
    return render(request, 'CORE/home.html')

@login_required()
def VW_products(request):
    return render(request, 'CORE/products.html')

def VW_exit(request):
    logout(request)
    return redirect('URL_home')


