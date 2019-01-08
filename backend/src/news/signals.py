from django.db.models.signals import post_save
from django.dispatch import receiver

from main.accessories import ThumbnailCreator
from news.models import Announcement, News
from pusher_push_notifications import PushNotifications
import news.pusher_data as pusher_data

pn_client = PushNotifications(
    instance_id=pusher_data.InstanceID,
    secret_key=pusher_data.Secret,
)


@receiver(post_save, sender=Announcement)
def notify_announcement(sender, instance: Announcement, **kwargs):
    if kwargs['created']:
        response = pn_client.publish(
            interests=[pusher_data.Interest_kaz],
            publish_body={'apns': {'aps': {'alert': instance.title_kaz, "sound": "bingbong.aiff"}},
                          'fcm': {'notification': {'title': instance.title_kaz, 'body': instance.text_kaz,
                                                   "sound": "default"}}}
        )

        response = pn_client.publish(
            interests=[pusher_data.Interest_rus],
            publish_body={'apns': {'aps': {'alert': instance.title_rus, "sound": "bingbong.aiff"}},
                          'fcm': {'notification': {'title': instance.title_rus, 'body': instance.text_rus,
                                                   "sound": "default"}}}
        )


@receiver(post_save, sender=Announcement)
def save_thumbnail_announcement(sender, instance: Announcement, **kwargs):
    if not instance.disable_signals:
        thumbnail_file = ThumbnailCreator.get_thumbnail(instance.icon.name)
        thumbnail_file.save('./media/announcement_thumbnails/thumbnail_{}.png'.format(instance.id), "PNG")
        instance.thumbnail = 'announcement_thumbnails/thumbnail_{}.png'.format(instance.id)
        instance.save_without_signals()


@receiver(post_save, sender=News)
def save_thumbnail_news(sender, instance: News, **kwargs):
    if not instance.disable_signals:
        thumbnail_file = ThumbnailCreator.get_thumbnail(instance.icon.name)
        thumbnail_file.save('./media/news_thumbnails/thumbnail_{}.png'.format(instance.id), "PNG")
        instance.thumbnail = 'news_thumbnails/thumbnail_{}.png'.format(instance.id)
        instance.save_without_signals()
