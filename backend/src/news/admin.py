from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import Announcement, Question, News


class TextAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_kaz', 'text_rus')


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_kaz', 'text_rus')
    exclude = ('view_count', 'thumbnail')


class AnnouncementAdmin(admin.ModelAdmin):
    exclude = ('view_count', 'thumbnail')


admin.site.register(Question)
admin.site.register(News, NewsAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
