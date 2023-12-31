# Generated by Django 4.2 on 2023-05-29 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("s_admin", "0004_alter_feesettings_fee_type"),
        ("s_members", "0004_member_payment_status_member_registration_fees_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memberregistration",
            name="registration_fee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="s_admin.feesettings",
                verbose_name="Fee Name",
            ),
        ),
    ]
