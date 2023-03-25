from django.contrib import admin

from .models import FoodCategory, MenuItem, DayMenu, TimeMenu

admin.site.register(FoodCategory)
admin.site.register(MenuItem)
admin.site.register(DayMenu)
admin.site.register(TimeMenu)
