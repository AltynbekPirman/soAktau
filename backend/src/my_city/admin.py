from django.contrib import admin

from my_city.models import CityImage, CityVideo, CityNews


class ImageInline(admin.StackedInline):
    model = CityImage
    extra = 1


class VideoInline(admin.StackedInline):
    model = CityVideo
    extra = 1


class MyCityAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline]


admin.site.register(CityNews, MyCityAdmin)
