"""cengweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from app_lecture import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^candidate/', views.candidate, name="candidate"),
    url(r'^admin/', admin.site.urls),
    url(r'^lectures/', include('app_lecture.urls')),
    url(r'^lecturers/', include('app_lecturer.urls')),
    url(r'^lab/', include('app_lab.urls')),
    url(r'^developers/', include('developers.urls')),
    url(r'^report', views.report),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




