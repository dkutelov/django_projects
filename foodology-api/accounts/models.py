from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )

    # copied from AbstractUser
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into '
            'this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be '
            'treated as active. Unselect this instead '
            'of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now,
    )

    # Add field

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo_url = models.URLField(max_length=200, default="https://res.cloudinary.com/dariku/image/upload/v1607681887/events/user-photos/user-default.jpg")
    
    phone = models.CharField(max_length=12, blank=False, validators=[
        RegexValidator(regex=r'^\+?0?\d{8,9}$', 
                        message="Phone number must be entered in the format: '+999999999'. Up to 9 digits allowed.")])

    def __str__(self):
        return f'{self.user.email}'


class DefaultDeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=False, default='Sofia')
    post_code = models.CharField(max_length=4, validators=[
        RegexValidator(regex=r'^\d{4}$', 
                        message="Post code should be 4 digits")])
    city_area = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=False)
    street_number = models.CharField(max_length=100, blank=False)
    app_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.city} - {self.street} {self.street_number}'

