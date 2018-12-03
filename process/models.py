from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from project.models import Project


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-updated')


class Base(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class FirstConfig(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="First Configuration")
    is_default = models.BooleanField(default=False)
    config = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class SecondConfig(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Second Configuration")
    is_default = models.BooleanField(default=False)
    config = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class ThirdConfig(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Third Configuration")
    is_default = models.BooleanField(default=False)
    config = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class FourthConfig(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Fourth Configuration")
    file_one = models.FileField(upload_to='uploads/')
    file_two = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
