"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from timetable.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login/', login, name='login'),
    path('forgot/', forgot, name='forgot'),
    path('logout/', sign_out, name='logout'),
    path('logout1/', custom_logout, name='logout1'),
    path('register/', register, name='register'),
    path('dashboard/',dashboard, name='dashboard'),
    path('profile/',profile_view, name='profile'),
    path('create/',create, name='create'),
    path('register-teacher/', register_teacher, name='register_teacher'),
    path('configure-initial-parameters/', configure_initial_parameters, name='configure_initial_parameters'),
    path('input-practical-subjects/', input_practical_subjects, name='input_practical_subjects'),
    path('process-practical_subjects/', process_practical_subjects, name='process_practical_subjects'),
    path('input-theory-data/', input_theory_data, name='input_theory_data'),
    path('generate-timetables/', generate_timetables, name='generate_timetables'),
    path('process-theory-data/',process_theory_data, name='process_theory_data'),

]

