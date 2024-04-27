from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    #path ("URL",Views.Name Of Views),
    path('',views.index),
    path("cookie",views.saveCookie),

    
    path("se3", views.se3),
    path("dbms",views.dbms),
    path("M3",views.m3),
    path("pcpf",views.pcpf),
    path("dsa",views.dsa),
    # path("pcom",views.pcom),

    path("se4", views.se4),
    path("m4", views.m4),
    path("at",views.at),
    path("coa",views.coa),
    path("cnnd",views.cnnd),
    path("os",views.os),
            ]