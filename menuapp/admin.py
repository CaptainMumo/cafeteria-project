from django.contrib import admin
from django.db import models
from django import forms

from .models import FoodCategory, MenuItem, DayMenu, TimeMenu


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(DayMenu)
class DayMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'day')
    search_fields = ('name','day')
    filter_horizontal = ('sub_menus',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_category', 'price')
    search_fields = ('name', 'food_category__name')


@admin.register(TimeMenu)
class TimeMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')
    search_fields = ('name',)    
    filter_horizontal = ('menu_items',)

