# Generated by Django 2.0.8 on 2018-11-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]