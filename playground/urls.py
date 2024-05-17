
from django.urls import path
from . import views


#array of paths
urlpatterns = [
    path("hello/", views.say_hello)
]