# To execute the script:
# python manage.py shell
# exec(open(".local_scripts/populate_light_novels.py").read())
from light_novels import models
import os
import re

chapter_no_re = re.compile(r'chapter[\s*\-_]*(\d+)([\s\S]+)', re.I)

main_dir = r'C:\Users\malza\Documents\light_novels\martial-peak\04000'

martial_peak = models.Novel.objects.filter(name='Martial Peak').first()
print(martial_peak)
for subdir, dirs, files in os.walk(main_dir):
    for file in files:
        if not file.endswith('(raw).html'):
            print(F'{subdir}/{file}')
            chapter_no_search = chapter_no_re.search(file)
            chapter_no = chapter_no_search.group(1)
            title = file.replace('.html', '')
            with open(os.path.join(subdir, file), 'r', encoding="utf8") as f:
                contents = f.read()
                models.Chapter.objects.create(title=title, novel=martial_peak, number=chapter_no, text=contents)