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
    template_name = 'inventory/inventory_list.html'
    success_url = reverse_lazy('inventory:index')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/detail.html'
    success_url = reverse_lazy('inventory:list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/delete.html'
    success_url = reverse_lazy('inventory:list')

# inventory search using function

class InventorySearchView(ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "inventory"

    success_url = reverse_lazy('inventory:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            category__name__contains=self.request.GET.get(
                "name", ""),  # key value
            # category__name__contains=self.request.GET.get("name", ""),
        )

# order


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    success_url = reverse_lazy('inventory:order_index')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')
    # order = Order.objects.all()


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'inventory/order/order_detail.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'inventory/order/order_delete.html'
    success_url = reverse_lazy('inventory:order_list')
# purchase


class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase/purchase_list.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase/purchase_form.html'
    success_url = reverse_lazy('inventory:purchase_index')
    # order = Order.objects.all()


class PurchaseUpdateView(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/purchase/purchase_form.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name_name = 'inventory/purchase/purchase_detail.html'
    success_url = reverse_lazy('inventory:purchase_index')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'inventory/purchase/purchase_delete.html'
    success_url = reverse_lazy('inventory:purchase_index')

# StockReportListView


class StockReportListView(ListView):
    model = StockReport
    template_name = 'inventory/stock_report_list.html'

    success_url = reverse_lazy('inventory:stock_report')

    def get_stock_remain(self):
        stock = StockReport.objects.all()

    def stock_remain(self):
        inventory = Inventory.objects.filter(quantity='quantity')
        stock = StockReport.objects.all()
        inventory_quantity = self.inventory.quantity
        order_quantity = self.order.quantity
        remaining_stock = inventory_quantity - order_quantity
        print(remaining_stock)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # inventory = Inventory.objects.filter(
    #     #     quantity='quantity')  # calling all inventory obj
    #     inventory = Inventory.objects.values(
    #         'item_name').annotate(total_quantity=Sum('quantity'))
    #     stock_remain = {}  # dictionary to stroe stock remain
    #     for item in inventory:
    #         order_quantity = inventory
    #         remaining_stock = item.quantity - total_order_quantity
    #         stock_remain[item.item_name] = remaining_stock
    #     context['stock_remain'] = stock_remain
    #     return context
