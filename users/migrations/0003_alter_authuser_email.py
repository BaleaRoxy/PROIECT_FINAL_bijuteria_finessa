# Generated by Django 3.2.9 on 2022-03-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email'),
        ),
    ]
