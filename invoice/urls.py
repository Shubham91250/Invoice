"""
URL configuration for invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from inv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('database/', views.database, name='database'),
    path('add/', views.add_invoice1, name='add_invoice1'),
    path('add1/', views.add_invoice2, name='add_invoice2'),
    path('provider/', views.add_provider,name='add_provider'),
    path('update_comapny/<int:id>',views.update_company,name='update_company'),
    path('delete/<int:id>',views.delete,name='delete'),
     path('delete_client/<int:pk>',views.delete_client,name='delete_client'),
    path('edit_client/<int:id>',views.edit_client,name='edit_client'),
    path('allList/',views.allList,name='allList'),
    path('review//<int:pk>/',views.review,name='review'),
    path('report_list/', views.report_list, name='report_list'),
    path('pdf_report/<int:pk>/', views.pdf_report, name='pdf_report')
]
