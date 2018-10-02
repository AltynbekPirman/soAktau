from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from django_summernote.widgets import SummernoteWidget

from services.models import Post, SubService, Service, Title

admin.site.register((Title, SubService))


# class SubServiceInline(admin.StackedInline):
#     model = SubService
#     extra = 0


# class TitleInline(admin.StackedInline):
#     model = Title
#     extra = 0


class PostInline(admin.StackedInline, SummernoteInlineModelAdmin):
    model = Post
    extra = 0
    summernote_fields = ('text',)


class ServiceAdmin(admin.ModelAdmin):

    inlines = [
        PostInline
    ]

    def get_queryset(self, request):
        qs = super(ServiceAdmin, self).get_queryset(request)
        qs = qs.order_by('language',)
        return qs

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows': 3, 'cols': 130})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 130})},

    }


admin.site.register(Service, ServiceAdmin)
