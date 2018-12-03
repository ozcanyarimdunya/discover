from django import forms

from .models import (FirstConfig, SecondConfig, ThirdConfig, FourthConfig)


class FormFirstConfig(forms.ModelForm):
    attr_1 = forms.CharField(required=False, label="First Attribute")
    attr_2 = forms.CharField(required=False, label="Second Attribute")

    class Meta:
        model = FirstConfig
        fields = ('name', 'attr_1', 'attr_2')

    def save(self, commit=True):
        instance = super().save(commit=False)

        attr_1 = self.cleaned_data['attr_1']
        attr_2 = self.cleaned_data['attr_2']

        config = {
            "attr_1": attr_1,
            "attr_2": attr_2,
        }
        instance.config = config

        if commit:
            instance.save()

        return instance


class FormSecondConfig(forms.ModelForm):
    attr_1 = forms.CharField(required=False, label="First Attribute")
    attr_2 = forms.CharField(required=False, label="Second Attribute")

    class Meta:
        model = SecondConfig
        fields = ('name', 'attr_1', 'attr_2')

    def save(self, commit=True):
        print("I am in here")
        return super().save(commit=True)


class FormThirdConfig(forms.ModelForm):
    attr_1 = forms.CharField(required=False, label="First Attribute")
    attr_2 = forms.CharField(required=False, label="Second Attribute")

    class Meta:
        model = ThirdConfig
        fields = ('name', 'attr_1', 'attr_2')

    def save(self, commit=True):
        print("I am in here")
        return super().save(commit=True)
