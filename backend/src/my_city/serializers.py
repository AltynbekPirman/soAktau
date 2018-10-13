from rest_framework import serializers

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

    def group_by_lang_kaz(self, obj):
        return {
            'id': obj.id, 'title': obj.title_kaz, 'body': obj.text_kaz, 'createdAt': obj.created_date,
            'imageUrls': self.get_image_urls(obj), 'video': obj.video_url, 'image': self.get_screen_url(obj)
        }

    def group_by_lang_rus(self, obj):
        return {
            'id': obj.id, 'title': obj.title_rus, 'body': obj.text_rus, 'createdAt': obj.created_date,
            'imageUrls': self.get_image_urls(obj), 'video': obj.video_url, 'image': self.get_screen_url(obj)
        }
