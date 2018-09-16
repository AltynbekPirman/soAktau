from django.contrib import admin

from services.models import Post, SubService, Service

admin.site.register((Service, SubService, Post))
