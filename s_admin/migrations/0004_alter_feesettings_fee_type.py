# Generated by Django 4.2 on 2023-05-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("s_admin", "0003_remove_rolepermissions_permission_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feesettings",
            name="fee_type",
            field=models.CharField(
                choices=[("ONLINE", "ONLINE"), ("OFFLINE", "OFFLINE")],
                default="ONLINE",
                verbose_name="Fee Mode",
            ),
        ),
    ]
