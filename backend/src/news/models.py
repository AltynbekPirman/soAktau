from django.db import models


class News(models.Model):

    title = models.TextField(verbose_name='название')
    text = models.TextField(verbose_name='текст')
    language = models.ForeignKey('main.Language', null=True, on_delete=models.SET_NULL, verbose_name='язык')
    created_date = models.DateTimeField(auto_now_add=True)
    photo_url = models.TextField(null=True, verbose_name='фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'


class Announcement(models.Model):
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
    question = models.TextField(verbose_name='вопрос')
    created_date = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey('main.Language', null=True, on_delete=models.SET_NULL, verbose_name='язык')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Answer(models.Model):
    text = models.TextField(verbose_name='ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос', related_name='answers')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
