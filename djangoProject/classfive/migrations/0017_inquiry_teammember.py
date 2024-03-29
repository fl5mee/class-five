# Generated by Django 4.2.4 on 2023-10-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classfive', '0016_alter_slide_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('inquiry_type', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name (what you want this event to be called in the admin interface)')),
                ('title', models.TextField()),
                ('desc', models.TextField(verbose_name='description')),
                ('img', models.ImageField(upload_to='images/', verbose_name='image')),
            ],
        ),
    ]
