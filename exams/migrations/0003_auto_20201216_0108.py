# Generated by Django 3.1.4 on 2020-12-16 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_content_exams_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.form'),
        ),
        migrations.AlterField(
            model_name='content',
            name='subject',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='exams.subject'),
        ),
    ]
