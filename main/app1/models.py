import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.name


class Department(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'department'

    def __str__(self):
        return self.name


class Role(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'

    def __str__(self):
        return self.name


class Status(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self):
        return self.name


class Task(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='id_category')
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'task'

    def __str__(self):
        return self.description


class UserProject(models.Model):
    # id_django = models.OneToOneField(User, models.CASCADE, db_column='id_django')
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='id_role')
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department')
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'UserProject'

    def __str__(self):
        return self.full_name
