from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^firstclass/', views.classone, name="firstclass"),
    url(r'^secondclass/', views.classtwo, name="secondclass"),
    url(r'^thirdclass/', views.classthree, name="thirdclass"),
    url(r'^fourthclass/', views.classfour, name="fourthclass"),
    url(r'^', views.developers, name="developers"),
]
