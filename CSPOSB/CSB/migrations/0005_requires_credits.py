# Generated by Django 3.1.7 on 2021-04-15 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSB', '0004_auto_20210415_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='requires',
            name='credits',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
