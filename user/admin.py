from django.contrib import admin
from user.models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import authenticate
from user.forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
#     list_display = ('email',  'is_active',)
#     list_filter = ('is_active',)  # Remove 'email' from list_filter
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        # Wrap fields in a tuple
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2',  'is_active',), }))
    search_fields = ('email',)  # Enclose 'email' in a tuple
    ordering = ('email',)  # Enclose 'email' in a tuple
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
