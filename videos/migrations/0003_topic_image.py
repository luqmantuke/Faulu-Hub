# Generated by Django 3.1.4 on 2021-02-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_topic_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(null=True, upload_to='videos'),
        ),
    ]