from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    steps = models.TextField() 
    cooking_time = models.PositiveIntegerField(help_text="Время в минутах") 
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    categories = models.ManyToManyField(Category, related_name="recipes")  
    
    def __str__(self):
        return self.title
