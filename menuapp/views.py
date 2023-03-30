from datetime import date, datetime
from django.db.models import Q
from django.utils import timezone

from django.shortcuts import render
from .models import DayMenu, TimeMenu, MenuItem, FoodCategory


def index(request):
    """ Get the days menu """
    todays_menu = current_menus = menu_items = current_menu_label = current_menu_end_time = None
    # Get the current date
    today = date.today()
    # Retrieve the corresponding menu
    todays_menu = DayMenu.objects.filter(day=today).first()

    # Get the submenu based on current time
    current_time = datetime.now()
    if todays_menu is not None:
        current_menus = todays_menu.sub_menus.all().filter(start_time__lte=current_time).filter(end_time__gt=current_time).order_by('end_time')
        

    # Get the menu items
    if current_menus is not None:
        for current_menu in current_menus:
            if menu_items is None:
                menu_items = current_menu.menu_items.all()
            else:
                menu_items = menu_items.union(current_menu.menu_items.all(), all=False)
            if current_menu_end_time is not None:
                if current_menu.end_time < current_menu_end_time:
                    current_menu_end_time = current_menu.end_time
            else:
                current_menu_end_time = current_menu.end_time
    
    all_day_menu = TimeMenu.objects.filter(name="All Day Menu").first()
    all_day_menu_items = None

    if all_day_menu is not None:
        all_day_menu_items = all_day_menu.menu_items.all()

    if all_day_menu_items is not None:
        if menu_items is not None:
            menu_items = menu_items.union(all_day_menu_items, all=False)
        else:
            menu_items = all_day_menu_items

    # Group them by their categories in a dictionary of lists
    items_by_category = {}
    if menu_items is not None:
        for item in menu_items:
            if item.food_category in items_by_category:
                if len(items_by_category[item.food_category]) < 9: 
                    items_by_category[item.food_category].append(item)
                else:
                    key = item.food_category.name
                    if key in items_by_category:
                        items_by_category[key].append(item)
                    else:
                        items_by_category[key] = [item]
            else:
                items_by_category[item.food_category] = [item]
    

    
    """
    split_cats = {}
    for key in items_by_category:
        c = 0
        if len(items_by_category[key]) > 10:
            newkey = key.name
            split_cats[newkey] = items_by_category[key][10:]
            items_by_category[key] = items_by_category[key][:10]
            c = c + 1

    items_by_category.update(split_cats)
    """ 
    # Add the menu and submenus to the context
    context = {
        'title': "Cafeteria Menu App"
    }
    print(current_menu_end_time)
    if current_menu_label:
        context['menulabel'] = current_menu_label

    if current_menu_end_time:
        context['current_menu_end_time'] = current_menu_end_time.strftime("%H:%M:%S")

    if len(items_by_category) > 0:
        context['menuitems'] = items_by_category   

    return render(request=request, 
                template_name="menuapp/index.html", 
                context=context)

