# Generated by Django 4.2 on 2023-05-27 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("s_members", "0002_alter_member_created_by_alter_member_first_name_and_more"),
        ("s_admin", "0002_permissionsettings_alter_streets_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupSetting",
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
                    "group_code",
                    models.CharField(max_length=10, verbose_name="group_code"),
                ),
                (
                    "group_name",
                    models.CharField(max_length=50, verbose_name="group_name"),
                ),
                (
                    "group_description",
                    models.TextField(max_length=120, verbose_name="group_description"),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_on"),
                ),
                (
                    "updated_on",
                    models.DateTimeField(auto_now=True, verbose_name="updated_on"),
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
                "verbose_name": "GroupSetting",
                "verbose_name_plural": "GroupSettings",
            },
        ),
        migrations.CreateModel(
            name="GroupMembers",
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
                    "group_setting_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_group.groupsetting",
                    ),
                ),
                (
                    "member_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_members.member",
                    ),
                ),
            ],
            options={
                "verbose_name": "GroupMembers",
                "verbose_name_plural": "GroupMembers",
            },
        ),
        migrations.CreateModel(
            name="GroupMemberRole",
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
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_group.groupsetting",
                    ),
                ),
                (
                    "member_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_members.member",
                    ),
                ),
                (
                    "role_permission_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_admin.rolepermissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "GroupMemberRole",
                "verbose_name_plural": "GroupMemberRoles",
            },
        ),
    ]
