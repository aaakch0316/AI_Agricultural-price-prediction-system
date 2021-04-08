from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, address, **extra_fields):
        if not email :
            raise ValueError('The given email mist be set')
        print(email)
        print(address)
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        address = self.model.normalize_address(address)
        user = self.model(email = email, username = username, address = address, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user

    def create_user(self, address, username = '', password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(address, username, password, **extra_fields)
    
    def create_superuser(self, password, address, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(address, username, password, **extra_fields)


class User(AbstractUser):
    # nickname = models.CharField(max_length=50)
    '''
    username(email)과 비번만으로도 가입가능 
    '''
    phone_number = models.CharField(blank=True, max_length=50)
    address = models.CharField(blank=True, max_length=300)
    items_of_interest = models.CharField(blank=True, max_length=300)
    job = models.CharField(blank=True, max_length=50)
    first_name = None
    last_name = None
    email = None
    # USERNAME_FIELD = ''
    REQUIRED_FIELDS = []
    objects = UserManager()




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
