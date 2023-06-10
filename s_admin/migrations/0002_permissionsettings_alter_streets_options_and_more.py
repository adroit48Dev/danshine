# Generated by Django 4.2 on 2023-05-27 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("s_admin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PermissionSettings",
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
                (
                    "permission_name",
                    models.CharField(max_length=50, verbose_name="Permission Name"),
                ),
                (
                    "permission_description",
                    models.TextField(
                        max_length=150, verbose_name="Permission Description"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="created on"),
                ),
                (
                    "updated_on",
                    models.DateTimeField(auto_now=True, verbose_name="updated on"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ACTIVE", "ACTIVE"),
                            ("INACTIVE", "INACTIVE"),
                            ("PENDING", "PENDING"),
                            ("DELETED", "DELETED"),
                        ],
                        default="ACTIVE",
                        verbose_name="status",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "PermissionSettings",
                "verbose_name_plural": "PermissionSettings",
            },
        ),
        migrations.AlterModelOptions(
            name="streets",
            options={"verbose_name": "Streets", "verbose_name_plural": "Streets"},
        ),
        migrations.AlterField(
            model_name="area",
            name="area_code",
            field=models.CharField(max_length=50, verbose_name="area code"),
        ),
        migrations.AlterField(
            model_name="area",
            name="area_description",
            field=models.TextField(verbose_name="area description"),
        ),
        migrations.AlterField(
            model_name="area",
            name="area_name",
            field=models.CharField(max_length=50, verbose_name="area name"),
        ),
        migrations.AlterField(
            model_name="area",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="area",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, verbose_name="updated on"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_description",
            field=models.TextField(verbose_name="fee description"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_frequency_unit",
            field=models.CharField(
                choices=[
                    ("ONETIME", "ONETIME"),
                    ("DAYS", "DAYS"),
                    ("MONTHS", "MONTHS"),
                    ("YEARS", "YEARS"),
                ],
                verbose_name="fee frequency unit",
            ),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_frequency_value",
            field=models.IntegerField(max_length=3, verbose_name="fee frequency value"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_name",
            field=models.CharField(max_length=50, verbose_name="fee name"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_type",
            field=models.CharField(max_length=50, verbose_name="fee type"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_unit",
            field=models.CharField(
                choices=[("FLAT", "FLAT"), ("PERCENTAGE", "PERCENTAGE")],
                verbose_name="fee unit",
            ),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="fee_value",
            field=models.IntegerField(max_length=5, verbose_name="fee value"),
        ),
        migrations.AlterField(
            model_name="feesettings",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, verbose_name="updated on"),
        ),
        migrations.AlterField(
            model_name="streets",
            name="street_description",
            field=models.CharField(max_length=100, verbose_name="street description"),
        ),
        migrations.AlterField(
            model_name="streets",
            name="street_name",
            field=models.CharField(max_length=50, verbose_name="stree name"),
        ),
        migrations.AlterField(
            model_name="streets",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, verbose_name="updated on"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, verbose_name="updated on"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="zone_code",
            field=models.CharField(max_length=6, verbose_name="zone code"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="zone_description",
            field=models.TextField(max_length=80, verbose_name="zone description"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="zone_name",
            field=models.CharField(max_length=50, verbose_name="zone name"),
        ),
        migrations.AlterField(
            model_name="zonegroup",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="zonegroup",
            name="group_description",
            field=models.TextField(verbose_name="zone group description"),
        ),
        migrations.AlterField(
            model_name="zonegroup",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, verbose_name="updated on"),
        ),
        migrations.CreateModel(
            name="RoleSettings",
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
                (
                    "role_name",
                    models.CharField(max_length=50, verbose_name="role name"),
                ),
                (
                    "role_description",
                    models.TextField(max_length=150, verbose_name="role description"),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="created on"),
                ),
                (
                    "updated_on",
                    models.DateTimeField(auto_now=True, verbose_name="updated on"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ACTIVE", "ACTIVE"),
                            ("INACTIVE", "INACTIVE"),
                            ("PENDING", "PENDING"),
                            ("DELETED", "DELETED"),
                        ],
                        default="ACTIVE",
                        verbose_name="status",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "RoleSetting",
                "verbose_name_plural": "RoleSettings",
            },
        ),
        migrations.CreateModel(
            name="RolePermissions",
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
                (
                    "permission_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_admin.permissionsettings",
                    ),
                ),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_admin.rolesettings",
                    ),
                ),
            ],
            options={
                "verbose_name": "RolePermissions",
                "verbose_name_plural": "RolePermissions",
            },
        ),
    ]
