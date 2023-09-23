# Generated by Django 4.2.4 on 2023-09-22 22:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_tag_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF",
                image_field=None,
                max_length=7,
                samples=None,
                unique=True,
                verbose_name="Цвет",
            ),
        ),
    ]