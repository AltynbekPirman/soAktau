from django.db import models


class CityNews(models.Model):
    title_kaz = models.TextField(verbose_name='название(kaz)')
    title_rus = models.TextField(verbose_name='название(rus)')
    text_kaz = models.TextField(verbose_name='текст(kaz)')
    text_rus = models.TextField(verbose_name='текст(rus)')
    created_date = models.DateTimeField(auto_now_add=True)

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


class CityVideo(models.Model):
    url = models.URLField(max_length=150, verbose_name='видео')
    news = models.ForeignKey(CityNews, related_name='videos', null=True,
                             verbose_name='видео', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'видео'
        verbose_name = 'видео'
