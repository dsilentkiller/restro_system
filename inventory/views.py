from django.shortcuts import render
from inventory.models import Inventory, Order, Purchase, StockReport
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventory.forms import InventoryForm, PurchaseForm, OrderForm


def base(request):
    return render(request, 'inventory/base.html')
# inventory


class InventoryListView(ListView):
    model = Inventory
    template = 'inventory/inventory_list.html'
    success_url = reverse_lazy('inventory:index')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')


class InventoryDetailView(DetailView):
    model = Inventory
    template = 'inventory/detail.html'
    success_url = reverse_lazy('inventory:list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template = 'inventory/delete.html'
    success_url = reverse_lazy('inventory:list')

# order


class OrderListView(ListView):
    model = Order
    template = 'order/order_list.html'
    success_url = reverse_lazy('inventory:order_index')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')
    # order = Order.objects.all()


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderDetailView(DetailView):
    model = Order
    template = 'inventory/order/order_detail.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderDeleteView(DeleteView):
    model = Order
    template = 'inventory/order/order_delete.html'
    success_url = reverse_lazy('inventory:order_list')
# purchase


class PurchaseListView(ListView):
    model = Purchase
    template = 'inventory/purchase_list.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template = 'purchase/purchase_form.html'
    success_url = reverse_lazy('inventory:purchase_index')
    # order = Order.objects.all()


class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template = 'purchase/purchase_form.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseDetailView(DetailView):
    model = Purchase
    template = 'purchase/purchase_detail.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template = 'purchase/purchase_delete.html'
    success_url = reverse_lazy('inventory:purchase_index')

# StockReportListView


class StockReportListView(ListView):
    model = StockReport
    print('hell')
    template = 'inventory/stockreport_list.html'
    print('hell')
    # success_url = reverse_lazy('inventory:stock_report')

    def stock_remain(request):
        stock = StockReport.objects.all()
        print('hello')
        return render(request, 'inventory/stockreport_list', {'stock_remain': stock})
