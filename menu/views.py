

# Create your views here.
from django.shortcuts import render
from menu.models import MenuItem, Receipe, Category, Ingredient
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from menu.forms import MenuItemForm, ReceipeForm, CategoryForm, IngredientForm


class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu/menuitem_list.html'
    success_url = reverse_lazy('menu:list')
    queryset = MenuItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = self.queryset
        return context


class MenuCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/menuitem_form.html'
    success_url = reverse_lazy('menu:list')


class MenuUpdateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/menuitem_form.html'
    success_url = reverse_lazy('menu:list')


class MenuDetailView(CreateView):
    model = MenuItem
    template_name = 'menu/menu_detail.html'
    success_url = reverse_lazy('menu:list')


class MenuDeleteView(DeleteView):
    model = MenuItem
    template_name = 'menu/delete.html'
    success_url = reverse_lazy('menu:list')

# receipe


class ReceipeListView(ListView):
    model = Receipe
    template_name = 'menu/receipe/receipe_list.html'
    success_url = reverse_lazy('menu:list')
    queryset = Receipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receipe'] = self.queryset
        return context


class ReceipeCreateView(CreateView):
    model = Receipe
    form_class = ReceipeForm
    template_name = 'menu/receipe/receipe_form.html'
    success_url = reverse_lazy('menu:list')


class ReceipeUpdateView(CreateView):
    model = Receipe
    form_class = ReceipeForm
    template_name = 'menu/receipe/receipe_form.html'
    success_url = reverse_lazy('menu:list')


class ReceipeDetailView(CreateView):
    model = Receipe
    template_name = 'menu/receipe/receipe_detail.html'
    success_url = reverse_lazy('menu:list')


class ReceipeDeleteView(DeleteView):
    model = Receipe
    template_name = 'menu/receipe/receipe_delete.html'
    success_url = reverse_lazy('menu:list')

# =========================== category==============================


class CategoryListView(ListView):
    model = Category
    template_name = 'menu/category/category_list.html'
    success_url = reverse_lazy('menu:category_list')
    # queryset = Receipe.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['receipe'] = self.queryset
    #     return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'menu/category/category_form.html'
    success_url = reverse_lazy('menu:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'menu/category/category_form.html'
    success_url = reverse_lazy('menu:category_list')


class CategoryDetailView(CreateView):
    model = Category
    template_name = 'menu/category/category_detail.html'
    success_url = reverse_lazy('menu:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'menu/category/category_delete.html'
    success_url = reverse_lazy('menu:category_list')


def SearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Category.objects.none()  # initialize an empty queryset

    if query:

        results = Category.objects.filter(name__icontains=query)

        return render(request, 'menu/category/category_list.html', {'object_list': results})
    else:
        results = Category.objects.none()

# ================================ ingredient ===========================


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'menu/ingredient/ingredient_list.html'
    success_url = reverse_lazy('menu:ingredient_list')
    # queryset = Receipe.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['receipe'] = self.queryset
    #     return context


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'menu/ingredient/ingredient_form.html'
    success_url = reverse_lazy('menu:ingredient_list')


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = Ingredientgit Form
    template_name = 'menu/ingredient/ingredient_form.html'
    success_url = reverse_lazy('menu:ingredient_list')


class IngredientDetailView(CreateView):
    model = Ingredient
    template_name = 'menu/ingredient/ingredient_detail.html'
    success_url = reverse_lazy('menu:ingredient_list')


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'menu/ingredient/ingredient_delete.html'
    success_url = reverse_lazy('menu:ingredient_list')


def IngredientSearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Ingredient.objects.none()  # initialize an empty queryset

    if query:

        results = Ingredient.objects.filter(name__icontains=query)

        return render(request, 'menu/ingredient/ingredient_list.html', {'object_list': results})
    else:
        results = Ingredient.objects.none()
