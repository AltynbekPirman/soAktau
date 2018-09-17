from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from news.models import Announcement, Answer, Question

admin.site.register(Announcement)
# admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):

    inlines = [
        AnswerInline,
    ]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'rows': 3, 'cols': 60})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 60})},

    }
    readonly_fields = ('question', 'language')


admin.site.register(Question, QuestionAdmin)
