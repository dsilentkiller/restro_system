from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from menu.models import MenuItem
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from menu.forms import MenuItemForm


class MenuListView(ListView):
    model = MenuItem
    template = 'menu/menuitem_list.html'
    success_url = reverse_lazy('menu:list')


class MenuCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template = 'menu/menuitem_form.html'
    success_url = reverse_lazy('menu:list')


class MenuUpdateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template = 'menu/menuitem_form.html'
    success_url = reverse_lazy('menu:list')


class MenuDetailView(CreateView):
    model = MenuItem
    template = 'menu/menu_detail.html'
    success_url = reverse_lazy('menu:list')


class MenuDeleteView(DeleteView):
    model = MenuItem
    template = 'menu/delete.html'
    success_url = reverse_lazy('menu:list')
