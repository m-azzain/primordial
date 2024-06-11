# To execute the script:
# python manage.py shell
# exec(open(".local_scripts/populate_diary_maghrib_field.py").read())
from activities.models import Diary
dq = Diary.objects.all().order_by('-date')
print(dq.query)
dq1 = dq[0]
print(dq1)
# This last record already has a vlue of almaghrib field been set
t1 = dq1.almaghrib
print(t1)
minute = 0
hour = 0
for d in dq:
    t2 = t1.replace(minute=t1.minute - minute, hour=t1.hour - hour)
    if t2.minute == 0:
        minute = 0
        hour += 1
    else:
        minute = minute + 1
    d.almaghrib = t2
    d.save()
    print(d.almaghrib)
