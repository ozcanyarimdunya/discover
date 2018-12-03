from django import forms

from .models import Project


class FormProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'type')
