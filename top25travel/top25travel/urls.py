"""top25travel URL Configuration

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
from beach import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('1/', views.data1),
    path('3/', views.data2),
    path('4/', views.data3),
    path('5/', views.data4),
    path('6/', views.data5),
    path('7/', views.data6),
    path('8/', views.data7),
    path('9/', views.data8),
    path('10/', views.data9),
    path('11/', views.data10),
    path('12/', views.data11),
    path('13/', views.data12),
    path('14/', views.data13),
    path('15/', views.data14),
    path('16/', views.data15),
    path('17/', views.data16),
    path('18/', views.data17),
    path('19/', views.data18),
    path('20/', views.data19),
    path('21/', views.data20),
    path('base/', views.viewbase)
]
