"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from accounts import views as account

urlpatterns = [
    path('register/', account.registerUser, name="userRegister"),
    path('registeradmin/', account.registerAdmin, name="adminRegister"),
    path('login/', account.loginUser, name="adminandUserLogin"),
    path('logout/', account.logoutUser, name="logout"),
    path('edit/', account.updateProfile, name="update"),
    path('password/', account.changePassword, name="changepass"),
    path('', account.home, name="home"),
    path('admin/', admin.site.urls),
]
