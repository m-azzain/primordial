# Generated by Django 5.0.6 on 2024-06-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_novels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='flag',
            field=models.TextField(choices=[('BLUE', 'BLUE'), ('GREEN', 'GREEN'), ('RED', 'RED')], default='BLUE'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.FloatField(default=0.0),
        ),
    ]