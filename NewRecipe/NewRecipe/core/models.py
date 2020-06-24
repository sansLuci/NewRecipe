from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	"""Manager class which helps in creating a user or superuser"""
	def create_user(self, email, password=None, **extra_fields):
		'''Create and save a new user'''
		if not email:
			raise ValueError('Provide email address')

		user = self.model(email=self.normalize_email(email), **extra_fields) 
		'''Function 'normalize-email()' comes with BaseUserManager class'''
		user.set_password(password)
		user.save(using=self._db)
		
		return user

	def create_superuser(self, email, password):
		'''Create and save a new superuser'''
		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		
		return user


class User(AbstractBaseUser, PermissionsMixin):
	"""Custom user model that supports using email instead of username"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email' # default email