NOTE_LENGTH = 200
STRING_PADDING_LEN = 20
STRING_PADDING_CHAR = '#'

FIXTURES_FILE_NAME = 'testdata_c3c0a7eb.json'


def get_activity_diary_id_list(activity):
    activity_diary_id_list = []
    if activity.after_midnight_diary_set.count() != 0:
        diary_id_set = activity_diary_id_list.extend(list(activity.after_midnight_diary_set.all().
                                              values_list('id', flat=True)))
    elif activity.morning_diary_set.count() != 0:
        diary_id_set = activity_diary_id_list.extend(list(activity.morning_diary_set.all().values_list('id', flat=True)))
    elif activity.during_day_diary_set.count() != 0:
        diary_id_set = activity_diary_id_list.extend(list(activity.during_day_diary_set.all().values_list('id', flat=True)))
    elif activity.evening_diary_set.count() != 0:
        diary_id_set = activity_diary_id_list.extend(list(activity.evening_diary_set.all().values_list('id', flat=True)))
    elif activity.before_midnight_diary_set.count() != 0:
        diary_id_set = activity_diary_id_list.extend(list(activity.before_midnight_diary_set.all().
                                              values_list('id', flat=True)))
    return activity_diary_id_list
