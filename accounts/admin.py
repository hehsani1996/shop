from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'username')

##########################################
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm
# from .models import CustomUser

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = CustomUser

# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     fieldsets = UserAdmin.fieldsets + (
#     (None, {'fields': ('biography',)}),
#  )

# admin.site.register(CustomUser, CustomUserAdmin)
