# Generated by Django 5.1.7 on 2025-03-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="thumbnail",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
