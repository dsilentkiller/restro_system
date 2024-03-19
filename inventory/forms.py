from django import forms
from inventory.models import Inventory, Order


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.ChoiceField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ChoiceField(attrs={'class': 'forms.control'}),

        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'forms.control'}),

            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.RadioSelectField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ChoiceField(attrs={'class': 'forms.control'}),
            # 'table': forms.ChoiceField(attrs={'class': 'forms.control'}),
        }
