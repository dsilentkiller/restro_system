
from django.urls import path
from menu import views
app_name = 'menu'


urlpatterns = [

    # menu
    path('create/', views.MenuCreateView.as_view(), name='create'),
    path('list/', views.MenuListView.as_view(), name='list'),
    path('update/<int:pk>', views.MenuUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.MenuListView.as_view(), name='detail'),
    path('delete/<int:pk>', views.MenuDeleteView.as_view(), name='delete'),

    # category
    path('category/create/', views.CategoryCreateView.as_view(),
         name='category_create'),
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),

    path('category/update/<int:pk>', views.CategoryUpdateView.as_view(),
         name='category_update'),
    path('category/detail/<int:pk>', views.CategoryListView.as_view(),
         name='category_detail'),
    path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(),
         name='category_delete'),
    path('search', views.SearchView,
         name='category-search'),


    # receipe
    # menu
    path('receipe/create/', views.ReceipeCreateView.as_view(), name='receipe_create'),
    path('receipe/list/', views.ReceipeListView.as_view(), name='receipe_list'),
    path('receipe/update/<int:pk>',
         views.ReceipeUpdateView.as_view(), name='receipe_update'),
    path('receipe/detail/<int:pk>',
         views.ReceipeListView.as_view(), name='receipe_detail'),
    path('receipe/delete/<int:pk>', views.ReceipeDeleteView.as_view(),
         name='receipe_delete'),


]
