from dal import autocomplete
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from activities.models import Activity, ActivityType


class ActivityTyeForm(ModelForm):
    class Meta:
        model = ActivityType
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ActivityTyeForm, self).clean()
        night_prayer_surah_ids = set(cleaned_data['night_prayer_surahs'].order_by('id').
                                     values_list('id', flat=True))
        other_activity_type_list = (ActivityType.objects.filter(night_prayer_surahs__id__in=night_prayer_surah_ids).
                                    # exclude(pk=form.instance.pk).
                                    distinct())
        print(other_activity_type_list.query)
        # The order only important if we are comparing list for equality, but sets == operator does not need the order
        for activity_type in other_activity_type_list:
            night_prayer_surah_ids_2 = set(activity_type.night_prayer_surahs.all().order_by('id').
                                           values_list('id', flat=True))
            if night_prayer_surah_ids_2 == night_prayer_surah_ids:
                ids_str = ', '.join([str(i) for i in night_prayer_surah_ids_2])
                msg = F'We have duplicated ActivityType: ({ids_str})'
                self.add_error("night_prayer_surahs", msg)
                raise ValidationError(
                    'We have duplicated ActivityType with surahs: (%(surah_ids)s)',
                    code='duplicated_activity_type',
                    params={'surah_ids': ids_str}
                )
        return cleaned_data


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
