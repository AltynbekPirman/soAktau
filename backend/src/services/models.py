from django.db import models


class AbstractModel(models.Model):

    def __str__(self):
        if self.title_rus:
            if len(self.title_rus) > 100:
                return "{}...".format(self.title_rus[:99])
            return self.title_rus[:99]

    class Meta:
        abstract = True


class Service(AbstractModel):
    title_kaz = models.TextField(verbose_name='название(kaz)', unique=True)
    title_rus = models.TextField(verbose_name='название(rus)', unique=True)
    # language = models.ForeignKey('main.Language', null=True, on_delete=models.SET_NULL, verbose_name='язык')
    # many2one sub_services

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class SubService(AbstractModel):
    title_kaz = models.TextField(verbose_name='название(kaz)', unique=True)
    title_rus = models.TextField(verbose_name='название(rus)', unique=True)

    class Meta:
        verbose_name = "Суб-Услуги"
        verbose_name_plural = "Суб-Услуги"


class Title(models.Model):
    name_kaz = models.TextField(verbose_name="название(kaz)", unique=True)
    name_rus = models.TextField(verbose_name="название(rus)", unique=True)

    def __str__(self):
        return self.name_rus

    class Meta:
        verbose_name = "Заглавие"
        verbose_name_plural = "Заглавие"


class Post(AbstractModel):

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='posts', verbose_name='услуга')
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='posts',
                                    verbose_name='cуб-услуга')
    title = models.ForeignKey(Title, verbose_name='заглавие', on_delete=models.CASCADE, related_name='posts')
    text_kaz = models.TextField(verbose_name="текст(kaz)")
    text_rus = models.TextField(verbose_name="текст(rus)")

    def __str__(self):
        return self.text_rus[:150]

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
