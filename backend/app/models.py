from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user

class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    def __str__(self):
        return self.username

class Role(models.Model):
    role = models.TextField()

class User(AppUser):
    birthday = models.DateField()
    startPrice = models.FloatField()
    startAmount = models.FloatField()
    progressDays = models.IntegerField()
    progressAmount = models.IntegerField()
    progressPrice = models.FloatField()
    role = models.ForeignKey(Role, default='user', on_delete=models.CASCADE)

class Admin(AppUser):
    name = models.TextField()
    role = models.ForeignKey(Role, default='admin', on_delete=models.CASCADE)

class Article(models.Model):
    articleId = models.AutoField(primary_key=True)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    text = models.TextField()

class Quote(models.Model):
    quoteId = models.AutoField(primary_key=True)
    text = models.TextField()
