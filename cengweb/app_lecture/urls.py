from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^firstclass/', views.classone, name="firstclass"),
    url(r'^secondclass/', views.classone, name="secondclass"),
    url(r'^thirdclass/', views.classone, name="thirdclass"),
    url(r'^fourthclass/', views.classone, name="fourthclass"),
]
