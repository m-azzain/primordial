from dal import autocomplete
from django.forms import ModelForm

from light_novels.models import BadSentence


class BadSentenceForm(ModelForm):
    class Meta:
        model = BadSentence
        fields = '__all__'
        widgets = {
            'sentence': autocomplete
            .ModelSelect2(
                url='light_novels:sentence_autocomplete',
                attrs={
                    'data-placeholder': 'Select a sentence to autocomplete',
                    'data-minimum-input-length': 3,
                }),
        }