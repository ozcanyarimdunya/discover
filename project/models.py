from django.contrib.auth.models import User
from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-updated')


class Base(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class Type(Base):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Project(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    status = models.CharField(max_length=30, default="Not Started")
    is_done = models.BooleanField(default=False)
    started = models.DateTimeField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)

    @property
    def user_name(self):
        return self.user.username

    @property
    def type_name(self):
        return self.type.name

    def __str__(self):
        return self.name
