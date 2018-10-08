from django.contrib import admin
from django.db import models

from news.models import Announcement, Question, News

admin.site.register(Question)
admin.site.register((Announcement, News))
