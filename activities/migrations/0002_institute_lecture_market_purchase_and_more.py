# Generated by Django 5.0.4 on 2024-04-15 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=48, null=True)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='activitytype',
            name='purchasing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitytype',
            name='reviewing_lecture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='diary',
            name='fasting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='fifth_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fifth_name_person_set', to='activities.personname'),
        ),
        migrations.AddField(
            model_name='person',
            name='seventh_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seventh_name_person_set', to='activities.personname'),
        ),
        migrations.AddField(
            model_name='person',
            name='sixth_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sixth_name_person_set', to='activities.personname'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.book'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='night_prayer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='night_prayer_surahs',
            field=models.ManyToManyField(null=True, related_name='night_prayer_surah_activityType_set', to='activities.quransurah'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='practicing_programming',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='programming',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.programming'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='quran_surahs',
            field=models.ManyToManyField(null=True, related_name='recited_quran_surah_activityType_set', to='activities.quransurah'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='reading_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='received_persons',
            field=models.ManyToManyField(null=True, related_name='received_persons_set', to='activities.person'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='receiving_person',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='reciting_quran',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='relaxing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='sleeping',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='visited_persons',
            field=models.ManyToManyField(null=True, related_name='visited_persons_activityType_set', to='activities.person'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='visited_places',
            field=models.ManyToManyField(null=True, to='activities.place'),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='visiting_person',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='visiting_place',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='after_midnight',
            field=models.ManyToManyField(related_name='after_midnight_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='after_noon',
            field=models.ManyToManyField(related_name='after_noon_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='before_midnight',
            field=models.ManyToManyField(related_name='before_midnight_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='during_day',
            field=models.ManyToManyField(related_name='during_day_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='evening',
            field=models.ManyToManyField(related_name='evening_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='morning',
            field=models.ManyToManyField(related_name='morning_diary_set', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='current_residence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.place'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_name_person_set', to='activities.personname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='fourth_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fourth_name_person_set', to='activities.personname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='prior_residences',
            field=models.ManyToManyField(null=True, related_name='person_place_prior_residences_rel', to='activities.place'),
        ),
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_name_person_set', to='activities.personname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='third_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_name_person_set', to='activities.personname'),
        ),
        migrations.AlterField(
            model_name='personname',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='programming',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('note', models.TextField(null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.institute')),
            ],
        ),
        migrations.AddField(
            model_name='activitytype',
            name='lecture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.lecture'),
        ),
        migrations.AddField(
            model_name='activitytype',
            name='market',
            field=models.ManyToManyField(null=True, to='activities.market'),
        ),
    ]
