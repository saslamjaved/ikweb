# Generated by Django 5.1 on 2024-08-26 15:47

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('description', models.TextField()),
                ('video_link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
            ],
        ),
    ]