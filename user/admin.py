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
    list_display = ('email',  'is_active',)
    list_filter = ('email',)  # Remove 'email' from list_filter
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        # Wrap fields in a tuple
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}),)

    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["email",  "password1", "password2", "is_active"],
    #         },
    #     ),
    # ]
    search_fields = ('email',)  # Enclose 'email' in a tuple
    ordering = ('email',)  # Enclose 'email' in a tuple
    # filter_horizontal = ()

    # def get_fieldsets(self, request, obj=None):
    #     if not request.user.is_superuser:
    #         if obj:
    #             if isinstance(obj, CustomUser):
    #                 fieldsets = (
    #                     (None, {'fields': ('email', 'password',)}),
    #                     (('Personal info'), {'fields': ('first_name', 'last_name', 'profession_title',
    #                                                     'country', 'city', 'postal_code', 'address', 'workplace', 'phone_nr', 'birth_date')}),
    #                     (('Permissions'), {'fields': ('is_active',)}),
    #                     (('Important dates'), {
    #                      'fields': ('last_login', 'date_joined')}),
    #                 )
    #                 return fieldsets
    #         else:
    #             return self.add_fieldsets
    #     else:
    #         if obj:
    #             if isinstance(obj, CustomUser):
    #                 return self.fieldsets
    #         else:
    #             return self.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
