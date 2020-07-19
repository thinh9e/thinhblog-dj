# Generated by Django 3.0.8 on 2020-07-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0028_remove_setting_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='badge_class',
            field=models.CharField(choices=[('1', 'primary'), ('2', 'secondary'), ('3', 'success'), ('4', 'danger'), ('5', 'warning'), ('6', 'info'), ('7', 'light'), ('8', 'dark')], default=('8', 'dark'), max_length=1),
        ),
    ]
