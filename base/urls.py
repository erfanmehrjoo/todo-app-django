"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import TaskDetail , TaskList , CustomLoginView ,  RegisterPage , TaskCreate  , TaskUpdate , TaskDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/" , CustomLoginView.as_view() , name="login"),
    path("logout/" , LogoutView.as_view(next_page="login") , name="logout"),
    path("register/" , RegisterPage.as_view() , name="register"),
    path("" , TaskList.as_view() , name="tasks"),
    path("task/<int:pk>/" , TaskDetail.as_view() , name="task"),
    path("task-create/" , TaskCreate.as_view() , name="task-create"),
    path("task-update/<int:pk>/" , TaskUpdate.as_view() , name="task-update"),
    path("task-delete/<int:pk>" , TaskDelete.as_view() , name="task-delete"),
]
