# Generated by Django 5.0.6 on 2024-06-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_novels', '0003_word_is_name_word_unique_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profanitycategory',
            name='name',
            field=models.CharField(choices=[('FILTHY', 'FILTHY'), ('ANTI-RELIGIOUS', 'ANTI-RELIGIOUS')], default='FILTHY', max_length=200),
        ),
    ]