from django.test import TestCase

from activities.models import Activity, ActivityType
from activities.utils import get_activity_diary_id_list, FIXTURES_FILE_NAME


class ActivityTestCase(TestCase):
    fixtures = [FIXTURES_FILE_NAME]

    def test_activity_duration_should_be_positive(self):
        """"
        Activity duration should be positive.

        duration is a generated field which calculate the difference between The activity time_from and time_to fields
        """

        activities = Activity.objects.all()
        for activity in activities:
            # print(activity)
            self.assertGreaterEqual(activity.duration, 0,
                                    'Activity duration should be greater than or equal zero')

    def test_night_prayer_activity_type_should_be_unique(self):
        """
        NIGHT_PRAYER activity_type should be unique.
        This uniqueness is together with ManyToManyField, night_prayer_surahs.
        That means and activity type of NIGHT_PRAYER that has specific surahs should not be duplicated.
        """
        # activity_types = ActivityType.objects.filter(night_prayer_surahs__isnull=False)
        activity_types = ActivityType.objects.filter(type='NIGHT_PRAYER')
        for activity_type in activity_types:
            activity_type_surahs = list(activity_type.night_prayer_surahs.all().order_by('id').
                                        values_list('id', flat=True))
            for activity_type_2 in activity_types:
                activity_type_2_surahs = list(activity_type_2.night_prayer_surahs.all().order_by('id').
                                              values_list('id', flat=True))
                if activity_type_2 != activity_type:
                    self.assertNotEqual(activity_type_surahs, activity_type_2_surahs,
                                        msg='activity_type NIGHT_PRAYER should be unique')

    def test_reciting_quran_activity_type_should_be_unique(self):
        """
        RECITING_QURAN activity_type should be unique.
        This uniqueness is together with ManyToManyField, quran_surahs.
        That means and activity type of RECITING_QURAN that has specific surahs should not be duplicated.
        """
        # activity_types = ActivityType.objects.filter(quran_surahs__isnull=False)
        activity_types = ActivityType.objects.filter(type='RECITING_QURAN')
        for activity_type in activity_types:
            activity_type_surahs = list(activity_type.quran_surahs.all().order_by('id').values_list('id', flat=True))
            for activity_type_2 in activity_types:
                activity_type_2_surahs = list(activity_type_2.quran_surahs.all().order_by('id').
                                              values_list('id', flat=True))
                if activity_type_2 != activity_type:
                    # print(activity_type_surahs, activity_type_2_surahs)
                    self.assertNotEqual(activity_type_surahs, activity_type_2_surahs,
                                        msg='activity_type RECITING_QURAN should be unique')

    def test_an_activity_should_belong_to_at_least_one_diary(self):
        for activity in Activity.objects.all():
            activity_diary_id_list = get_activity_diary_id_list(activity)
            self.assertGreater(len(activity_diary_id_list), 0, msg='Activity should have at least one diary')