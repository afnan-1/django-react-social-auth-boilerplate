# Generated by Django 3.2 on 2021-04-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]