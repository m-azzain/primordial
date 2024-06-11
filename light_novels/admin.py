from django.contrib import admin

from .forms import BadSentenceForm
from .models import (Novel, Chapter, ProfanityCategory, WordExample, Word, BadWord,
                     ChapterWord, Sentence, BadSentence, ChapterSentence)

class BadSentenceAdmin(admin.ModelAdmin):
    form = BadSentenceForm


admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(ProfanityCategory)
admin.site.register(WordExample)
admin.site.register(Word)
admin.site.register(BadWord)
admin.site.register(ChapterWord)
admin.site.register(Sentence)
admin.site.register(BadSentence, BadSentenceAdmin)
admin.site.register(ChapterSentence)

