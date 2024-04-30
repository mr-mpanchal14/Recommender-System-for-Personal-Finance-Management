from django.contrib import admin
from .models import Info

# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'education', 'income', 'fees', 'predictions')


admin.site.register(Info, InfoAdmin)