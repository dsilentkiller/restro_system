from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static
from user.urls import views
app_name = 'user'


urlpatterns = [
    # path('', views.base, name='base'),
    # ==================user=================================
    path('', views.LoginView.as_view(), name='login'),
    # path('list/', views.InventoryListView.as_view(), name='inventory_list'),
    # path('update/<int:pk>', views.InventoryUpdateView.as_view(), name='update'),
    # path('detail/<int:pk>', views.InventoryDetailView.as_view(),
    #  name='inventory_detail'),
    # path('delete/<int:pk>', views.InventoryDeleteView.as_view(),
    #  name='inventory_delete'),
    # path('inventory/search',
    #      views.InventorySearchView.as_view(), name='inventory_search'),
    # =========================item==================










]
