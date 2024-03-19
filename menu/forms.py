from django import forms
from menu.models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('__all__')
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'forms.control'}),
            'quantity': forms.TextInput(attrs={'class': 'forms.control'}),
            'price': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'unit': forms.ChoiceField(attrs={'class': 'forms.control'}),
            'description': forms.TextInput(attrs={'class': 'forms.control'}),
            # 'category': forms.ChoiceField(attrs={'class': 'forms.control'}),

        }
