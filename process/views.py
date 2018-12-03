from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

from process.models import FirstConfig
from project.models import Project
from .forms import FormFirstConfig, FormSecondConfig, FormThirdConfig

FORMS = [
    ("first", FormFirstConfig),
    ("second", FormSecondConfig),
    ("third", FormThirdConfig),
]

TEMPLATES = {
    "first": "process/first.html",
    "second": "process/second.html",
    "third": "process/third.html",
}


class ConfigWizard(SessionWizardView):
    form_list = [FormFirstConfig, FormSecondConfig, FormThirdConfig]
    initial_dict = {
        "first": {},
        "second": {},
    }

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict=None, **kwargs):
        print(self.initial_dict)
        first_form = form_dict.get('first', None)
        # second_form = form_dict.get('second', None)
        # third_form = form_dict.get('third', None)

        if first_form:
            first_form.instance.user = self.request.user
            first_form.instance.project_id = self.kwargs.get('project_id', None)
            if first_form.is_valid():
                first_form.save()
            else:
                print("First form is not valid")
                print(dir(first_form))

        return HttpResponseRedirect('/')


_config = ConfigWizard.as_view(FORMS)
