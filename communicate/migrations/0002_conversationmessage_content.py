# Generated by Django 4.1.7 on 2023-11-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("communicate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversationmessage",
            name="content",
            field=models.TextField(default=1),
        ),
    ]
