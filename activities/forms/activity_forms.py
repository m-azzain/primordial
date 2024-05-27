from dal import autocomplete
from django.forms import ModelForm

from activities.models import Activity, ActivityType


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