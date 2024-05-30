from django.test import TestCase
from django.utils import timezone

from activities.models import Diary, Activity, ActivityType


# Create your tests here.
# class DiaryTestCase(TestCase):
#     def test_diary_after_midnight_sleep_duration_is_positive(self):
#         diary = Diary()
#         diary.save()
class ActivityTestCase(TestCase):
    def test_activity_duration_should_be_positive(self):
        activity = Activity()
        activity.time_from = timezone.now().replace(hour=2).time()
        activity.time_to = timezone.now().replace(hour=3,minute=30).time()
        activity_type = ActivityType(type=ActivityType.TypeChoices.SLEEPING.value)
        activity_type.save()
        activity.activity_type = activity_type
        activity.save()
        self.assertGreaterEqual(activity.duration, 0, 'Activity duration should be greater than or equal zero')