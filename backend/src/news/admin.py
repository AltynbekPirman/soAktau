from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import Announcement, Question, News


class TextAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_kaz', 'text_rus')


admin.site.register(Question)
admin.site.register(News, TextAdmin)

admin.site.register(Announcement)
