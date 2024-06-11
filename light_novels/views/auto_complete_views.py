import datetime

from dal import autocomplete
from django.contrib.postgres.search import SearchQuery
from django.db.models import Q
from django.utils import timezone

from light_novels.models import Sentence


class SentenceAutocomplete(autocomplete.Select2QuerySetView):
    """
    Autocomplete view for Sentence objects.
    Returns sentences with text that match the given search terms.
    """
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Activity.objects.none()

        qs = Sentence.objects.all()
        if self.q:
            q_args = self.q.strip()
            qs = qs.filter(text__search=SearchQuery(q_args))
        print(qs.query)
        return qs
