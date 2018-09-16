from django.db import models


class AbstractModel(models.Model):
    title = models.TextField(verbose_name='название')
    language = models.ForeignKey('main.Language', null=True, on_delete=models.SET_NULL, verbose_name='язык')

    def __str__(self):
        if len(self.title) > 100:
            return "{}...".format(self.title[:99])

        return self.title[:99]

    class Meta:
        abstract = True


class Service(AbstractModel):
    pass
    # many2one sub_services

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class SubService(AbstractModel):

    class Meta:
        verbose_name = "Суб-Услуги"
        verbose_name_plural = "Суб-Услуги"


class Post(AbstractModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sub_services', verbose_name='услуга')
    text = models.TextField(verbose_name="текст")
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='posts',
                                    verbose_name='cуб-услуга')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
