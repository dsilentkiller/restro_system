from django import forms
from menu.models import MenuItem, Recipe, Category, Ingredient


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('food_name', 'price', 'category')
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'forms.control'}),
            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms.control'}),
            'description': forms.Textarea(attrs={'class': 'forms.control'}),


        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('__all__')
        widgets = {

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),


        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms.control'}),



        }
