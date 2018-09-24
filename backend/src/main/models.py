from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.code
