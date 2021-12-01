from django.db import models

class Urls(models.Model):
    url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=30)

    def __str__(self):
        return self.url
