from django.test import TestCase
from django.utils import timezone

from activities.models import Diary, Activity, ActivityType


# Create your tests here.
class DiaryTestCase(TestCase):
    fixtures = ['testdata_031f78ea.json']

    def test_diary_after_midnight_sleep_duration_is_positive_and_less_than_or_equal_5(self):
        """"
        Tests diary after midnight sleep duration should be positive and less than or equal 5.

        We already have data from testdata_031f78ea.json that been dumped from our database. The data is compatible
        with this our application models structure as of the commit 031f78ea.
        """
        diaries = Diary.objects.all()
        for diary in diaries:
            print(diary)
            self.assertGreaterEqual(diary.get_after_midnight_sleep_duration(), 0,
                                    msg='after midnight sleep duration of a diary should be positive')
            self.assertLessEqual(diary.get_after_midnight_sleep_duration(), 5,
                                    msg='after midnight sleep duration of a diary should be less than or equal 5')

