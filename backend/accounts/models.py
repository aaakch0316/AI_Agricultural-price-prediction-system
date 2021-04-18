from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        try:
            user = self.model(
                user_type=User.USER_TYPE_CHOICES[0],
                username=username,
                email=email,
            )
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            user.set_password(password)
            user.is_active = True
            user.save()
            return user
        except Exception as e:
            print(e)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        try:
            superuser = self.create_user(
                user_type=User.USER_TYPE_CHOICES[0],
                username=username,
                password=password,
                email=email,
            )
            superuser.is_admin = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.is_staff = True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)





class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ('django', 'Django'),
        ('facebook', 'Facebook'),
        ('gmail', 'Gmail')
    )

    user_type = models.CharField(
        max_length=20,
        choices = USER_TYPE_CHOICES,
        default = USER_TYPE_CHOICES[0]
    )

    email = models.EmailField(max_length=100, null=False)
    username = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=12)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()








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
