# Generated by Django 3.1.6 on 2021-02-16 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['order']},
        ),
    ]