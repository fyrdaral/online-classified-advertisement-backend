from django.db import models

from department import models as m_department
from user import models as user


class Advertisement(models.Model):
    like_new = '5'
    very_good_state = '4'
    good_condition = '3'
    worn = '2'
    poor_condition = '1'

    STATE_CHOICES = [
        (like_new, 'Like New'),
        (very_good_state, 'Very Good State'),
        (good_condition, 'Good Condition'),
        (worn, 'Worn'),
        (poor_condition, 'Poor Condition'),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True, null=True)

    department = models.ForeignKey(m_department.Department, on_delete=models.CASCADE)
    owner = models.ForeignKey(user.User, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    price = models.IntegerField(default=0)
    size = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(
        max_length=3,
        choices=STATE_CHOICES,
        default=good_condition,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_created']
