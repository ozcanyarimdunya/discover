"""
Data Columns

NAME    : Player name
AGE	    : Player age
GK	    : Goalkeeper skill
LB	    : Left Back skill
RB	    : Right Back skill
DF	    : Defence skill
MD	    : Middle skill
LP	    : Left Wing skill
RP      : Right Wing skill
ST      : Striker skill
"""

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from project.models import Project


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-updated')


class Base(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class NullDataConfig(Base):
    config = JSONField()


class AgeDataConfig(Base):
    min_age = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)


class SkillSelection(Base):
    selection = JSONField(null=True, blank=True)


class SkillDataConfig(Base):
    config = JSONField(null=True, blank=True)


class Data(Base):
    file = models.FileField(upload_to="uploads/")


class Anytype(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
