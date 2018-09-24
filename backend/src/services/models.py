from django.db import models


class AbstractModel(models.Model):

    def __str__(self):
        if self.title:
            if len(self.title) > 100:
                return "{}...".format(self.title[:99])
            return self.title[:99]

    class Meta:
        abstract = True


class Service(AbstractModel):
    title = models.TextField(verbose_name='название', unique=True)
    language = models.ForeignKey('main.Language', null=True, on_delete=models.SET_NULL, verbose_name='язык')
    # many2one sub_services

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class SubService(AbstractModel):
    title = models.TextField(verbose_name='название', unique=True)

    class Meta:
        verbose_name = "Суб-Услуги"
        verbose_name_plural = "Суб-Услуги"


class Title(models.Model):
    name = models.TextField(verbose_name="текст", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Title"


class Post(AbstractModel):
    title = models.ForeignKey(Title, verbose_name='название', on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='posts', verbose_name='услуга')
    text = models.TextField(verbose_name="текст")
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='posts',
                                    verbose_name='cуб-услуга')

    def __str__(self):
        return self.title.name

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
