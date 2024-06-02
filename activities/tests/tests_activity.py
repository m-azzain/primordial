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

    def test_an_activity_should_belong_to_at_least_one_diary(self):
        for activity in Activity.objects.all():
            activity_diary_id_list = get_activity_diary_id_list(activity)
            self.assertGreater(len(activity_diary_id_list), 0, msg='Activity should have at least one diary')