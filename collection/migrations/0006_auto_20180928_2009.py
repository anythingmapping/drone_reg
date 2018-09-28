# Generated by Django 2.1.1 on 2018-09-28 20:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0005_drone_associated_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='user',
            field=models.ForeignKey(default=5555, on_delete=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drone',
            name='user',
            field=models.ForeignKey(default=5555555555555555, on_delete=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
