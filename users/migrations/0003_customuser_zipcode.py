# Generated by Django 5.1 on 2024-08-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_city_customuser_country_customuser_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='zipcode',
            field=models.TextField(blank=True, null=True),
        ),
    ]
