# To execute the script:
# python manage.py shell
# exec(open(".local_scripts/populate_activitytype_type_field.py").read())
from activities.models import ActivityType

from django.db import transaction

at = ActivityType.objects.all()
print(at.query)

for a in at:
    more_than_one = 0
    if a.night_prayer:
        a.type = ActivityType.TypeChoices.NIGHT_PRAYER
        a.save()
        more_than_one += 1
    if a.reciting_quran:
        a.type = ActivityType.TypeChoices.RECITING_QURAN
        a.save()
        more_than_one += 1
    if a.reading_book:
        a.type = ActivityType.TypeChoices.READING_BOOK
        a.save()
        more_than_one += 1
    if a.practicing_programming:
        a.type = ActivityType.TypeChoices.PRACTICING_PROGRAMMING
        a.save()
        more_than_one += 1
    if a.visiting_person:
        a.type = ActivityType.TypeChoices.VISITING_PERSON
        a.save()
        more_than_one += 1
    if a.receiving_person:
        a.type = ActivityType.TypeChoices.RECEIVING_PERSON
        a.save()
        more_than_one += 1
    if a.visited_doctor:
        a.type = ActivityType.TypeChoices.VISITING_DOCTOR
        a.save()
        more_than_one += 1
    if a.visiting_place:
        a.type = ActivityType.TypeChoices.VISITING_PLACE
        a.save()
        more_than_one += 1
    if a.moving_to_different_residence:
        a.type = ActivityType.TypeChoices.CHANGING_RESIDENCE
        a.save()
        more_than_one += 1
    if a.purchasing:
        a.type = ActivityType.TypeChoices.PURCHASING
        a.save()
        more_than_one += 1
    if a.reviewing_lecture:
        a.type = ActivityType.TypeChoices.REVIEWING_LECTURE
        a.save()
        more_than_one += 1
    if a.reviewing_general_topic:
        a.type = ActivityType.TypeChoices.REVIEWING_GENERAL_TOPIC
        a.save()
        more_than_one += 1
    if a.sleeping:
        a.type = ActivityType.TypeChoices.SLEEPING
        a.save()
        more_than_one += 1
    if a.relaxing:
        a.type = ActivityType.TypeChoices.RELAXING
        a.save()
        more_than_one += 1
    if a.cleaning_clothes:
        a.type = ActivityType.TypeChoices.CLEANING_CLOTHS
        a.save()
        more_than_one += 1
    if a.cleaning_home:
        a.type = ActivityType.TypeChoices.CLEANING_HOME
        a.save()
        more_than_one += 1
    if a.shaving:
        a.type = ActivityType.TypeChoices.SHAVING
        a.save()
        more_than_one += 1
    if a.preparing_food:
        a.type = ActivityType.TypeChoices.PREPARING_FOOD
        a.save()
        more_than_one += 1
    transaction.commit()
    print(f'updated a record of activity type with id = {a.id} and more_than_one = {more_than_one}')
