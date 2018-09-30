from django.db.models.signals import post_save
from django.dispatch import receiver
# from pusher import Pusher
import pusher

from news.models import Announcement

# pusher = Pusher(app_id=u'608147', key=u'd2f5272d79b0860da7bc', secret=u'647a7adeb738f42f20d6', cluster=u'ap2')

@receiver(post_save, sender=Announcement)
def notify_announcement(sender, instance: Announcement, **kwargs):
    if kwargs['created']:
        print(12)
        # pusher.notify(['hello'], {
        #     'apns': {
        #         'aps': {
        #             'alert': {
        #                 'body': 'atawa atawa'
        #             }
        #         }
        #     }
        # })

        pusher_client = pusher.Pusher(
            app_id='608147',
            key='d2f5272d79b0860da7bc',
            secret='647a7adeb738f42f20d6',
            cluster='ap2',
            # ssl=True
        )

        pusher_client.trigger('my-channel', 'my-event', {'message': '{}'.format(instance.text)})
