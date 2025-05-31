from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    title = models.CharField(max_length=255)  # Название рецепта
    description = models.TextField()  # Описание
    steps = models.TextField()  # Шаги приготовления
    cooking_time = models.PositiveIntegerField(help_text="Время в минутах")  # Время приготовления
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)  # Картинка
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор рецепта
    categories = models.ManyToManyField(Category, related_name="recipes")  # Категории
    
    def __str__(self):
        return self.title
