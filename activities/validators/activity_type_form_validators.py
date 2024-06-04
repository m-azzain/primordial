from django.core.exceptions import ValidationError

from activities.models import ActivityType

NIGHT_PRAYER_SURAHS_M2M_FIELD = 'night_prayer_surahs'
QURAN_SURAHS_M2M_FIELD = 'quran_surahs'
RECEIVED_PERSON_M2M_FIELD = 'received_persons'
VISITED_PERSON_M2M_FIELD = 'visited_persons'
VISITED_PLACE_M2M_FIELD = 'visited_places'

DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE = 'There is a duplicated ActivityType with id: %(id)d'


def validate_activity_type_form(activity_form, cleaned_data):
    _validate_activity_type_night_prayer_form(activity_form, cleaned_data)
    _validate_activity_type_reciting_quran_form(activity_form, cleaned_data)
    _validate_activity_type_receiving_person_form(activity_form, cleaned_data)
    _validate_activity_type_visiting_person_form(activity_form, cleaned_data)
    _validate_activity_type_visiting_place_form(activity_form, cleaned_data)


def _validate_activity_type_night_prayer_form(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If the type is not NIGHT_PRAYER make sure the field night_prayer_surahs is empty and return
    if type_ != ActivityType.TypeChoices.NIGHT_PRAYER.value:
        if len(set(cleaned_data[NIGHT_PRAYER_SURAHS_M2M_FIELD])) != 0:
            msg = F'Night prayer surahs are not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(NIGHT_PRAYER_SURAHS_M2M_FIELD, msg)
            raise ValidationError(msg)
        return cleaned_data

    surah_ids = set(cleaned_data[NIGHT_PRAYER_SURAHS_M2M_FIELD].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(night_prayer_surahs__id__in=surah_ids).
                                distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        surah_ids_2 = set(activity_type.night_prayer_surahs.all().order_by('id').values_list('id', flat=True))
        if surah_ids_2 == surah_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(NIGHT_PRAYER_SURAHS_M2M_FIELD, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data


def _validate_activity_type_reciting_quran_form(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If the type is not RECITING_QURAN make sure the field quran_surahs is empty and return
    if type_ != ActivityType.TypeChoices.RECITING_QURAN.value:
        if len(set(cleaned_data[QURAN_SURAHS_M2M_FIELD])) != 0:
            msg = F'Quran surahs are not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(QURAN_SURAHS_M2M_FIELD, msg)
            raise ValidationError(msg)
        return cleaned_data

    surah_ids = set(cleaned_data[QURAN_SURAHS_M2M_FIELD].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(quran_surahs__id__in=surah_ids).
                                distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        surah_ids_2 = set(activity_type.quran_surahs.all().order_by('id').values_list('id', flat=True))
        if surah_ids_2 == surah_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(QURAN_SURAHS_M2M_FIELD, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data


def _validate_activity_type_receiving_person_form(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If the type is not RECEIVING_PERSON make sure the field received_persons is empty and return
    if type_ != ActivityType.TypeChoices.RECEIVING_PERSON.value:
        if len(set(cleaned_data[RECEIVED_PERSON_M2M_FIELD])) != 0:
            msg = F'Received persons are not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(RECEIVED_PERSON_M2M_FIELD, msg)
            raise ValidationError(msg)
        return cleaned_data

    person_ids = set(cleaned_data[RECEIVED_PERSON_M2M_FIELD].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(received_persons__id__in=person_ids).distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        person_ids_2 = set(activity_type.received_persons.all().order_by('id').values_list('id', flat=True))
        if person_ids_2 == person_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(RECEIVED_PERSON_M2M_FIELD, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data


def _validate_activity_type_visiting_person_form(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If the type is not VISITING_PERSON make sure the field visited_persons is empty and return
    if type_ != ActivityType.TypeChoices.VISITING_PERSON.value:
        if len(set(cleaned_data[VISITED_PERSON_M2M_FIELD])) != 0:
            msg = F'Visited persons are not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(VISITED_PERSON_M2M_FIELD, msg)
            raise ValidationError(msg)
        return cleaned_data

    person_ids = set(cleaned_data[VISITED_PERSON_M2M_FIELD].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(visited_persons__id__in=person_ids).distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        person_ids_2 = set(activity_type.visited_persons.all().order_by('id').values_list('id', flat=True))
        if person_ids_2 == person_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(VISITED_PERSON_M2M_FIELD, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data


def _validate_activity_type_visiting_place_form(activity_form, cleaned_data):
    type_ = cleaned_data.get('type')
    # If the type is not VISITING_PLACE make sure the field visited_places is empty and return
    if type_ != ActivityType.TypeChoices.VISITING_PLACE.value:
        if len(set(cleaned_data[VISITED_PLACE_M2M_FIELD])) != 0:
            msg = F'Visited places are not allowed with activity type %(type)s)' % {'type': type_}
            activity_form.add_error(VISITED_PLACE_M2M_FIELD, msg)
            raise ValidationError(msg)
        return cleaned_data

    places_ids = set(cleaned_data[VISITED_PLACE_M2M_FIELD].order_by('id').values_list('id', flat=True))
    other_activity_type_list = (ActivityType.objects.filter(visited_places__id__in=places_ids).distinct())
    # The order only important if we are comparing list for equality, but sets == operator does not need the order
    for activity_type in other_activity_type_list:
        places_ids_2 = set(activity_type.visited_places.all().order_by('id').values_list('id', flat=True))
        if places_ids_2 == places_ids:
            msg = DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': activity_type.id}
            activity_form.add_error(VISITED_PLACE_M2M_FIELD, msg)
            raise ValidationError(DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE,
                                  params={'id': activity_type.id})
    return cleaned_data