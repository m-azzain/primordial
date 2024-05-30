import datetime

from dal import autocomplete
from django.db.models import Q
from django.utils import timezone

from ..models import Activity, ActivityType


def get_activity_type_query(word):
    q_builder = Q()
    # q_sequence = word.strip().lower().split('+')
    q_sequence = word.strip().split('+')
    q = q_sequence[0]
    if q in 'night_prayer':
        if len(q_sequence) > 1:
            for q_surah in q_sequence[1:]:
                q_builder = q_builder | (Q(type=ActivityType.TypeChoices.NIGHT_PRAYER.value) &
                           Q(night_prayer_surahs__name_en__contains=q_surah))
        else:
            q_builder = q_builder | Q(type=ActivityType.TypeChoices.NIGHT_PRAYER.value)
    if q in 'reciting_quran':
        if len(q_sequence) > 1:
            for q_surah in q_sequence[1:]:
                q_builder = q_builder | (Q(type=ActivityType.TypeChoices.RECITING_QURAN.value) &
                           Q(quran_surahs__name_en__contains=q_surah))
        else:
            q_builder = q_builder | Q(type=ActivityType.TypeChoices.RECITING_QURAN.value)
    if q in 'practicing_programming':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.PRACTICING_PROGRAMMING.value)
    if q in 'reading_book':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.READING_BOOK.value)
    if q in 'visiting_person':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.VISITING_PERSON.value)
    if q in 'receiving_person':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.RECEIVING_PERSON.value)
    if q in 'visiting_place':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.VISITING_PLACE.value)
    if q in 'changing_residence':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.CHANGING_RESIDENCE.value)
    if q in 'purchasing':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.PURCHASING.value)
    if q in 'reviewing_lecture':
        if len(q_sequence) > 1:
            for q_lecture in q_sequence[1:]:
                q_builder = q_builder | (Q(type=ActivityType.TypeChoices.REVIEWING_LECTURE.value) &
                           Q(lecture__name_en__contains=q_lecture))
        else:
            q_builder = q_builder | Q(type=ActivityType.TypeChoices.REVIEWING_LECTURE.value)
    if q in 'reviewing_general_topic':
        if len(q_sequence) > 1:
            for q_topic in q_sequence[1:]:
                q_builder = q_builder | (Q(type=ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC.value) &
                           Q(general_topic__title__contains=q_topic))
        else:
            q_builder = q_builder | Q(type=ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC.value)
    if q in 'sleeping':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.SLEEPING.value)
    if q in 'relaxing':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.RELAXING.value)
    if q in 'cleaning_clothes':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.CLEANING_CLOTHS.value)
    if q in 'cleaning_home':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.CLEANING_HOME.value)
    if q in 'visiting_doctor':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.VISITING_DOCTOR.value)
    if q in 'preparing_food':
        q_builder = q_builder | Q(type=ActivityType.TypeChoices.PREPARING_FOOD.value)
    return q_builder


def get_activity_type_query_for_activity(word):
    q_builder = Q()
    # q_sequence = word.strip().lower().split('+')
    q_sequence = word.strip().split('+')
    q = q_sequence[0]
    if q in 'night_prayer':
        if len(q_sequence) > 1:
            for q_surah in q_sequence[1:]:
                q_builder = q_builder | (Q(activity_type__type=ActivityType.TypeChoices.NIGHT_PRAYER.value) &
                           Q(activity_type__night_prayer_surahs__name_en__contains=q_surah))
        else:
            q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.NIGHT_PRAYER.value)
    if q in 'reciting_quran':
        if len(q_sequence) > 1:
            for q_surah in q_sequence[1:]:
                q_builder = q_builder | (Q(activity_type__type=ActivityType.TypeChoices.RECITING_QURAN.value) &
                           Q(activity_type__quran_surahs__name_en__contains=q_surah))
        else:
            q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.RECITING_QURAN.value)
    if q in 'practicing_programming':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.PRACTICING_PROGRAMMING.value)
    if q in 'reading_book':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.READING_BOOK.value)
    if q in 'visiting_person':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.VISITING_PERSON.value)
    if q in 'receiving_person':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.RECEIVING_PERSON.value)
    if q in 'visiting_place':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.VISITING_PLACE.value)
    if q in 'changing_residence':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.CHANGING_RESIDENCE.value)
    if q in 'purchasing':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.PURCHASING.value)
    if q in 'reviewing_lecture':
        if len(q_sequence) > 1:
            for q_lecture in q_sequence[1:]:
                q_builder = q_builder | (Q(activity_type__type=ActivityType.TypeChoices.REVIEWING_LECTURE.value) &
                           Q(activity_type__lecture__name_en__contains=q_lecture))
        else:
            q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.REVIEWING_LECTURE.value)
    if q in 'reviewing_general_topic':
        if len(q_sequence) > 1:
            for g_topic in q_sequence[1:]:
                q_builder = q_builder | (Q(activity_type__type=ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC.value) &
                           Q(activity_type__general_topic__title__contains=g_topic))
        else:
            q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC.value)
    if q in 'sleeping':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.SLEEPING.value)
    if q in 'relaxing':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.RELAXING.value)
    if q in 'cleaning_clothes':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.CLEANING_CLOTHS.value)
    if q in 'cleaning_home':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.CLEANING_HOME.value)
    if q in 'visiting_doctor':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.VISITING_DOCTOR.value)
    if q in 'preparing_food':
        q_builder = q_builder | Q(activity_type__type=ActivityType.TypeChoices.PREPARING_FOOD.value)
    return q_builder


class ActivityAutocomplete(autocomplete.Select2QuerySetView):
    """
        Returns Activities that filtered using the provided query string.

        It builds the Q object from the string you provide. The provided string should have the structure:
        <activity_type>
        <activity_type>+<related-name>+<related-name>+<related-name>...
        <activity_type><space><activity_time_in_hours>+<related-name>+<related-name>+<related-name>...

        Note that the four characters (_, -, +, and space) are special; you should use them in their respective places.
        _ is used in activity_type like 'night_prayer'
        space is used to separate activity_type from activity_time_in_hours, if you want to provide time. It can also be
        used if you want to combine many different activity_types.
        - is used in names like Quran surahs' names or lecture names, for example Al-Nur.
        + is used to separate different names. The separated name would be combined with OR operations.
        """
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Activity.objects.none()

        qs = Activity.objects.all()
        q_builder = Q()
        if self.q:
            q_args = self.q.strip().split(' ')
            for q in q_args:
                try:
                    q_num = int(q)
                    time = timezone.now().replace(hour=q_num, minute=0, second=0, microsecond=0)
                    # q_builder = q_builder | Q(after_midnight_diary_set__alfajr__range=(time, time + datetime.timedelta(hours=1)))
                    # q_builder = q_builder | Q(time_from__range=(time, time + datetime.timedelta(hours=1)))
                    # The default operator is AND
                    q_builder = q_builder & Q(time_from__hour=q_num)
                except ValueError:
                    q_builder = q_builder & get_activity_type_query_for_activity(q)
                    continue
        qs = qs.filter(q_builder)
        # print(qs.query)
        return qs


class ActivityTypeAutocomplete(autocomplete.Select2QuerySetView):
    """
    Returns ActivityTypes that filtered using the provided query string.

    It builds the Q object from the string you provide. The provided string should have the structure:
    <activity_type>
    <activity_type>+<related-name>+<related-name>+<related-name>...
    <activity_type><space><activity_time_in_hours>+<related-name>+<related-name>+<related-name>...

    Note that the four characters (_, -, +, and space) are special; you should use them in their respective places.
    _ is used in activity_type like 'night_prayer'
    space is used to separate activity_type from activity_time_in_hours, if you want to provide time. It can also be
    used if you want to combine many different activity_types.
    - is used in names like Quran surahs' names or lecture names, for example Al-Nur.
    + is used to separate different names. The separated name would be combined with OR operations.
    """
    def get_queryset(self):
        qs = ActivityType.objects.all()
        q_builder = Q()
        if self.q:
            q_args = self.q.strip().split(' ')
            for q in q_args:
                q_builder = q_builder & get_activity_type_query(q)
        qs = qs.filter(q_builder)
        # print(qs.query)
        return qs