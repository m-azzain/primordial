from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime

from .models import (QuranSurah, Book, Programming, Person,
                     Place, Market, Purchase, Lecture, Doctor, Food, GeneralTopic)
from ..utils import NOTE_LENGTH, STRING_PADDING_LEN, STRING_PADDING_CHAR


class ActivityType(models.Model):
    class TypeChoices(models.TextChoices):
        NIGHT_PRAYER = 'NIGHT_PRAYER', _('Night Prayer')
        RECITING_QURAN = 'RECITING_QURAN', _('Reciting Quran')
        READING_BOOK = 'READING_BOOK', _('Reading Book')
        PRACTICING_PROGRAMMING = 'PRACTICING_PROGRAMMING', _('Practicing Programming')
        VISITING_PERSON = 'VISITING_PERSON', _('Visiting Person')
        RECEIVING_PERSON = 'RECEIVING_PERSON', _('Receiving Person')
        VISITING_DOCTOR = 'VISITING_DOCTOR', _('Visiting Dotor')
        VISITING_PLACE = 'VISITING_PLACE', _('Visiting Place')
        CHANGING_RESIDENCE = 'CHANGING_RESIDENCE', _('Changing Residence')
        PURCHASING = 'PURCHASING', _('Purchasing')
        REVIEWING_LECTURE = 'REVIEWING_LECTURE', _('Reviewing Lecture')
        REVIEWING_GENERAL_TOPIC = 'REVIEWING_GENERAL_TOPIC', _('Reviewing General Topic')
        SLEEPING = 'SLEEPING', _('Sleeping')
        RELAXING = 'RELAXING', _('Relaxing')
        CLEANING_CLOTHS = 'CLEANING_CLOTHS', _('Cleaning Cloths')
        CLEANING_HOME = 'CLEANING_HOME', _('Cleaning Home')
        SHAVING = 'SHAVING', _('Shaving')
        PREPARING_FOOD = 'PREPARING_FOOD', _('Preparing Food')
    type = models.CharField(max_length=30, choices=TypeChoices.choices, default=TypeChoices.NIGHT_PRAYER)

    night_prayer_surahs = models.ManyToManyField(QuranSurah, related_name="night_prayer_surah_activityType_set", blank=True)
    quran_surahs = models.ManyToManyField(QuranSurah, related_name="recited_quran_surah_activityType_set", blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    programming = models.ForeignKey(Programming, on_delete=models.CASCADE, null=True, blank=True)
    visited_persons = models.ManyToManyField(Person, related_name="visited_persons_activityType_set", blank=True)
    received_persons = models.ManyToManyField(Person, related_name="received_persons_set", blank=True)
    visited_places = models.ManyToManyField(Place, blank=True)
    moved_to_residence = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="moved_to_residence_set",
                                           null=True, blank=True)
    market = models.ManyToManyField(Market, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)
    general_topic = models.ForeignKey(GeneralTopic, on_delete=models.CASCADE, null=True, blank=True)
    visited_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    prepared_food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)

    note = models.TextField(null=True, blank=True)

    def get_type(self) -> TypeChoices:
        return self.TypeChoices[self.type]

    def __str__(self):
        str1 = []
        if self.get_type() is ActivityType.TypeChoices.NIGHT_PRAYER:
            str1.append('night_prayer'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            surahs = F'({",".join([str(s) for s in self.night_prayer_surahs.all()])})'
            str1.append(surahs)
        if self.get_type() is ActivityType.TypeChoices.RECITING_QURAN:
            str1.append('reciting_quran'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            surahs = F'({",".join([str(s) for s in self.quran_surahs.all()])})'
            str1.append(surahs)
        if self.get_type() is ActivityType.TypeChoices.READING_BOOK:
            str1.append(F'reading_book'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR)+f'({self.book})')
        if self.get_type() is ActivityType.TypeChoices.PRACTICING_PROGRAMMING:
            str1.append(F'programming'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR)+f'({self.programming})')
        if self.get_type() is ActivityType.TypeChoices.VISITING_PERSON:
            str1.append('visiting_person'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            persons = F'({",".join([str(s) for s in self.visited_persons.all()])})'
            str1.append(persons)
        if self.get_type() is ActivityType.TypeChoices.RECEIVING_PERSON:
            str1.append('receiving_person'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            # persons = F'({",".join([str(s) for s in self.received_persons.all()])})'
            # str1.append(persons)
        if self.get_type() is ActivityType.TypeChoices.VISITING_PLACE:
            str1.append('visiting_place'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            places = F'({",".join([str(s) for s in self.visited_places.all()])})'
            str1.append(places)
        if self.get_type() is ActivityType.TypeChoices.CHANGING_RESIDENCE:
            str1.append('changing_residence'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR) +
                        f'({self.moved_to_residence})')
        if self.get_type() is ActivityType.TypeChoices.PURCHASING:
            str1.append(F'purchasing'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR)+f'({self.purchase})')
        if self.get_type() is ActivityType.TypeChoices.REVIEWING_LECTURE:
            str1.append(F'reviewing_lecture'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR)+f'({self.lecture})')
        if self.get_type() is ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC:
            str1.append(
                F'reviewing_general_topic'.upper().ljust(STRING_PADDING_LEN, STRING_PADDING_CHAR) +
                f'({self.general_topic})')
        if self.get_type() is ActivityType.TypeChoices.SLEEPING:
            str1.append('sleeping'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
        if self.get_type() is ActivityType.TypeChoices.RELAXING:
            str1.append('relaxing'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
        if self.get_type() is ActivityType.TypeChoices.CLEANING_CLOTHS:
            str1.append('cleaning_clothes'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
        if self.get_type() is ActivityType.TypeChoices.SHAVING:
            str1.append('shaving'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))

        if self.get_type() is ActivityType.TypeChoices.VISITING_DOCTOR:
            str1.append(F'visiting_doctor'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR)+f'({self.visited_doctor})')
        if self.get_type() is ActivityType.TypeChoices.PREPARING_FOOD:
            str1.append('preparing_food'.upper().ljust(STRING_PADDING_LEN,STRING_PADDING_CHAR))
            str1.append(F'({self.prepared_food})')
        if self.get_type() is ActivityType.TypeChoices.CLEANING_HOME:
            str1.append('cleaning_home'.upper().ljust(STRING_PADDING_LEN, STRING_PADDING_CHAR))
        return F'AT: {', '.join(str1)}'


class Activity(models.Model):

    class Meta:
        verbose_name_plural = 'Activities'

    time_from = models.TimeField()
    time_to = models.TimeField()
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)

    @admin.display(
        ordering='activity_type',
        description="Period of the Day",
    )
    def day_period(self):
        tz = timezone.get_current_timezone() # django get us the time zone from the settings
        after_midnight = datetime.datetime(2000, 1, 1, 0, 0, 0, 0, tzinfo=tz)
        # midnight = datetime.strptime('2000/01/01 00:00:00.000000', '%d/%m/%y %H:%M:%S.%f')
        # midnight = midnight.astimezone(tz)
        after_midnight = after_midnight.time()
        morning = datetime.datetime(2000, 1, 1, 5, 0, 0, 0, tzinfo=tz)
        morning = morning.time()
        during_day = datetime.datetime(2000, 1, 1, 11, 0, 0, 0, tzinfo=tz)
        during_day = during_day.time()
        evening = datetime.datetime(2000, 1, 1, 18, 0, 0, 0, tzinfo=tz)
        evening = evening.time()
        before_midnight = datetime.datetime(2000, 1, 1, 22, 0, 0, 0, tzinfo=tz)
        before_midnight = before_midnight.time()
        if self.time_from >= after_midnight and self.time_from < morning:
            return "after_midnight"
        elif self.time_from >= morning and self.time_from < during_day:
            return "morning"
        elif self.time_from >= during_day and self.time_from < evening:
            return "during_day"
        elif self.time_from >= evening and self.time_from < before_midnight:
            return "evening"
        elif self.time_from >= before_midnight:
            return "before_midnight"

    def __str__(self):
        return F'{self.activity_type}: {self.time_from} to {self.time_to}'

