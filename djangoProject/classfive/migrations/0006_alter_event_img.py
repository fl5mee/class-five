# Generated by Django 4.1.5 on 2023-07-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classfive', '0005_event_link_alter_event_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
    ]
