# Generated by Django 2.2.1 on 2020-02-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0003_employees_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
