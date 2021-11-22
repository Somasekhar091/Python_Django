"""myProject URL Configuration

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
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hii/',views.hii,name='hii'),
    path('one/',views.one,name='one'),
    path('home/',views.home,name='HOME'),
    path('sample2/<str:string>/<int:number>/',views.sample2,name='sample2'),
    path('basic/',views.basic,name='basic'),
    path('temp1/',views.temp1,name='temp1'),
    path('lost/<str:name>/<int:id>/',views.lost,name='lost'),
    path('table/<int:num>/',views.table,name='table'),
    path('table2/',views.table2,name='table2'),
    path('external/',views.external,name='external'),
    path('work/<int:num>/',views.work,name="work"),
    path('student_register/',views.student_register,name="student_register"),
    path('signup/',views.signup,name='signup'),
    path('student_update/<int:num>/',views.student_update,name="update"),
]
sdzfhjzsdf
sdjfv
djhfd
