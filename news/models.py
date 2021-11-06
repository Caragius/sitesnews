from django.db import models




class Artical(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField("anons", max_length=250)
    full_text = models.TextField("State")
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"