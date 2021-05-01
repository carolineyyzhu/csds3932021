from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('PoSB', views.posb, name="PoSB"),
    path('RChecker', views.rchecker, name="RChecker"),
    path('posb', views.posb, name="PoSB")
]
