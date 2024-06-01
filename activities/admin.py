from django.contrib import admin

from .forms import DiaryForm, ActivityForm, ActivityTyeForm
from .models import (PersonName, Place, Market,
                     Person, QuranSurah, Book,
                     Purchase, Institute, Course, Lecture,
                     Programming, ActivityType, Activity,
                     Diary, EventType, Event, Doctor, Food, GeneralTopic)


class DiaryAdmin(admin.ModelAdmin):
    form = DiaryForm


class ActivityTypeAdmin(admin.ModelAdmin):
    form = ActivityTyeForm
    list_filter = ['type']
    search_fields = ['note']


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityForm
    fieldsets = [(None, {"fields": ["time_from", "time_to"]}), ("Type and Note", {"fields": ["activity_type", "note"]})]
    list_display = ['day_period', 'time_from', 'time_to', 'activity_type', 'note']
    list_filter = ['activity_type__type']
    search_fields = ['note']


admin.site.register(QuranSurah)
admin.site.register(Book)
admin.site.register(Institute)
admin.site.register(PersonName)
admin.site.register(Place)
admin.site.register(Market)
admin.site.register(Programming)
admin.site.register(Person)
admin.site.register(Purchase)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(ActivityType, ActivityTypeAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Doctor)
admin.site.register(Food)
admin.site.register(GeneralTopic)
# admin.site.register(ActivityTypeNightPrayerSurah)

