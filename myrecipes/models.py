# recipes/models.py
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    # Добавьте другие поля по вашему выбору

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()  # Время приготовления в минутах
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='RecipeCategory')  # Связь с категориями

    # Добавьте другие поля по вашему выбору

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Добавьте другие поля по вашему выбору

    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"
