# Generated by Django 3.0.4 on 2020-04-26 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
