# Generated by Django 5.1 on 2024-08-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_zipcode_customuser_postal_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='IN', max_length=100),
        ),
    ]
