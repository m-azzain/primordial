from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from activities.models import Diary


class DiaryListView(ListView):
    model = Diary
    template_name = "activities/diary_list.html"
    context_object_name = "diaries"
    paginate_by = 15

    def get_queryset(self):
        return Diary.objects.all().order_by('-date')


class DiaryDetailView(DetailView):
    model = Diary
    template_name = "activities/diary_detail.html"
    context_object_name = "diary"

