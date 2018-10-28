from PIL import Image
from django.db import models


class CityNews(models.Model):
    title_kaz = models.TextField(verbose_name='название(kaz)')
    title_rus = models.TextField(verbose_name='название(rus)')
    text_kaz = models.TextField(verbose_name='текст(kaz)')
    text_rus = models.TextField(verbose_name='текст(rus)')
    created_date = models.DateTimeField(auto_now_add=True)
    video_url = models.URLField(max_length=150, verbose_name='видео', null=True, blank=True)
    video_screenshot = models.ImageField(upload_to='my_city_video_screens', verbose_name='скриншот видео',
                                         null=True, blank=True)
    view_count = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='my_city_thumbnails', null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_signals = False

    def save_without_signals(self):
        """
        This allows for updating the model from code running inside post_save()
        signals without going into an infinite loop:
        """
        self.disable_signals = True
        self.save()
        self.disable_signals = False


    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save()
    #     if self.images.all():
    #         thumbnail_file = self._get_thumbnail(self.images.all()[0].icon.url)
    #         thumbnail_file.save('backend/src/mediamy_city_thumbnails/thumbnail_{}.png'.format(self.id), "PNG")
    #         self.thumbnail = 'my_city_thumbnails/thumbnail_{}.png'.format(self.id)
    #     elif self.video_screenshot:
    #         thumbnail_file = self._get_thumbnail(self.video_screenshot.url)
    #         thumbnail_file.save('backend/src/media/my_city_thumbnails/thumbnail_{}.png'.format(self.id), "PNG")
    #         self.thumbnail = 'my_city_thumbnails/thumbnail_{}.png'.format(self.id)
    #     super().save()

    @staticmethod
    def _get_thumbnail(image_location):
        image = Image.open('./backend/src{}'.format(image_location))
        thumbnail = image.resize([60, 60], Image.ANTIALIAS)
        return thumbnail

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name_plural = 'Мой Город'
        verbose_name = 'Мой Город'


class CityImage(models.Model):
    icon = models.ImageField(upload_to='my_city_images', verbose_name='изображение')
    news = models.ForeignKey(CityNews, related_name='images', null=True,
                             verbose_name='изображение', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'изображения'
        verbose_name = 'изображение'
