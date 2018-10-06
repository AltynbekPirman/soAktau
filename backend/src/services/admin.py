from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django_summernote.widgets import SummernoteWidget

from services.models import Post, SubService, Service, Title


class SubServiceAdmin(admin.ModelAdmin):
    fields = ('title_kaz', 'title_rus', 'order_in_list')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(code__isnull=True)
        return qs


class TitleAdmin(admin.ModelAdmin):
    fields = ('name_kaz', 'name_rus', 'order_in_list')


class SummernoteInlineModelAdmin(admin.options.InlineModelAdmin):
    formfield_overrides = {models.TextField: {'widget': SummernoteWidget}}


class PostInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Post
    ordering = ('-created_date', )
    fields = ('sub_service', 'title', 'text_kaz', 'text_rus')
    summernote_fields = ('text',)
    extra = 1


class ServiceAdmin(admin.ModelAdmin):

    inlines = [
        PostInline
    ]

    def get_queryset(self, request):
        qs = super(ServiceAdmin, self).get_queryset(request)
        return qs

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows': 3, 'cols': 130})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 130})},

    }


admin.site.register(Title, TitleAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(Service, ServiceAdmin)
