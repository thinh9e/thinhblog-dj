# Generated by Django 3.0.7 on 2020-06-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_auto_20200621_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='Cập nhật'),
        ),
    ]
