# Generated by Django 4.0.5 on 2022-06-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_userphoto_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
