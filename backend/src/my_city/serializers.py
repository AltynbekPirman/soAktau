from rest_framework import serializers

from main.accessories import ImageLinker
from my_city.models import CityNews


class CityNewsSerializer(serializers.ModelSerializer):
    kaz = serializers.SerializerMethodField('group_by_lang_kaz')
    rus = serializers.SerializerMethodField('group_by_lang_rus')

    class Meta:
        model = CityNews
        fields = ('kaz', 'rus')

    def get_image_urls(self, obj):
        images = obj.images.all()
        return [self.context['request'].build_absolute_uri(image.icon.url) for image in images]

    def get_screen_url(self, obj):
        images = obj.images.all()
        video_screen = obj.video_screenshot

        if images:
            return self.context['request'].build_absolute_uri(images[0].icon.url)
        elif video_screen:
            return self.context['request'].build_absolute_uri(video_screen.url)

    def get_thumbnail_url(self, obj):
        if obj.thumbnail:
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)
        return None

    def group_by_lang_kaz(self, obj):
        return {
            'id': obj.id, 'title': obj.title_kaz, 'body': ImageLinker(obj.text_kaz).link_images(),
            'createdAt': obj.created_date, 'imageUrls': self.get_image_urls(obj), 'video': obj.video_url,
            'image': self.get_screen_url(obj), 'viewCount': obj.view_count, 'thumbnail': self.get_thumbnail_url(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'id': obj.id, 'title': ImageLinker(obj.title_rus).link_images(), 'body': obj.text_rus,
            'createdAt': obj.created_date, 'imageUrls': self.get_image_urls(obj), 'video': obj.video_url,
            'image': self.get_screen_url(obj), 'viewCount': obj.view_count, 'thumbnail': self.get_thumbnail_url(obj)
        }
