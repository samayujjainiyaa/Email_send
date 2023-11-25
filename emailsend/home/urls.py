from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('sendotp/',views.sendotp,name="sendotp"),
    path('varifyotp/',views.varifyotp,name="varifyotp"),
]
