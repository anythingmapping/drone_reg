# Generated by Django 2.1.1 on 2018-09-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_camera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='brand',
            field=models.CharField(choices=[('hero3', 'hero3'), ('12MP', '12MP'), ('gopro', 'gopro')], max_length=21),
        ),
    ]