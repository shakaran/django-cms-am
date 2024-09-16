from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'customer_id', 'created_by', 'modified_by', 'created_at', 'updated_at')
    search_fields = ('name', 'surname', 'customer_id')
