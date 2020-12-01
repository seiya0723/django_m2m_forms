from django.urls import path
from . import views

app_name    = "menulist"
urlpatterns = [ 
    path('', views.index, name="index"),
]

