from django.views.generic import ListView, DetailView

from lxml import etree, builder, html
from lxml.cssselect import CSSSelector
from lxml.html import builder as html_builder

from light_novels.models import Chapter, Novel


class ChapterListView(ListView):
    model = Chapter
    template_name = 'light_novels/chapter_list.html'
    context_object_name = 'chapters'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.path
        novel = Novel.objects.get(pk=self.kwargs['novel_id'])
        chapters = Chapter.objects.filter(novel=novel)
        # return {'novel': novel, 'chapters': chapters}
        return chapters


class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'light_novels/chapter_detail.html'
    context_object_name = 'chapter'

    def get_context_data(self, **kwargs):
        chapter = Chapter.objects.get(pk=self.kwargs['pk'])
        body_sel = CSSSelector('body')
        h3_sel = CSSSelector('h3')
        strong_sel = CSSSelector('strong')
        raw_material = etree.HTML(chapter.text)
        head = h3_sel(raw_material)[0].text
        sub_heads = [s_h.text for s_h in strong_sel(raw_material)]
        chapter_content = body_sel(raw_material)[0]
        paragraphs = []
        for ins in chapter_content.iter('p'):
            if ins.text:
                paragraphs.append(ins.text)
        return {'chapter': chapter, 'head': head, 'sub_heads': sub_heads, 'paragraphs': paragraphs}
