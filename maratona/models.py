from django.db import models

class Class(models.Model):
    objects = None
    description = models.CharField(max_length=255, verbose_name='descrição')
    tutor = models.CharField(max_length=30, verbose_name='tutor')
    date = models.DateField(verbose_name='data')
    url = models.CharField(max_length=255, verbose_name='url', null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'aula'