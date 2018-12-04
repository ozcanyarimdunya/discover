from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django import forms
from formtools.wizard.views import SessionWizardView

from .forms import FormNullData, FormAgeData, FormSkillSelection, FormSkillData, FormData
from .models import SkillDataConfig

STEP_NULL_DATA = "null_data"
STEP_AGE = "age"
STEP_SKILL_SELECTION = "skill_selection"
STEP_SKILL = "skill"

FORMS = [
    (STEP_NULL_DATA, FormNullData),
    (STEP_AGE, FormAgeData),
    (STEP_SKILL_SELECTION, FormSkillSelection),
    (STEP_SKILL, FormSkillData),
]

TEMPLATES = {
    STEP_NULL_DATA: "anytype/1_null_data.html",
    STEP_AGE: "anytype/2_age.html",
    STEP_SKILL_SELECTION: "anytype/3_skill_selection.html",
    STEP_SKILL: "anytype/4_skill.html",
}


class ConfigWizard(SessionWizardView):
    form_list = [FormNullData, FormAgeData, FormSkillData]

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_instance(self, step):
        form_class = self.form_list[step]
        model = form_class.Meta.model
        print('==== ', model, ' ====')
        try:
            instance = model.objects.get(project_id=self.kwargs.get('project_id'))
            self.instance_dict.update({step: instance})
            # return instance # can be used
        except (model.DoesNotExist, model.MultipleObjectsReturned):
            pass
        return super().get_form_instance(step)

    # def get_form_instance(self, step):
    #     form_class = self.form_list[step]
    #     if step == STEP_SKILL:
    #         try:
    #             instance = SkillDataConfig.objects.get(project_id=self.kwargs.get('project_id'))
    #             return instance
    #         except (SkillDataConfig.DoesNotExist, SkillDataConfig.MultipleObjectsReturned):
    #             return None
    #     return super().get_form_instance(step)

    def get_form(self, step=None, data=None, files=None):
        """
        Some modify require for this
        There are still some bugs
        :param step:
        :param data:
        :param files:
        :return:
        """
        if step == STEP_SKILL:
            form_class = self.form_list[step]

            extras = self._get_extras(form_class)

            kwargs = self.get_form_kwargs(step)
            kwargs.update({
                'data': data,
                'files': files,
                'prefix': self.get_form_prefix(step, form_class),
                'initial': self.get_form_initial(step),
                'extras': extras,
            })
            if issubclass(form_class, (forms.ModelForm, forms.models.BaseInlineFormSet)):
                # If the form is based on ModelForm or InlineFormSet,
                # add instance if available and not previously set.
                kwargs.setdefault('instance', self.get_form_instance(step))
            elif issubclass(form_class, forms.models.BaseModelFormSet):
                # If the form is based on ModelFormSet, add queryset if available
                # and not previous set.
                kwargs.setdefault('queryset', self.get_form_instance(step))

            return form_class(**kwargs)

        _super = super(ConfigWizard, self).get_form(step, data, files)
        return _super

    def _get_extras(self, form_class):
        _data = self.get_cleaned_data_for_step(STEP_SKILL_SELECTION)
        extra = []
        for key, value in _data.items():
            if value:
                if key not in extra:
                    extra.append(key)
                setattr(form_class, key, True)
            else:
                if key in extra:
                    extra.remove(key)
                setattr(form_class, key, False)
        return extra

    def done(self, form_list, form_dict=None, **kwargs):
        print(self.instance_dict)
        for form in form_list:
            form.instance.project_id = self.kwargs.get('project_id', None)
            if form.is_valid():
                form.save()
            else:
                print("Not valid: ", str(self.steps.current))

        return HttpResponseRedirect('/')


class _DataUploadView(FormView):
    template_name = ""
    form_class = FormData
    success_url = "/"

    def form_valid(self, form):
        form.instance.project_id = self.kwargs.get('project_id', None)
        return super().form_valid(form)


_config = ConfigWizard.as_view(FORMS)
