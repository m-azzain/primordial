# Generated by Django 5.0.6 on 2024-06-09 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=1)),
                ('author', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfanityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WordExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light_novels.novel')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterSentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light_novels.chapter')),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_sentences', to='light_novels.sentence')),
            ],
        ),
        migrations.CreateModel(
            name='BadSentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light_novels.profanitycategory')),
                ('replacements', models.ManyToManyField(blank=True, to='light_novels.sentence')),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bad_sentences', to='light_novels.sentence')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light_novels.chapter')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_words', to='light_novels.word')),
            ],
        ),
        migrations.CreateModel(
            name='BadWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light_novels.profanitycategory')),
                ('replacements', models.ManyToManyField(blank=True, to='light_novels.word')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bad_words', to='light_novels.word')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='examples',
            field=models.ManyToManyField(to='light_novels.wordexample'),
        ),
    ]
