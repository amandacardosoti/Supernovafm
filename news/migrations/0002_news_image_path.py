# Generated by Django 3.2.4 on 2021-06-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]