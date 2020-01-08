from django.db import models


class Demo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
