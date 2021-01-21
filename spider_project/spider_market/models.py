from django.db import models
from django.contrib.auth.models import AbstractUser



class Category(models.Model):
    title = models.CharField("Название", max_length=50)
    
    def __str__(self):
        return self.title

class Company(models.Model):
    # title = models.CharField("Название", max_length=50) # for future
    description = models.TextField("Описание компании", blank=True)
    is_active = models.BooleanField('Доступность компании', default=False, db_index=True)

class Product(models.Model):    
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание продукта", blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='category_items')
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, related_name='company_items')
    is_active = models.BooleanField('Доступность продукта', default=False, db_index=True)

    def __str__(self):
        return self.title
