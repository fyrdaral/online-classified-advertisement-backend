from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True, null=True)
    order = models.IntegerField(default=1)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
