from django.contrib.auth.models import User
from django.test import TestCase

from activities.models import ActivityType, QuranSurah, Person, Place
from activities.utils import FIXTURES_FILE_NAME
from activities.validators import DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE


class ActivityTypeTestCase(TestCase):
    fixtures = [FIXTURES_FILE_NAME]

    def setUp(self):
        # create a user and do login for the client
        password = 'mypassword'
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        self.client.login(username=my_admin.username, password=password)

    def test_night_prayer_activity_type_should_be_unique(self):
        """
        NIGHT_PRAYER activity_type should be unique.
        This uniqueness is together with ManyToManyField, night_prayer_surahs.
        That means and activity type of NIGHT_PRAYER that has specific surahs should not be duplicated.
        """
        # activity_types = ActivityType.objects.filter(night_prayer_surahs__isnull=False)
        activity_types = ActivityType.objects.filter(type='NIGHT_PRAYER')
        for activity_type in activity_types:
            activity_type_surahs = list(activity_type.night_prayer_surahs.all().order_by('id').
                                        values_list('id', flat=True))
            for activity_type_2 in activity_types:
                activity_type_2_surahs = list(activity_type_2.night_prayer_surahs.all().order_by('id').
                                              values_list('id', flat=True))
                if activity_type_2 != activity_type:
                    self.assertNotEqual(activity_type_surahs, activity_type_2_surahs,
                                        msg='activity_type NIGHT_PRAYER should be unique')

    def test_duplicated_night_prayer_activity_type_should_raise_exception(self):
        """
        NIGHT_PRAYER activity_type should be unique.
        This uniqueness is together with ManyToManyField, night_prayer_surahs.
        That means and activity type of NIGHT_PRAYER that has specific surahs should not be duplicated.
        """
        surah_s = QuranSurah.objects.filter(id__in=[1, 2, 3])
        surah_ids = list(surah_s.values_list('id', flat=True))
        first_activity_type = ActivityType.objects.create(type=ActivityType.TypeChoices.NIGHT_PRAYER)
        first_activity_type.night_prayer_surahs.add(surah_s[0])
        first_activity_type.night_prayer_surahs.add(surah_s[1])
        first_activity_type.night_prayer_surahs.add(surah_s[2])
        first_activity_type.save()

        # Form data type should be in application/json; which is the default
        response = self.client.post("/admin/activities/activitytype/add/", {
            "type": "NIGHT_PRAYER",
            "night_prayer_surahs": surah_ids,
            "book": "",
            "programming": "",
            "moved_to_residence": "",
            "purchase": "",
            "lecture": "",
            "general_topic": "",
            "visited_doctor": "",
            "prepared_food": "",
            "note": "",
        })
        admin_form = response.context_data['adminform']
        self.assertFormError(admin_form, 'night_prayer_surahs',
                             [DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': first_activity_type.id}],
                             'There is a duplicated ActivityType with id')

    def test_reciting_quran_activity_type_should_be_unique(self):
        """
        RECITING_QURAN activity_type should be unique.
        This uniqueness is together with ManyToManyField, quran_surahs.
        That means and activity type of RECITING_QURAN that has specific surahs should not be duplicated.
        """
        # activity_types = ActivityType.objects.filter(quran_surahs__isnull=False)
        activity_types = ActivityType.objects.filter(type='RECITING_QURAN')
        for activity_type in activity_types:
            activity_type_surahs = list(activity_type.quran_surahs.all().order_by('id').values_list('id', flat=True))
            for activity_type_2 in activity_types:
                activity_type_2_surahs = list(activity_type_2.quran_surahs.all().order_by('id').
                                              values_list('id', flat=True))
                if activity_type_2 != activity_type:
                    # print(activity_type_surahs, activity_type_2_surahs)
                    self.assertNotEqual(activity_type_surahs, activity_type_2_surahs,
                                        msg='activity_type RECITING_QURAN should be unique')

    def test_duplicated_reciting_quran_activity_type_should_raise_exception(self):
        """
        RECITING_QURAN activity_type should be unique.
        This uniqueness is together with ManyToManyField, quran_surahs.
        That means and activity type of RECITING_QURAN that has specific surahs should not be duplicated.
        """

        surah_s = QuranSurah.objects.filter(id__in=[1, 2, 3])
        surah_ids = list(surah_s.values_list('id', flat=True))
        first_activity_type = ActivityType.objects.create(type=ActivityType.TypeChoices.RECITING_QURAN)
        first_activity_type.quran_surahs.add(surah_s[0])
        first_activity_type.quran_surahs.add(surah_s[1])
        first_activity_type.quran_surahs.add(surah_s[2])
        first_activity_type.save()

        # Form data type should be in application/json; which is the default
        response = self.client.post("/admin/activities/activitytype/add/", {
            "type": "RECITING_QURAN",
            "quran_surahs": surah_ids,
            "book": "",
            "programming": "",
            "moved_to_residence": "",
            "purchase": "",
            "lecture": "",
            "general_topic": "",
            "visited_doctor": "",
            "prepared_food": "",
            "note": "",
        })
        admin_form = response.context_data['adminform']
        self.assertFormError(admin_form, 'quran_surahs',
                             [DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': first_activity_type.id}],
                             'There is a duplicated ActivityType with id')

    def test_duplicated_receiving_person_activity_type_should_raise_exception(self):
        """
        RECEIVING_PERSON activity_type should be unique.
        This uniqueness is together with ManyToManyField, received_persons.
        That means and activity type of RECEIVING_PERSON that has specific persons should not be duplicated.
        """

        persons = Person.objects.all()[:3]
        person_ids = list(persons.values_list('id', flat=True))
        first_activity_type = ActivityType.objects.create(type=ActivityType.TypeChoices.RECEIVING_PERSON)
        first_activity_type.received_persons.add(persons[0])
        first_activity_type.received_persons.add(persons[1])
        first_activity_type.received_persons.add(persons[2])
        first_activity_type.save()

        # Form data type should be in application/json; which is the default
        response = self.client.post("/admin/activities/activitytype/add/", {
            "type": "RECEIVING_PERSON",
            "received_persons": person_ids,
            "book": "",
            "programming": "",
            "moved_to_residence": "",
            "purchase": "",
            "lecture": "",
            "general_topic": "",
            "visited_doctor": "",
            "prepared_food": "",
            "note": "",
        })
        admin_form = response.context_data['adminform']
        self.assertFormError(admin_form, 'received_persons',
                             [DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': first_activity_type.id}],
                             'There is a duplicated ActivityType with id')

    def test_duplicated_visiting_person_activity_type_should_raise_exception(self):
        """
        VISITING_PERSON activity_type should be unique.
        This uniqueness is together with ManyToManyField, visited_persons.
        That means and activity type of VISITING_PERSON that has specific persons should not be duplicated.
        """

        persons = Person.objects.all()[:3]
        person_ids = list(persons.values_list('id', flat=True))
        first_activity_type = ActivityType.objects.create(type=ActivityType.TypeChoices.VISITING_PERSON)
        first_activity_type.visited_persons.add(persons[0])
        first_activity_type.visited_persons.add(persons[1])
        first_activity_type.visited_persons.add(persons[2])
        first_activity_type.save()

        # Form data type should be in application/json; which is the default
        response = self.client.post("/admin/activities/activitytype/add/", {
            "type": "VISITING_PERSON",
            "visited_persons": person_ids,
            "book": "",
            "programming": "",
            "moved_to_residence": "",
            "purchase": "",
            "lecture": "",
            "general_topic": "",
            "visited_doctor": "",
            "prepared_food": "",
            "note": "",
        })
        admin_form = response.context_data['adminform']
        self.assertFormError(admin_form, 'visited_persons',
                             [DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': first_activity_type.id}],
                             'There is a duplicated ActivityType with id')

    def test_duplicated_visiting_place_activity_type_should_raise_exception(self):
        """
        VISITING_PLACE activity_type should be unique.
        This uniqueness is together with ManyToManyField, visited_places.
        That means an activity type of VISITING_PLACE that has specific places should not be duplicated.
        """

        places = Place.objects.all()[:3]
        place_ids = list(places.values_list('id', flat=True))
        first_activity_type = ActivityType.objects.create(type=ActivityType.TypeChoices.VISITING_PLACE)
        first_activity_type.visited_places.add(places[0])
        first_activity_type.visited_places.add(places[1])
        first_activity_type.visited_places.add(places[2])
        first_activity_type.save()

        # Form data type should be in application/json; which is the default
        response = self.client.post("/admin/activities/activitytype/add/", {
            "type": "VISITING_PLACE",
            "visited_places": place_ids,

        })
        admin_form = response.context_data['adminform']
        self.assertFormError(admin_form, 'visited_places',
                             [DUPLICATED_ACTIVITY_TYPE_VALIDATION_MESSAGE % {'id': first_activity_type.id}],
                             'There is a duplicated ActivityType with id')