from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Persons, Genders, Document_types, Resources,  Resources_roles, Roles, User_roles


from django.contrib.auth.models import Group  


admin.site.register(Persons)
admin.site.register(Genders)
admin.site.register(Document_types)
admin.site.register(Resources)
admin.site.register(Resources_roles)
admin.site.register(Roles)
#admin.site.register(User);
admin.site.register(User_roles)

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

admin.site.unregister(Group)  


