from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from activities.models import Diary, Activity, ActivityType


class ActivityListView(ListView):
    model = Activity
    template_name = "activities/activity_list.html"
    context_object_name = "activities"
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get("q")
        query = query.strip() if query else ""
        activities = Activity.objects.filter(
            Q(note__icontains=query) | Q(note__icontains=query)
        )
        return activities
        # return Activity.objects.all()


class ActivityDetailView(DetailView):
    model = Activity
    template_name = "activities/activity_detail.html"
    context_object_name = "activity"


class ActivityTypeListView(ListView):
    model = ActivityType
    template_name = "activities/activity_type_list.html"
    context_object_name = "activity_types"
    paginate_by = 50

    def get_queryset(self):
        # query = self.request.GET.get("q")
        # query = query.strip() if query else ""
        activity_types = ActivityType.objects.all().order_by("type", "id")
        return activity_types

