# Generated by Django 4.1 on 2022-09-26 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_room_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-updated", "-created"]},
        ),
    ]
