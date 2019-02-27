from uuid import uuid4
import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.skill.models import Skill
from apps.sector.models import Sector


class UserManager(BaseUserManager):
    def _create_user(
            self,
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          last_login=timezone.now(),
                          registered_at=timezone.now(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        max_length=255)
    first_name = models.CharField(
        verbose_name='First name',
        max_length=30,
        default='first')
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=30,
        default='last')
    avatar = models.ImageField(verbose_name='Avatar', blank=True)
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Work sector')
    skills = models.ManyToManyField(Skill, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nationality = models.CharField(
        verbose_name='Nationality',
        max_length=255,
        blank=True,
        null=True)
    age =  models.PositiveSmallIntegerField(
        verbose_name='Age',
        blank=True,
        null=True)
    started = models.DateField(
        verbose_name='Started at',
        default=datetime.date.today)
    ended = models.DateField(
        verbose_name='Ended at',
        blank=True,
        null=True)
    is_employee = models.BooleanField(verbose_name='Employee', default=True)
    address = models.CharField(
        verbose_name='Address',
        max_length=511,
        blank=True,
        null=True)
    phone_regex = RegexValidator(
        regex=r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
        message="Phone number must be entered in the format: '+999999999'. Up to 17 digits allowed.")
    phone_number = models.CharField(
        verbose_name='phone number',
        validators=[phone_regex],
        max_length=255,
        blank=True,
        null=True)
    token = models.UUIDField(
        verbose_name='Token',
        default=uuid4,
        editable=False)
    is_archived = models.BooleanField(verbose_name='Archived', default=False)

    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    registered_at = models.DateTimeField(
        verbose_name='Registered at',
        auto_now_add=timezone.now)

    # Fields settings
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    full_name.fget.short_description = 'Full name'

    @property
    def days_in_company(self):
        if self.is_employee:
            delta = datetime.date.today() - self.started
        elif self.ended:
            delta = self.ended - self.started
        else:
            delta = datetime.date.today() - self.started
        return f'{delta.days}'
    days_in_company.fget.short_description = 'Days in company'
    

    def get_days_in_company(self):
        return self.days_in_company

    @property
    def short_name(self):
        return f'{self.last_name} {self.first_name[0]}.'
    short_name.fget.short_description = 'Short name'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=User)
def update_stock(sender, instance, **kwargs):
    if not instance:
            return

    if hasattr(instance, '_dirty'):
        return
    if instance.ended <= datetime.date.today():
        instance.is_employee = False
    elif instance.ended == None:
        instance.is_employee = True
    else:
        instance.is_employee = True
    try:
        instance._dirty = True
        instance.save()
    finally:
        del instance._dirty

