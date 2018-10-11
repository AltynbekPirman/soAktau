from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.code


class CompanyInfo(models.Model):
    info_kaz = models.TextField()
    info_rus = models.TextField()

    def __str__(self):
        return self.info_rus

    class Meta:
        verbose_name_plural = 'О Компании'
        verbose_name = 'О Компании'


class Address(models.Model):
    email = models.EmailField()
    buses = models.CharField(max_length=256, verbose_name='автобусы')
    address_kaz = models.CharField(max_length=256, verbose_name='адрес(kaz)')
    address_rus = models.CharField(max_length=256, verbose_name='адрес(rus)')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'адрес'
        verbose_name = 'адрес'


class Coordinate(models.Model):
    longitude = models.DecimalField(verbose_name='долгота(карта)', max_digits=20, decimal_places=6)
    latitude = models.DecimalField(verbose_name='широта(карта)', max_digits=20, decimal_places=6)
    address = models.ForeignKey(Address, related_name='coordinates', null=True,
                                verbose_name='адрес', on_delete=models.SET_NULL)

    def __str__(self):
        return 'x: {}; y: {}'.format(self.longitude, self.latitude)

    class Meta:
        verbose_name_plural = 'координаты'
        verbose_name = 'координаты'


class Phone(models.Model):
    telephone = models.CharField(max_length=64, verbose_name='телефон')
    address = models.ForeignKey(Address, related_name='phones', null=True,
                                verbose_name='адрес', on_delete=models.SET_NULL)

    def __str__(self):
        return self.telephone

    @staticmethod
    def _extract_number(phone: str) -> str:
        res = ''
        for char in phone:
            if char.isdigit():
                res += char
        return res

    def _add_href_to_phone(self) -> None:
        tel_num = self._extract_number(self.telephone)
        self.telephone = '<a href="tel:{tel_num}">{tel}</a>'.format(tel_num=tel_num, tel=self.telephone)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self._add_href_to_phone()
        super().save()

    class Meta:
        verbose_name_plural = 'телефон'
        verbose_name = 'телефон'


class ChatRoom(models.Model):
    title_rus = models.CharField(max_length=512, verbose_name='Название чата(kaz)')
    title_kaz = models.CharField(max_length=512, verbose_name='Название чата(rus)')

    def __str__(self):
        return self.title_rus

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    message_kaz = models.TextField()
    message_rus = models.TextField()
