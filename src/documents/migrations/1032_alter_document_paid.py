# Generated by Django 4.1.7 on 2023-04-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1031_document_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="paid",
            field=models.DateTimeField(
                auto_now=True, db_index=True, verbose_name="paid"
            ),
        ),
    ]
