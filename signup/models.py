from django.db import models
import uuid
import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
from django.contrib.auth.validators import validators
class customUserManager(BaseUserManager):
    def create_user(self,username,email,password,is_staff,is_superuser,is_active):
        if not email:
            raise ValueError("The given Email must be set")
        email=self.normalize_email(email)
        user_obj=self.model(
            email=email,
            username=username
            )
        user_obj.set_password(password)
        user_obj.active=is_active
        user_obj.staff=is_staff
        user_obj.admin=is_superuser
        user_obj.save(using=self._db)
        return(user_obj)
    def create_staffuser(self,username,email,password=None):
        return self.create_user(username,email,password,True,True,True)
    
    def create_superuser(self,username,email,password=None):
        return self.create_user(username,email,password,True,True,True)

class Users(AbstractUser):
    username=models.CharField(max_length=150,unique=True,validators=[validators.validate_slug])
    user_id=models.UUIDField(primary_key=True,default=uuid.uuid1,unique=True)
    email=models.EmailField(unique=True,validators=[validators.validate_email])
    #user_password=models.CharField(max_length=100,unique=False,validators=[validators.validate_slug])
    staff=models.BooleanField(default=False)
    active=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=customUserManager()

    def __str__(self):
        return '{}'.format(str(self.username))
    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
    @property
    def is_superuser(self):
        return self.admin