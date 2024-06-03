from dal import autocomplete
from django.forms import ModelForm

from activities.models import Activity, ActivityType
from activities.validators import validate_activity_type_form


class ActivityTyeForm(ModelForm):

    class Meta:
        model = ActivityType
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ActivityTyeForm, self).clean()
        return validate_activity_type_form(self, cleaned_data)


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'activity_type': autocomplete
            .ModelSelect2(
                url='activities:activity_type_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity type to autocomplete',
                    'data-minimum-input-length': 3,
                }),
        }
