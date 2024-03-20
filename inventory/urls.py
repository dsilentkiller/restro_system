from django.contrib import admin
from django.urls import path
from inventory import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'inventory'


urlpatterns = [
    path('', views.base, name='base'),
    # inventory
    path('create/', views.InventoryCreateView.as_view(), name='create'),
    path('list/', views.InventoryListView.as_view(), name='list'),
    path('update/', views.InventoryUpdateView.as_view(), name='update'),
    path('detail/', views.InventoryListView.as_view(), name='detail'),
    # order
    path('inventory/order/list/', views.OrderListView.as_view(), name='order_index'),
    path('order/create/',
         views.OrderCreateView.as_view(), name='order_create'),

    path('inventory/order/update/',
         views.OrderUpdateView.as_view(), name='order_update'),




    path('inventory/order/detail/',
         views.OrderListView.as_view(), name='order_detail'),
    path('inventory/search',
         views.InventorySearchView.as_view(), name='inventory_search'),




    # purchase
    path('purchase/list/', views.PurchaseListView.as_view(), name='purchase_index'),
    path('purchase/create/',
         views.PurchaseCreateView.as_view(), name='purchase_create'),

    path('purchase/update/',
         views.PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase/detail/', views.PurchaseListView.as_view(),
         name='purchase_detail'),

    path('stock/report', views.StockReportListView.as_view(),
         name='stock_report'),

]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
