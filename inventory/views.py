from django.shortcuts import render
from inventory.models import Inventory, Order, Purchase, Item, Table
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventory.forms import InventoryForm, PurchaseForm, OrderForm, ItemForm, TableForm
from menu.models import Recipe


def base(request):
    return render(request, 'inventory/base.html')
# ===============================================inventory =========================================##


class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')

# inventory search using function


class InventorySearchView(ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "inventory"

    success_url = reverse_lazy('inventory:inventory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            category__contains=self.request.GET.get(
                "category__name", ""),  # key value
            # foreign key bhakole search garna milena
            item__name__icontains=self.request.GET.get("item_name", ""),
            # price__contains=self.request.GET.get("price", ""),
            # quantity__contains=self.request.GET.get("quantity", ""),
        )
################################################################## item###########################


class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item/item_list.html'
    # success_url = reverse_lazy('inventory:item_list')


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item/item_form.html'
    success_url = reverse_lazy('inventory:item_list')


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item/item_form.html'
    success_url = reverse_lazy('inventory:item_list')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventory/item/item_detail.html'
    success_url = reverse_lazy('inventory:item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item/item_delete.html'
    success_url = reverse_lazy('inventory:item_list')

# inventory search using function


class ItemSearchView(ListView):
    model = Item
    template_name = "inventory/item/item_list.html"
    context_object_name = "item"

    # success_url = reverse_lazy('inventory:item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self, request):
    #     query = self.request.GET.get("q", "")
    #     results = Item.objects.none()
    #     if query:
    #         results = Item.objects.filter(name__icontains=query)
    #         return render(request, 'inventory/item/item_list.html', {'item': results})
    #     else:
    #         results = Item.objects.none()


def SearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Item.objects.none()  # initialize an empty queryset

    if query:

        results = Item.objects.filter(name__icontains=query)

        return render(request, 'inventory/item/item_list.html', {'object_list': results})
    else:
        results = Item.objects.none()
################################################################## table ###########################


class TableListView(ListView):
    model = Table
    template_name = 'inventory/table/table_list.html'
    success_url = reverse_lazy('inventory:table_list')


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = 'inventory/table/table_form.html'
    success_url = reverse_lazy('inventory:table_list')


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = 'inventory/table/table_form.html'
    success_url = reverse_lazy('inventory:table_list')


# class TableDetailView(DetailView):
#     model = Table
#     template_name = 'inventory/item/item_detail.html'
#     success_url = reverse_lazy('inventory:item_list')


class TableDeleteView(DeleteView):
    model = Table
    template_name = 'inventory/table/table_delete.html'
    success_url = reverse_lazy('inventory:table_list')

# inventory search using function


class TableSearchView(ListView):
    model = Table
    template_name = "inventory/table/table_list.html"
    context_object_name = "table"

    # success_url = reverse_lazy('inventory:item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self, request):
    #     query = self.request.GET.get("q", "")
    #     results = Item.objects.none()
    #     if query:
    #         results = Item.objects.filter(name__icontains=query)
    #         return render(request, 'inventory/item/item_list.html', {'item': results})
    #     else:
    #         results = Item.objects.none()


def SearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Table.objects.none()  # initialize an empty queryset

    if query:

        results = Table.objects.filter(name__icontains=query)

        return render(request, 'inventory/table/table_list.html', {'object_list': results})
    else:
        results = Table.objects.none()

# ================================================order -============================================================================


class OrderListView(ListView):
    model = Order
    template_name = 'inventory/order/order_list.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order/order_form.html'
    success_url = reverse_lazy('inventory:order_list')
    order = Order.objects.all()

    def form_valid(self, form):
        order = form.save(commit=False)
        order.save()
        # get order item
        order_items = Recipe.objects.filter(food_name=order.menu_item_name)

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     order = form.save(commit=False)
    #     order.save()

    #     recipes = Recipe.objects.filter(food_name=order.menu_item_name)
    #     for recipe in recipes:
    #         inventory_item = Inventory.objects.get(
    #             ingredient_name=recipe.ingredient_name)
    #         new_quantity = inventory_item.quantity - \
    #             (recipe.quantity * order.quantity)
    #         if new_quantity >= 0:
    #             inventory_item.quantity = new_quantity
    #             inventory_item.save()
    #         else:
    #             print('insufficient quantity')

    #     return response


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order/order_form.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'inventory/order/order_detail.html'
    success_url = reverse_lazy('inventory:order_list')


class OrderCancelView(DeleteView):
    model = Order
    template_name = 'inventory/order/order_cancel.html'
    success_url = reverse_lazy('inventory:order_list')
# =================================================================purchase==================================


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


def PurchaseSearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Purchase.objects.none()  # initialize an empty queryset

    if query:

        results = Purchase.objects.filter(item_name__icontains=query)

        return render(request, 'inventory/purchase/purchase_list.html', {'object_list': results})
    else:
        results = Purchase.objects.none()

# ==================================   StockReportListView ==============================


# class StockReportListView(ListView):
#     model = StockReport
#     template_name = 'inventory/stock_report_list.html'
#     success_url = reverse_lazy('inventory:stock_report')

#     def get_stock_remain(self):
#         stock = StockReport.objects.all()

#     def stock_remain(self):
#         inventory = Inventory.objects.filter(quantity='quantity')
#         stock = StockReport.objects.all()
#         inventory_quantity = self.inventory.quantity
#         order_quantity = self.order.quantity
#         remaining_stock = inventory_quantity - order_quantity
#         print(remaining_stock)

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


# def StockReportSearchView(request):
#     query = request.GET.get('q', '')  # retrieve the search query
#     results = StockReport.objects.none()  # initialize an empty queryset

#     if query:

#         results = StockReport.objects.filter(menu_item_name__icontains=query)

#         return render(request, 'inventory/stock_report_list.html', {'object_list': results})
#     else:
#         results = StockReport.objects.none()
