from django.db import models
from django.utils import timezone

class FoodCategory(models.Model):
    """
    Food category: Protein, Starch, Dessert, Mixed dish, Special dish, Combo
    Attributes:
        name: name of the category
        image: image representative of a category, sets carousel background, defaults to blue background
    """
    name = models.CharField(max_length=50)
    # Optional image field
    image = models.ImageField(upload_to='food_category_images/', 
                              null=True, 
                              blank=True,
                              verbose_name="Optional Image (Representative of the category)",
                              help_text="This image will act as the background for the carousel for this category")
    # Optional flag video field
    special_flag_video = models.FileField(upload_to='food_category_videos/', 
                                          null=True, 
                                          blank=True,
                                          verbose_name="Optional Special Flag Video (Only for Specials)",
                                          help_text="This video will act as the background for the carousel for this special")
    # Optional flag image field
    special_flag_image = models.ImageField(upload_to='food_category_images/', 
                                           null=True, 
                                           blank=True,
                                           verbose_name="Optional Special Flag Image (Only for Specials)",
                                           help_text="This image will act as the background for the carousel for this special in the absence of the video")
    description = models.TextField(null=True, blank=True)    

    def __str__(self) -> str:
        return f"{self.name}"

class MenuItem(models.Model):
    """
    Represents a menu item
    Attributes:
        code: The unique menu item code used by the cafeteria
        name: The name of the item
        category: Protein, starch, fruit, vegetable etc        
        price: The cost of the item
        [description]: Optional brief description of the item
        [image]: Optional image of the item
    """
    # Ask what the code convention is
    code = models.CharField(max_length=10, unique=True, null=True, blank=True) 
    name = models.CharField(max_length=100, unique=True)
    food_category = models.ForeignKey(FoodCategory, models.SET_NULL, null=True, blank=True)     
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    # Optional
    description = models.TextField(null=True, blank=True)    

    # Optional image field
    image = models.ImageField(upload_to='menu_item_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.food_category}) @ {self.price}"

class TimeMenu(models.Model):
    """
    Menu for a particular time
    Breakfast, lunch, dinner etc
    Consists of many menu items
    """
    name = models.CharField(max_length=100, unique=True)
    start_time = models.TimeField(default=timezone.now().strftime('%H:%M:%S')) # Change to datetimefield
    end_time = models.TimeField(default=timezone.now().strftime('%H:%M:%S')) # Change to datetimefield
    menu_items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return f"{self.name} from {self.start_time} to {self.end_time}"

class DayMenu(models.Model):
    """
    Menu for a particular day
    Consists of breakfast, lunch, dinner submenus
    """

    name = models.CharField(max_length=50, default=timezone.datetime.today().strftime('%A'))
    day = models.DateField(default=timezone.now, unique=True)
    sub_menus = models.ManyToManyField(TimeMenu)

    def __str__(self):
        return f"{self.name}-{self.day}"








