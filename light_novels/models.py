from django.db import models


class Novel(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=1)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    number = models.FloatField(default=0.0)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    # BLUE, GREEN, RED
    # blue is the cleanest one, followed by green which less clean, and lastly red is the worst
    flag = models.TextField(choices=[('BLUE', 'BLUE'), ('GREEN', 'GREEN'), ('RED', 'RED')], default='BLUE')
    text = models.TextField()

    def __str__(self):
        st = F'{self.number}: {self.title}'
        return st


class ProfanityCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WordExample(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text.split('\n')[0]


class Word(models.Model):
    text = models.CharField(max_length=50)
    is_name = models.BooleanField(default=False)
    examples = models.ManyToManyField(WordExample)

    def __str__(self):
        return self.text

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['text'], name='unique_word')
        ]


class BadWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='bad_words')
    category = models.ForeignKey(ProfanityCategory, on_delete=models.CASCADE)
    replacements = models.ManyToManyField(Word, blank=True)


class ChapterWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='chapter_words')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return F'{self.chapter.number} - {self.word}  ({self.count})'


class Sentence(models.Model):
    text = models.TextField()


class BadSentence(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, related_name='bad_sentences')
    category = models.ForeignKey(ProfanityCategory, on_delete=models.CASCADE)
    replacements = models.ManyToManyField(Sentence, blank=True)


class ChapterSentence(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, related_name='chapter_sentences')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

