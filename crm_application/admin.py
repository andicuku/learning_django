from django.contrib import admin

# Register your models here.
from crm_application.models import Agent, Lead, User

admin.site.register(Agent)
admin.site.register(Lead)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'is_staff')


admin.site.register(User, UserAdmin)
