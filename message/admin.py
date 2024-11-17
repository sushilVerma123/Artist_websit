from django.contrib import admin
from .models.contact import Contact
from .models.profile import Profile

# Register your models here.


class AdminContact(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'user_messages', 'datetime']


class AdminProfile(admin.ModelAdmin):
    list_display = ['full_name', 'description', 'gender', 'mobile', 'address', 'image', 'instagram', 'twitter',
                    'facebook',
                    'linkedin', 'customer']


admin.site.register(Contact, AdminContact)
admin.site.register(Profile, AdminProfile)
