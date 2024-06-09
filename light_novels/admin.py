from django.contrib import admin


from .models import (Novel, Chapter, ProfanityCategory, WordExample, Word, BadWord,
                     ChapterWord, Sentence, BadSentence, ChapterSentence)


admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(ProfanityCategory)
admin.site.register(WordExample)
admin.site.register(Word)
admin.site.register(BadWord)
admin.site.register(ChapterWord)
admin.site.register(Sentence)
admin.site.register(BadSentence)
admin.site.register(ChapterSentence)

