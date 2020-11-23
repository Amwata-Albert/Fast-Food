
from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User

admin.site.register(Profile)
admin.site.register(User,UserAdmin)