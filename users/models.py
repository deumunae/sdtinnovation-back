from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Please, type username')

        user = self.model(
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields
        )

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=True required for Superuser')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=True required for Superuser')

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=256,
        verbose_name='Почта',
        unique=True,
    )
    # Дата создания
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        null=True,
    )
    # Дата редактирования
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования',
        null=True,
    )
    # Django Additional (не трогать)
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Сотрудник организации',
        help_text='Открывает доступ к панели администратора с указанными правами',
    )  # права к админ-панели
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный аккаунт',
        help_text='Статус (по умолчанию "Да")',
    )  # активный аккаунт

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Пользователь системы'
        verbose_name_plural = 'Пользователи системы'

    def __str__(self):
        return self.username