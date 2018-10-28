from django.db.models.signals import post_save
from django.dispatch import receiver

from main.accessories import ThumbnailCreator
from my_city.models import CityNews


@receiver(post_save, sender=CityNews)
def save_thumbnail(sender, instance: CityNews, **kwargs):
    if not instance.disable_signals:
        if instance.images.all():
            thumbnail_file = ThumbnailCreator.get_thumbnail(instance.images.all()[0].icon.name)
            thumbnail_file.save('./media/my_city_thumbnails/thumbnail_{}.png'.format(instance.id), "PNG")
            instance.thumbnail = 'my_city_thumbnails/thumbnail_{}.png'.format(instance.id)
            instance.save_without_signals()
        elif instance.video_screenshot:
            thumbnail_file = ThumbnailCreator.get_thumbnail(instance.video_screenshot.name)
            thumbnail_file.save('./media/my_city_thumbnails/thumbnail_{}.png'.format(instance.id), "PNG")
            instance.thumbnail = 'my_city_thumbnails/thumbnail_{}.png'.format(instance.id)
            instance.save_without_signals()
