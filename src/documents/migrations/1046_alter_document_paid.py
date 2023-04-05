# Generated by Django 4.2 on 2023-04-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1045_alter_document_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="paid",
            field=models.DateTimeField(
                blank=True, db_index=True, null=True, verbose_name="paid"
            ),
        ),
    ]