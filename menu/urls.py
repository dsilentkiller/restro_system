
from django.urls import path
from menu import views
app_name = 'menu'


urlpatterns = [

    # menu
    path('create/', views.MenuCreateView.as_view(), name='menu_create'),
    path('list/', views.MenuListView.as_view(), name='menu_list'),
    path('update/<int:pk>', views.MenuUpdateView.as_view(), name='menu_update'),
    path('detail/<int:pk>', views.MenuListView.as_view(), name='menu_detail'),
    path('delete/<int:pk>', views.MenuDeleteView.as_view(), name='menu_delete'),
    path('menu/search', views.MenuSearchView, name='menu_search'),

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

    # ingredient
    path('ingredient/create/', views.IngredientCreateView.as_view(),
         name='ingredient_create'),
    path('ingredient/list/', views.IngredientListView.as_view(),
         name='ingredient_list'),
    path('ingredient/update/<int:pk>',
         views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredient/detail/<int:pk>',
         views.IngredientListView.as_view(), name='ingredient_detail'),
    path('ingredient/delete/<int:pk>', views.IngredientDeleteView.as_view(),
         name='ingredient_delete'),
    path('ingredient/search', views.IngredientSearchView,
         name='ingredient_search'),


]
