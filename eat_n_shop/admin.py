from django.contrib import admin
from .models import Grocery

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'nowHave', 'eaten', 'unitMeasure', 'min', 'purchased','imageURL')

# Register your models here.
admin.site.register(Grocery, GroceryAdmin)
