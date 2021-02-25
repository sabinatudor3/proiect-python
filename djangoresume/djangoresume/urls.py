"""djangoresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path('', views.home_view, name = "home"),
    path('profile/', views.get_data, name = "profile"),
    path('tech/', views.get_tech, name = "tech"),
    path('skills/', views.get_skills, name = "skills"),
    path('work/', views.get_work, name = "work"),
    path('education/', views.get_education, name = "education"),
    path('language/', views.get_language, name = "language"),
    path('template/', views.get_template, name = "template"),
    path('template1/', views.template1_view, name = "template1"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('admin/', admin.site.urls),
]
