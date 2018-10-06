from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import Announcement
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
            publish_body={'apns': {'aps': {'alert': instance.title_kaz}},
                          'fcm': {'notification': {'title': instance.title_kaz, 'body': instance.text_kaz}}}
        )

        response = pn_client.publish(
            interests=[pusher_data.Interest_rus],
            publish_body={'apns': {'aps': {'alert': instance.title_rus}},
                          'fcm': {'notification': {'title': instance.title_rus, 'body': instance.text_rus}}}
        )
