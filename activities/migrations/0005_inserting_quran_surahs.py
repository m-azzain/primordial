import re
from django.db import migrations, models

r_en = re.compile(r'^([^(]*)\(')
r_ar = re.compile(r'^[0-9]*-([^0-9]*)[0-9]*-([^0-9]*)[0-9]*-([^0-9]*)')
surah_en = []
surah_ar = []
with open("activities/files/quran_surah_en.txt", encoding='utf8') as file_en:
    for line_en in file_en:
        surah_en.append(r_en.search(line_en).groups(1)[0].strip())

# If you provide a negative value to step, then the slicing runs backward, meaning from right to left.
# For example, if you set step equal to -1, then you can build a slice that
# retrieves all the characters in reverse order
with open("activities/files/quran_surah_ar.txt", encoding='utf8') as file_ar:
    for line_ar in file_ar:
        groups = r_ar.search(line_ar).groups()
        # surah_ar.append(groups[0].strip()[slice(None, None, -1)])
        # surah_ar.append(groups[1].strip()[slice(None, None, -1)])
        # surah_ar.append(groups[2].strip()[slice(None, None, -1)])
        # surah_ar.append(groups[0].strip()[::-1])
        # surah_ar.append(groups[1].strip()[::-1])
        # surah_ar.append(groups[2].strip()[::-1])
        # surah_ar.append("".join(reversed(groups[0].strip())))
        # surah_ar.append("".join(reversed(groups[1].strip())))
        # surah_ar.append("".join(reversed(groups[2].strip())))
        surah_ar.append(groups[0].strip())
        surah_ar.append(groups[1].strip())
        surah_ar.append(groups[2].strip())

i = 1
combined_list = []
for a, e in zip(surah_ar, surah_en):
    combined_list.append((i, a, e))
    i += 1


class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0004_eventtype_activitytype_cleaning_clothes_and_more'),
    ]

    operations = [migrations.AddField(
        model_name='QuranSurah',
        name='number',
        field=models.IntegerField(default=0),
    )]
    for n, a, e in combined_list:
        operations.append(
            migrations.RunSQL(
                F"insert into activities_quransurah(\"number\",\"name_ar\", \"name_en\")values({n},'{a}','{e}')"))
