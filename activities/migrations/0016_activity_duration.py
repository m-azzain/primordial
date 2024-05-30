# Generated by Django 5.0.6 on 2024-05-29 18:19

import django.db.models.expressions
import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0015_remove_activitytype_cleaning_clothes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(django.db.models.functions.datetime.Extract('time_to', 'hour'), '-', django.db.models.functions.datetime.Extract('time_from', 'hour')), '+', django.db.models.expressions.CombinedExpression(django.db.models.expressions.CombinedExpression(django.db.models.functions.datetime.Extract('time_to', 'minute'), '-', django.db.models.functions.datetime.Extract('time_from', 'minute')), '/', models.Value(60))), output_field=models.FloatField()),
        ),
    ]