from django.core.exceptions import ValidationError

from activities.models import ActivityType

NIGHT_PRAYER_SURAHS = 'night_prayer_surahs'

DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE = 'There is a duplicated ActivityType with id: %(id)d'


def validate_activity_type_form(activity_form, cleaned_data):
    _validate_activity_type_form_night_prayer(activity_form, cleaned_data)


def _validate_activity_type_form_night_prayer(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If type not NIGHT_PRAYER make sure the field night_prayer_surahs is empty and return
    if type_ != ActivityType.TypeChoices.NIGHT_PRAYER.value:
        if len(set(cleaned_data[NIGHT_PRAYER_SURAHS])) != 0:
            msg = F'Night prayer surahs not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(NIGHT_PRAYER_SURAHS, msg)
            raise ValidationError(msg)
        return cleaned_data

    surah_ids = set(cleaned_data[NIGHT_PRAYER_SURAHS].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(night_prayer_surahs__id__in=surah_ids).
                                distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        surah_ids_2 = set(activity_type.night_prayer_surahs.all().order_by('id').values_list('id', flat=True))
        if surah_ids_2 == surah_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(NIGHT_PRAYER_SURAHS, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data
