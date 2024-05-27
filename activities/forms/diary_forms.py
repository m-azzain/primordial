from dal import autocomplete
from django.forms import ModelForm

from activities.models import Diary


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'
        widgets = {
            'after_midnight': autocomplete
            .ModelSelect2Multiple(
                url='activities:activity_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity to autocomplete',
                    'data-minimum-input-length': 3,
                }),
            'morning': autocomplete
            .ModelSelect2Multiple(
                url='activities:activity_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity to autocomplete',
                    'data-minimum-input-length': 3,
                }),
            'during_day': autocomplete
            .ModelSelect2Multiple(
                url='activities:activity_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity to autocomplete',
                    'data-minimum-input-length': 3,
                }),
            'evening': autocomplete
            .ModelSelect2Multiple(
                url='activities:activity_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity to autocomplete',
                    'data-minimum-input-length': 3,
                }),
            'before_midnight': autocomplete
            .ModelSelect2Multiple(
                url='activities:activity_autocomplete',
                attrs={
                    'data-placeholder': 'Select an activity to autocomplete',
                    'data-minimum-input-length': 3,
                }),
        }