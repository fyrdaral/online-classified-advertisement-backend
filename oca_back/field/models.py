from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True, null=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class IntegerField(Field):
    pass


class BooleanField(Field):
    pass


class CharField(Field):
    pass
