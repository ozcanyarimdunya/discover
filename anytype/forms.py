from django import forms

from .models import (NullDataConfig, AgeDataConfig, SkillSelection, SkillDataConfig, Data)


class FormNullData(forms.ModelForm):
    DELETE = 'DELETE'
    FILL = 'FILL'
    NULL_CHOICES = (
        (DELETE, 'Delete Null Data'),
        (FILL, 'Fill Null Data with 0'),
    )
    selection = forms.ChoiceField(choices=NULL_CHOICES, label="Select method")  # , widget=forms.RadioSelect)

    class Meta:
        model = NullDataConfig
        fields = ('selection',)

    def save(self, commit=True):
        instance = super().save(commit=False)

        selection = self.cleaned_data['selection']

        config = {
            "delete": selection == self.DELETE,
            "attr_2": selection == self.FILL,
        }
        instance.config = config

        if commit:
            instance.save()

        return instance


class FormAgeData(forms.ModelForm):
    _min = forms.IntegerField(min_value=1, max_value=10, label="Min Age", required=False)
    _max = forms.IntegerField(min_value=1, max_value=10, label="Max Age", required=False)

    class Meta:
        model = AgeDataConfig
        fields = ('_min', '_max')

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.min_age = self.cleaned_data['_min']
        instance.max_age = self.cleaned_data['_max']

        if commit:
            instance.save()

        return instance


class FormSkillSelection(forms.ModelForm):
    skill_1 = forms.CharField(required=True, label="1. Skill")
    skill_2 = forms.CharField(required=False, label="2. Skill")
    skill_3 = forms.CharField(required=False, label="3. Skill")
    skill_4 = forms.CharField(required=False, label="4. Skill")
    skill_5 = forms.CharField(required=False, label="5. Skill")

    class Meta:
        model = SkillSelection
        fields = ('skill_1', 'skill_2', 'skill_3', 'skill_4', 'skill_5')

    def save(self, commit=True):
        return super(FormSkillSelection, self).save(commit=False)


class FormSkillData(forms.ModelForm):
    skill_1_A = forms.CharField(label="1. Skill A")
    skill_1_B = forms.CharField(label="1. Skill B")
    skill_1_C = forms.CharField(label="1. Skill C")

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extras', [])
        super().__init__(*args, **kwargs)

        for field in extra_fields:
            self.fields[f"{field}_A"] = forms.CharField()
            self.fields[f"{field}_B"] = forms.CharField()
            self.fields[f"{field}_C"] = forms.CharField()

    class Meta:
        model = SkillDataConfig
        fields = ('skill_1_A', 'skill_1_B', 'skill_1_C')

    def save(self, commit=True):
        instance = super().save(commit=False)

        config = {
            'skill_1': {
                "skill_1_A": self.cleaned_data["skill_1_A"],
                "skill_1_B": self.cleaned_data["skill_1_B"],
                "skill_1_C": self.cleaned_data["skill_1_C"],
            }
        }

        if self.skill_2:
            config['skill_2'] = {
                "skill_2_A": self.cleaned_data["skill_2_A"],
                "skill_2_B": self.cleaned_data["skill_2_B"],
                "skill_2_C": self.cleaned_data["skill_2_C"],
            }
        if self.skill_3:
            config['skill_3'] = {
                "skill_3_A": self.cleaned_data["skill_3_A"],
                "skill_3_B": self.cleaned_data["skill_3_B"],
                "skill_3_C": self.cleaned_data["skill_3_C"],
            }
        if self.skill_4:
            config['skill_4'] = {
                "skill_4_A": self.cleaned_data["skill_4_A"],
                "skill_4_B": self.cleaned_data["skill_4_B"],
                "skill_4_C": self.cleaned_data["skill_4_C"],
            }
        if self.skill_5:
            config['skill_5'] = {
                "skill_5_A": self.cleaned_data["skill_5_A"],
                "skill_5_B": self.cleaned_data["skill_5_B"],
                "skill_5_C": self.cleaned_data["skill_5_C"],
            }

        instance.config = config

        if commit:
            instance.save()

        return instance


class FormData(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('file',)
