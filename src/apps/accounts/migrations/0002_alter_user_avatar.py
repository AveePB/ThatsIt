# Generated by Django 5.1.1 on 2024-09-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(default=None, upload_to="avatars"),
        ),
    ]
