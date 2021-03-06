import itertools

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass


for fs_name, fs_options in itertools.chain(UserAdmin.fieldsets, UserAdmin.add_fieldsets):
    fs_options['fields'] = [('email' if f == 'username' else f) for f in fs_options['fields'] if f != 'email']

for list_name in ('list_display', 'list_filter', 'search_fields', 'ordering'):
    lst = getattr(UserAdmin, list_name)
    lst = [f for f in lst if f != 'username']
    setattr(UserAdmin, list_name, lst)
