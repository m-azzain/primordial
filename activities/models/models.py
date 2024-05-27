from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime

NOTE_LENGTH = 200
class PersonName(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)

    def __str__(self):
        return F'({self.name_en}){self.name_ar}'


class Place(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    # Called parallels because they are parallel to the equator and to one another
    # Roughly the distance between each latitude is 69 miles; 111 kilometers
    latitude = models.DecimalField(max_digits=48, null=True, decimal_places=6, blank=True)
    # Run from north to south called meridians.
    # The prime meridian runs through Greenwich Observatory in England; the 0 degree
    # ON the opposite side of the earth is the International date line at approximately 180 degrees longitude,
    # Though the date line does not follow an straight line.
    longitude = models.DecimalField(max_digits=48, null=True, decimal_places=6, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name

class Market(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    # Called parallels because they are parallel to the equator and to one another
    # Roughly the distance between each latitude is 69 miles; 111 kilometers
    latitude = models.DecimalField(max_digits=48, null=True, decimal_places=6, blank=True)
    # Run from north to south called meridians.
    # The prime meridian runs through Greenwich Observatory in England; the 0 degree
    # ON the opposite side of the earth is the International date line at approximately 180 degrees longitude,
    # Though the date line does not follow an straight line.
    longitude = models.DecimalField(max_digits=48, null=True, decimal_places=6, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name

class Person(models.Model):
    first_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="first_name_person_set")
    second_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="second_name_person_set")
    third_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="third_name_person_set")
    fourth_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="fourth_name_person_set")
    fifth_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="fifth_name_person_set", null=True, blank=True)
    sixth_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="sixth_name_person_set", null=True, blank=True)
    seventh_name = models.ForeignKey(PersonName, on_delete=models.CASCADE, related_name="seventh_name_person_set", null=True, blank=True)

    current_residence = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True)
    prior_residences = models.ManyToManyField(Place, related_name="person_place_prior_residences_rel", blank=True)

    def __str__(self):
        return F' {self.fourth_name} {self.third_name} {self.second_name} {self.first_name}'


class Doctor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return F'{self.person}'

class QuranSurah(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return F'({self.name_en}){self.name_ar}'

class Book(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name


class Purchase(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=48, null=True, decimal_places=4)
    currency = models.CharField(max_length=10, default='EGP', choices=[("EGP", "EGP"),
                                                                       ("USD", "USD"),
                                                                       ("EUR", "EUR"),
                                                                       ("SDG", "SDG")])
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name


class Institute(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name


class GeneralTopic(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name_en if self.name_en else self.name_ar}: {self.institute}'


class Lecture(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name_en if self.name_en else self.name_ar}: {self.course}'


class Programming(models.Model):
    language = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.language}: {self.framework}'


class Food(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name_en == 'N/A':
            name = self.name_ar
        elif self.name_ar == 'N/A':
            name = self.name_en
        else:
            name = f'({self.name_en}){self.name_ar}'
        return name


class EventType(models.Model):
    type = models.CharField(max_length=200)
    note = models.TextField(null=True)

    def __str__(self):
        return self.type


class Event(models.Model):
    date = models.DateField()
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return F"{self.type} of: {self.note}"

