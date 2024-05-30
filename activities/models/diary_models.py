from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

from ..utils import NOTE_LENGTH
from .activity_models import Activity
from .activity_models import AFTER_MIDNIGHT, MORNING, tz
from .models import Place


class Diary(models.Model):
    """
    This class, Diary, is used to store all the diary activities. It inherits from django.db.models.Model.

    We separate the diary activities into five periods of the day.
    we divide the day(24 hours) into five periods:
    1. AFTER_MIDNIGHT (form 00:00 to < 05:00)
    2. MORNING (form 05:00 to < 11:00)
    3. DURING_DAY (form 11:00 to < 18:00)
    4. EVENING (form 18:00 to < 22:00)
    5. BEFORE_MIDNIGHT (form 22:00 to < 23:59)

    Each activity will belong to one of these five periods.
    To make it easy to register your activities you only need to watch the starting time of your activity. That means we
    determine which period an activity belongs to by its starting time; The end time of an activity may expand to the next
    period, but try your best to make your activities sit in one period.
    If you have a long activity that take the whole time of two or more periods, you can separate them into
    two or more activities.
    In the future we may add a validation rule that prevents an activity from expanding more than two periods;
    But that is not likely.

    For any of these 5 period of the day the Activities should have different ActivityType
    For example you can not have two activities in the morning that have the same ActivityType
    For now nothing stop you from doing that, but it is better to simple data structure. That may be good when try
    to generate reports later on.
    We may also think about adding validation to enforce such rule.
    """
    class Meta:
        verbose_name_plural = 'Diaries'

    date = models.DateField()
    alfajr = models.TimeField()
    dawn = models.TimeField()
    almaghrib = models.TimeField()
    after_midnight = models.ManyToManyField(Activity, related_name="after_midnight_diary_set") # 12am to 4am
    morning = models.ManyToManyField(Activity, related_name="morning_diary_set") # 5am to 9am
    during_day = models.ManyToManyField(Activity, related_name="during_day_diary_set") # 9am to 6pm
    evening = models.ManyToManyField(Activity, related_name="evening_diary_set") # 6pm to 9pm
    before_midnight = models.ManyToManyField(Activity, related_name="before_midnight_diary_set") # 9pm to 12pm

    residence = models.ForeignKey(Place, null=True, on_delete=models.CASCADE)
    fasting = models.BooleanField(default=False)

    note = models.TextField(null=True, blank=True)

    def get_after_midnight_sleep_duration(self):
        """
        Returns the sleeping duration of the specific diary period, AFTER_MIDNIGHT.

        The sleeping activity in the period Before Midnight and in the other times (other than After Midnight)
        is registered explicitly. The sleeping activity of the period After Midnight is not registered;
        Because it might be intermittent. We calculate the sleeping time of this duration (After Midnight)
        by subtracting the other activities' durations from the total time ot this period.
        The total time of After Midnight period is 5 hours, it might change in the future.

        There is a flexibility in prayer times; we won't register them. Usually we remove prayers time from the activities
        that happen during the prayer time. Except for Alfajr; its time is usually part of the NIGHT_PRAYER activity.
        """
        after_midnight_total_time = (MORNING.hour - AFTER_MIDNIGHT.hour) + (MORNING.minute - AFTER_MIDNIGHT.minute) / 60
        after_midnight_waking_time = 0
        for activity in self.after_midnight.all():
            after_midnight_waking_time += activity.duration
        return after_midnight_total_time - after_midnight_waking_time

    def display_note(self):
        if len(self.note) > NOTE_LENGTH:
            return self.note[:NOTE_LENGTH]
        return self.note

    def __str__(self):
        return F'Diary: {self.date}'

