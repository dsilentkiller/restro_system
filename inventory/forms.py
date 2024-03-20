from django import forms
from inventory.models import Inventory, Order, Purchase, Item


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')
        widgets = {
            # 'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),


        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('__all__')
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.RadioSelectField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
            # 'table': forms.ModelChoiceField(attrs={'class': 'forms.control'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'forms.control'})
        }
