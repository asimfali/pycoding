from django.contrib import admin

from .models import *
from django import forms


class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass


class SmartphoneCategoryChoiceField(forms.ModelChoiceField):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='notebooks'))


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return SmartphoneCategoryChoiceField(Category.objects.filter(slug='smartphones'))


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
