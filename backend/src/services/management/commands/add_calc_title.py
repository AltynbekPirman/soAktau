from django.core.management.base import BaseCommand
from django.db import IntegrityError

from services.models import Title, SubService, Service, Post


class Command(BaseCommand):

    help = "Whatever you want to print here"

    def execute(self, *args, **options):
        try:
            calc_service = Service.objects.get(
                title_rus__icontains='Назначение государственной адресной социальной помощи')
        except Service.DoesNotExist:
            calc_service = Service.objects.create(
                title_rus='Назначение государственной адресной социальной помощи (АСП)',
                title_kaz='Мемлекеттік атаулы әлеуметтік көмек (АӘК) тағайындау',
                icon='media/icon.png'
            )

        try:
            dummy_title = Title.objects.get(
                name_rus__icontains='Об услуге')
        except Service.DoesNotExist:
            dummy_title = Title.objects.create(
                name_rus='Об услуге',
                name_kaz='Қызмет жайында',
            )

        try:
            calc_sub_service = SubService.objects.get(code='calc')
        except Title.DoesNotExist:
            calc_sub_service = SubService.objects.create(
                title_rus='calculator',
                title_kaz='calculator',
                code='calc'
            )

        try:
            Post.objects.create(
                service=calc_service, sub_service=calc_sub_service, title=dummy_title,
                text_kaz='some dummy text', text_rus='some dummy text',
            )
        except Exception as e:
            print(e)
