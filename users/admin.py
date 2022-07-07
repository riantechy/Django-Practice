from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete: False
#     verbose_name_plural = 'Profile'
#     fk_name: 'User'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

# def get_inline_instance(self, request, obj=None):
#     if not obj:
#         return list()
#     return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
admin.site.register(Profile)
# admin.site.register(User, CustomUserAdmin)


