from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
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
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    customized User
    """
    email = models.EmailField(
        verbose_name=_('email id'),
        max_length=64,
        unique=True,
        help_text='EMAIL ID.'
    )
    username = models.CharField(
        max_length=30,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email

# class UserManager(BaseUserManager):
#     def _create_user(self, email, username, password, address, **extra_fields):
#         if not email :
#             raise ValueError('The given email mist be set')
#         print(email)
#         print(address)
#         email = self.normalize_email(email)
#         username = self.model.normalize_username(username)
#         address = self.model.normalize_address(address)
#         user = self.model(email = email, username = username, address = address, **extra_fields)
#         user.set_password(password)
#         user.save (using = self._db)
#         return user

#     def create_user(self, address, username = '', password = None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(address, username, password, **extra_fields)
    
#     def create_superuser(self, password, address, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff = True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser = True')

#         return self._create_user(address, username, password, **extra_fields)


# class User(AbstractUser):
#     # nickname = models.CharField(max_length=50)
#     '''
#     username(email)과 비번만으로도 가입가능 
#     '''
#     phone_number = models.CharField(blank=True, max_length=50)
#     address = models.CharField(blank=True, max_length=300)
#     items_of_interest = models.CharField(blank=True, max_length=300)
#     job = models.CharField(blank=True, max_length=50)
#     first_name = None
#     last_name = None
#     email = None
#     # USERNAME_FIELD = ''
#     REQUIRED_FIELDS = []
#     objects = UserManager()




    # first_name = None
    # last_name = None
    # # username = None
    # name = models.CharField('이름', blank=True, max_length=50)
    # address = models.CharField('주소', blank=True, max_length=200)
    # phone_number = models.CharField('휴대폰번호', blank=True, max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # # bio = models.TextField(max_length=500, blank=True)
    # # location = models.CharField(max_length=30, blank=True)
    # # birth_date = models.DateField(null=True, blank=True)
