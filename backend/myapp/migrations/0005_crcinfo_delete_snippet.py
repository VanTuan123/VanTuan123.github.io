# Generated by Django 4.2 on 2023-06-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_rename_code_snippet_data_remove_snippet_language_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CRCInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, default="", max_length=100)),
                ("data", models.TextField()),
            ],
            options={"ordering": ["data"],},
        ),
        migrations.DeleteModel(name="Snippet",),
    ]
