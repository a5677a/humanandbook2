# Generated by Django 3.2.6 on 2021-08-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
