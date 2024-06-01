from django.urls import path
from .views import (index, DiaryListView, DiaryDetailView,
                    ActivityListView, ActivityDetailView, ActivityTypeListView,
                    ActivityAutocomplete, ActivityTypeAutocomplete, QuranSurahAutocomplete)

# To avoid the error: "ellipse_bikes is not a registered namespace"
# https://stackoverflow.com/questions/41883254/django-is-not-a-registered-namespace
app_name = "activities"

urlpatterns = [
    path("", index, name="index"),
    path("diaries/", DiaryListView.as_view(), name="diaries"),
    path("diaries/<int:pk>/", DiaryDetailView.as_view(), name="diary"),
    path("activities/", ActivityListView.as_view(), name="activities"),
    path("activities/types", ActivityTypeListView.as_view(), name="activity_types"),
    path("activities/<int:pk>/", ActivityDetailView.as_view(), name="activity"),

    path(r'activity_autocomplete/', ActivityAutocomplete.as_view(), name="activity_autocomplete"),
    path(r'activity_type_autocomplete/', ActivityTypeAutocomplete.as_view(), name="activity_type_autocomplete"),
    path(r"quran_surah/autocomplete/", QuranSurahAutocomplete.as_view(), name="quran_surah_autocomplete"),
]

