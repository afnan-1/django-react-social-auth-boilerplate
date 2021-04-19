# Generated by Django 3.2 on 2021-04-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='picture',
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
