from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            ValueError('Username required')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password):
        return self._create_user(username, password)

    def create_superuser(self, username, password):
        return self._create_user(
            username,
            password,
            is_staff=True,
            is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Логин', max_length=50, unique=True)
    email = models.EmailField('E-mail', max_length=100,)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField("Имя", max_length=20)
    last_name = models.CharField("Фамилия", max_length=50)
    phone = models.CharField('телефон', max_length=30)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title


class Company(models.Model):
    description = models.TextField("Описание компании", blank=True)
    is_active = models.BooleanField(
        'Доступность компании',
        default=False,
        db_index=True
    )


class Product(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание продукта", blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
        related_name='category_items'
    )
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.CASCADE,
        related_name='company_items'
    )
    is_active = models.BooleanField(
        'Доступность продукта',
        default=False,
        db_index=True
    )

    def __str__(self):
        return self.title
