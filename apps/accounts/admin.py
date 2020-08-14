from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.conf import settings

from .models import Profile, Order


# admin.site.register(Account)

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Datos del cliente'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine, )

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(User, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)