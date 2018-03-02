from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from signup.models import Users
User=get_user_model()
class UserAdmin(admin.ModelAdmin):
    search_fields=['email']
    class meta:
        model=User


admin.site.register(Users,UserAdmin)
