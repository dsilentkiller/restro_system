from django.contrib import admin
from django.urls import path
from menu import views
app_name = 'menu'


urlpatterns = [

    # menu
    path('create/', views.MenuCreateView.as_view(), name='create'),
    path('list/', views.MenuListView.as_view(), name='list'),
    path('update/', views.MenuUpdateView.as_view(), name='update'),
    path('detail/', views.MenuListView.as_view(), name='detail'),



]
