# Generated by Django 4.2 on 2023-06-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_crcinfo_delete_snippet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crcinfo", name="data", field=models.TextField(default=""),
        ),
    ]
