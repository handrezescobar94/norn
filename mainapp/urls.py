from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('inicio/', views.inicio_page, name='inicio'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]