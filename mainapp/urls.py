from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('inicio/', views.inicio_page, name='inicio'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login-log/', views.login_logs, name='login_logs'),
    #path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('filter-login-log/', views.filter_login_logs, name='filter_login_logs'),
]