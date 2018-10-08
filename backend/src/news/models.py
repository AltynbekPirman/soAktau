from django.db import models


class News(models.Model):
    icon = models.ImageField(upload_to='news_images')
    title_kaz = models.TextField(verbose_name='название(kaz)')
    title_rus = models.TextField(verbose_name='название(rus)')
    text_kaz = models.TextField(verbose_name='текст(kaz)')
    text_rus = models.TextField(verbose_name='текст(rus)')
    created_date = models.DateTimeField(auto_now_add=True)

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
