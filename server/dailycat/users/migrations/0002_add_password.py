# Generated by Django 3.1.7 on 2021-04-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_add_users_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
