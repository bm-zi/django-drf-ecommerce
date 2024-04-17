# Generated by Django 5.0.3 on 2024-04-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Description",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
