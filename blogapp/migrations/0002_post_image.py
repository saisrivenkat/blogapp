# Generated by Django 3.0.6 on 2020-06-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='post_images'),
        ),
    ]
