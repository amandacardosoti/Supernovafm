# Generated by Django 3.2.4 on 2021-06-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210614_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='carrossel',
            field=models.BooleanField(default=False),
        ),
    ]
