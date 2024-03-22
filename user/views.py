from django.shortcuts import render

from user.models import CustomUser
from django.views.generic import FormView
from django.urls import reverse_lazy
from user.forms import LoginForm
# from inventory.forms import InventoryForm, PurchaseForm, OrderForm, ItemForm, TableForm


class LoginView(FormView):
    model = CustomUser
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('inventory:inventory_list')
