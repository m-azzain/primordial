# Generated by Django 5.0.4 on 2024-04-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_inserting_quran_surahs'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
