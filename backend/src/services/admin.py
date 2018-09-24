from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from services.models import Post, SubService, Service, Title

admin.site.register((Title, SubService))


# class SubServiceInline(admin.StackedInline):
#     model = SubService
#     extra = 0


# class TitleInline(admin.StackedInline):
#     model = Title
#     extra = 0


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class ServiceAdmin(admin.ModelAdmin):

    inlines = [
        PostInline
    ]

    def get_queryset(self, request):
        qs = super(ServiceAdmin, self).get_queryset(request)
        qs = qs.order_by('language',)
        return qs

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows': 3, 'cols': 160})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 160})},

    }


admin.site.register(Service, ServiceAdmin)
