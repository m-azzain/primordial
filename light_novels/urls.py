from django.urls import path

from light_novels.views import ChapterListView, ChapterDetailView, index, SentenceAutocomplete

app_name = 'light_novels'

urlpatterns = [
    path("", index, name="index"),
    path("<int:novel_id>/chapters/", ChapterListView.as_view(), name="chapters"),
    path("<int:novel_id>/chapters/<int:pk>", ChapterDetailView.as_view(), name="chapter"),

    path(r'sentence_autocomplete/', SentenceAutocomplete.as_view(), name="sentence_autocomplete"),
]