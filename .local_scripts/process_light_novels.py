# To execute the script:
# python manage.py shell
# exec(open(".local_scripts/process_light_novels.py", encoding="utf8").read())
from light_novels import models

from lxml import etree
from lxml.cssselect import CSSSelector

martial_peak = models.Novel.objects.filter(name='Martial Peak').first()
for i in range(5, 102):
    chapter = models.Chapter.objects.get(pk=i)

    body_sel = CSSSelector('body')
    h3_sel = CSSSelector('h3')
    strong_sel = CSSSelector('strong')
    raw_material = etree.HTML(chapter.text)
    head = h3_sel(raw_material)[0].text
    sub_heads = [s_h.text for s_h in strong_sel(raw_material)]
    chapter_content = body_sel(raw_material)[0]

    words = {}
    sentences = {}
    for ins in chapter_content.iter('p'):
        if ins.text:
            text = ins.text
            text = text.replace('\n', ' ')
            text = text.replace('\t', ' ')
            text = text.replace('\r', ' ')
            for word in text.split():
                word = word.strip('"').strip(";").strip("!")
                word = word.strip("'").strip(".").strip(",")
                word = word.strip("?")
                word = word.strip("“").strip("”").strip("?”").strip("!”").strip(".”")
                if len(word) > 1:
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
            for sentence_s_1 in text.split('.'):
                for sentence_s_2 in sentence_s_1.split(','):
                    sentence_s_2 = sentence_s_2.strip(" ").strip("“").strip("”")
                    if len(sentence_s_2) > 1:
                        if sentence_s_2 in sentences:
                            sentences[sentence_s_2] += 1
                        else:
                            sentences[sentence_s_2] = 1

    for word in words:
        print('inserting the word: ', word)
        word_2 = models.Word.objects.filter(text=word).first()
        if not word_2:
            word_2 = models.Word.objects.create(text=word)
        models.ChapterWord.objects.create(word=word_2, chapter=chapter, count=words[word])
    for sentence in sentences:
        print('inserting the sentence: ', sentence)
        sentence_2 = models.Sentence.objects.filter(text=sentence).first()
        if not sentence_2:
            sentence_2 = models.Sentence.objects.create(text=sentence)
        models.ChapterSentence.objects.create(sentence=sentence_2, chapter=chapter, count=sentences[sentence])



