from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django_summernote.widgets import SummernoteWidget

from services.models import Post, SubService, Service, Title

admin.site.register((Title, SubService))


class SummernoteInlineModelAdmin(admin.options.InlineModelAdmin):
    formfield_overrides = {models.TextField: {'widget': SummernoteWidget}}


class PostInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Post
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


admin.site.register(Service, ServiceAdmin)
