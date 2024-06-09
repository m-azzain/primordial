from django.urls import path

from light_novels.views import ChapterListView, ChapterDetailView

app_name = 'light_novels'

urlpatterns = [
    path("<int:novel_id>/chapters/", ChapterListView.as_view(), name="chapters"),
    path("<int:novel_id>/chapters/<int:pk>", ChapterDetailView.as_view(), name="chapter"),
]