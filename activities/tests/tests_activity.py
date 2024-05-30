from django.test import TestCase

from activities.models import Activity, ActivityType


class ActivityTestCase(TestCase):
    fixtures = ['testdata_031f78ea.json']

    def test_activity_duration_should_be_positive(self):
        """"
        Activity duration should be positive.

        duration is a generated field which calculate the difference between The activity time_from and time_to fields
        """

        activities = Activity.objects.all()
        for activity in activities:
            print(activity)
            self.assertGreaterEqual(activity.duration, 0,
                                    'Activity duration should be greater than or equal zero')
