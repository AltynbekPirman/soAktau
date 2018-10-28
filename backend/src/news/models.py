from PIL import Image
from django.db import models


def get_thumbnail(image_location):
    image = Image.open('./backend/src{}'.format(image_location))
    thumbnail = image.resize([60, 60], Image.ANTIALIAS)
    return thumbnail


class News(models.Model):
    icon = models.ImageField(upload_to='news_images')
    title_kaz = models.TextField(verbose_name='название(kaz)')
    title_rus = models.TextField(verbose_name='название(rus)')
    text_kaz = models.TextField(verbose_name='текст(kaz)')
    text_rus = models.TextField(verbose_name='текст(rus)')
    is_main = models.BooleanField(default=False, verbose_name='на главную')
    created_date = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='news_thumbnails', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        thumbnail_file = get_thumbnail(self.icon.url)
        thumbnail_file.save('backend/src/media/news_thumbnails/thumbnail_{}.png'.format(self.id), "PNG")
        self.thumbnail = 'news_thumbnails/thumbnail_{}.png'.format(self.id)
        super().save()

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'


class Announcement(models.Model):
    icon = models.ImageField(upload_to='notif_images')
    title_kaz = models.TextField(verbose_name='название(kaz)')
    title_rus = models.TextField(verbose_name='название(rus)')
    text_kaz = models.TextField(verbose_name='текст(kaz)')
    text_rus = models.TextField(verbose_name='текст(rus)')
    created_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='announcement_thumbnails', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        thumbnail_file = get_thumbnail(self.icon.url)
        thumbnail_file.save('backend/src/media/announcement_thumbnails/thumbnail_{}.png'.format(self.id), "PNG")
        self.thumbnail = 'announcement_thumbnails/thumbnail_{}.png'.format(self.id)
        super().save()

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name_plural = 'уведомления'
        verbose_name = 'уведомление'


class Question(models.Model):
    question_kaz = models.TextField(verbose_name='вопрос(kaz)')
    question_rus = models.TextField(verbose_name='вопрос(rus)')
    answer_kaz = models.TextField(verbose_name='ответ(kaz)')
    answer_rus = models.TextField(verbose_name='ответ(rus)')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_rus

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
