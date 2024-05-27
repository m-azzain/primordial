# Generated by Django 5.0.4 on 2024-04-19 06:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_lecture_course_alter_activitytype_market_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='activitytype',
            name='cleaning_clothes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitytype',
            name='shaving',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='diary',
            name='alfajr',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary',
            name='dawn',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary',
            name='residence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.place'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.eventtype')),
            ],
        ),
    ]