from django.contrib import admin
from django.urls import path
from inventory import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'inventory'


urlpatterns = [
    path('', views.base, name='base'),
    # ==================inventory=================================
    path('create/', views.InventoryCreateView.as_view(), name='create'),
    path('list/', views.InventoryListView.as_view(), name='inventory_list'),
    path('update/<int:pk>', views.InventoryUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.InventoryDetailView.as_view(),
         name='inventory_detail'),
    path('delete/<int:pk>', views.InventoryDeleteView.as_view(),
         name='inventory_delete'),
    path('inventory/search',
         views.InventorySearchView.as_view(), name='inventory_search'),
    # =========================item==================
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/list/', views.ItemListView.as_view(), name='item_list'),
    path('item/update/<int:pk>', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/detail/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/delete/<int:pk>', views.ItemDeleteView.as_view(),
         name='item_delete'),
    path('item/search',
         views.ItemSearchView.as_view(), name='item_search'),




    # ===================  order================================
    path('inventory/order/list/', views.OrderListView.as_view(), name='order_index'),
    path('order/create/',
         views.OrderCreateView.as_view(), name='order_create'),

    path('inventory/order/update/',
         views.OrderUpdateView.as_view(), name='order_update'),
    path('inventory/order/detail/',
         views.OrderListView.as_view(), name='order_detail'),





    # =================================  purchase===============================
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
