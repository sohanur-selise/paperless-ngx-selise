# Generated by Django 4.1.7 on 2023-04-02 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1030_alter_paperlesstask_task_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="paid",
            field=models.DateTimeField(
                db_index=True, default=django.utils.timezone.now, verbose_name="paid"
            ),
        ),
    ]