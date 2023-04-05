# Generated by Django 4.1.7 on 2023-04-02 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1042_remove_document_paid_alter_document_checksum"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="paid",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now, verbose_name="paid"
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="checksum",
            field=models.CharField(
                help_text="The checksum of the original document.",
                max_length=32,
                unique=True,
                verbose_name="checksum",
            ),
        ),
    ]