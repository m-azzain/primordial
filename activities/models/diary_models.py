from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

from ..utils import NOTE_LENGTH
from .activity_models import Activity
from .models import Place


class Diary(models.Model):
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

    def display_note(self):
        if len(self.note) > NOTE_LENGTH:
            return self.note[:NOTE_LENGTH]
        return self.note

    def __str__(self):
        return F'Diary: {self.date}'

