# Generated by Django 2.1.1 on 2018-09-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('brand', models.CharField(choices=[('hero3', 'hero3'), ('12MP', '12MP'), ('gopro', 'gopro')], max_length=1)),
                ('megapixel', models.IntegerField()),
            ],
        ),
    ]
