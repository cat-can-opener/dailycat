# Generated by Django 3.1.7 on 2021-05-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_add_is_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='liked_counts',
            field=models.IntegerField(default=0),
        ),
    ]