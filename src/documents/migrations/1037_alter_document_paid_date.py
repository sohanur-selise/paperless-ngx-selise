# Generated by Django 4.1.7 on 2023-04-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1036_alter_document_paid_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="paid_date",
            field=models.DateField(
                blank=True, db_index=True, null=True, verbose_name="paid_date"
            ),
        ),
    ]
