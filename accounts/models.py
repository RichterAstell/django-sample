from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class MemberManager(BaseUserManager):
    pass
    # def create_user(self, member_id, password=None):
    #     pass
    # def create_superuser(self, member_id, password=None):
    #     pass

class Member(AbstractBaseUser):
    member_id = models.CharField(primary_key=True, max_length=8, null=False, unique=True)
    password = models.CharField(max_length=1024, null=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'member_id'
    objects = MemberManager()
