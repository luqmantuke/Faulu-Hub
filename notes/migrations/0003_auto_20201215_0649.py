# Generated by Django 3.1.4 on 2020-12-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20201215_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
