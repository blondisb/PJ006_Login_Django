from django.urls import path, include
from . import views as vw

urlpatterns = [
    path('', vw.VW_home, name='URL_home'),
    path('products/', vw.VW_products, name='URL_products'),
    path('logout/', vw.VW_exit, name='URL_logout'),
]
