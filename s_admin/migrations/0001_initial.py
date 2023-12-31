# Generated by Django 4.2 on 2023-05-08 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=150, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="is staff"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="is active"),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Area",
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
                    "area_name",
                    models.CharField(max_length=50, verbose_name="area_name"),
                ),
                (
                    "area_code",
                    models.CharField(max_length=50, verbose_name="area_code"),
                ),
                ("pincode", models.IntegerField(max_length=6, verbose_name="pincode")),
                ("area_description", models.TextField(verbose_name="area_description")),
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
                "verbose_name": "Area",
                "verbose_name_plural": "Areas",
            },
        ),
        migrations.CreateModel(
            name="Zone",
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
                    "zone_name",
                    models.CharField(max_length=50, verbose_name="zone_name"),
                ),
                ("zone_code", models.CharField(max_length=6, verbose_name="")),
                (
                    "zone_description",
                    models.TextField(max_length=80, verbose_name="zone_description"),
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
                "verbose_name": "Zone",
                "verbose_name_plural": "Zones",
            },
        ),
        migrations.CreateModel(
            name="ZoneGroup",
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
                    "group_description",
                    models.TextField(verbose_name="zone_grp_description"),
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
                    "area_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_admin.area",
                        verbose_name="area",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "zone_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="s_admin.zone",
                        verbose_name="zone",
                    ),
                ),
            ],
            options={
                "verbose_name": "ZoneGroup",
                "verbose_name_plural": "ZoneGroups",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("first_name", models.CharField(max_length=100, null=True)),
                ("last_name", models.CharField(max_length=100, null=True)),
                (
                    "intials",
                    models.CharField(
                        choices=[("MR", "MR"), ("MRS", "MRS"), ("MISS", "MISS")],
                        default="MRS",
                        null=True,
                        verbose_name="initials",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "MALE"), ("F", "FEMALE"), ("O", "OTHERS")],
                        default="F",
                        null=True,
                        verbose_name="gender",
                    ),
                ),
                (
                    "dob",
                    models.DateField(
                        blank=True,
                        max_length=8,
                        null=True,
                        verbose_name="date of birth",
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        null=True,
                        upload_to="media/user_files/",
                        verbose_name="Profile picture",
                    ),
                ),
                (
                    "employee_id",
                    models.CharField(
                        editable=False,
                        max_length=10,
                        unique=True,
                        verbose_name="employee id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
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
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "UserProfile",
                "verbose_name_plural": "UserProfiles",
            },
        ),
        migrations.CreateModel(
            name="Streets",
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
                    "street_name",
                    models.CharField(max_length=50, verbose_name="stree_name"),
                ),
                (
                    "street_description",
                    models.CharField(max_length=100, verbose_name="street_description"),
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
                "verbose_name": "Streets",
                "verbose_name_plural": "Streetss",
            },
        ),
        migrations.CreateModel(
            name="OrganizationSetting",
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
                    "organization_name",
                    models.CharField(max_length=50, verbose_name="organization_name"),
                ),
                ("org_code", models.CharField(max_length=10, verbose_name="org_code")),
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
                "verbose_name": "OrganizationSetting",
                "verbose_name_plural": "OrganizationSettings",
            },
        ),
        migrations.CreateModel(
            name="FeeSettings",
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
                ("fee_name", models.CharField(max_length=50, verbose_name="fee_name")),
                ("fee_description", models.TextField(verbose_name="fee_description")),
                ("fee_type", models.CharField(max_length=50, verbose_name="fee_type")),
                (
                    "fee_value",
                    models.IntegerField(max_length=5, verbose_name="fee_value"),
                ),
                (
                    "fee_unit",
                    models.CharField(
                        choices=[("FLAT", "FLAT"), ("PERCENTAGE", "PERCENTAGE")],
                        verbose_name="fee_unit",
                    ),
                ),
                (
                    "fee_frequency_value",
                    models.IntegerField(
                        max_length=3, verbose_name="fee_frequency_value"
                    ),
                ),
                (
                    "fee_frequency_unit",
                    models.CharField(
                        choices=[
                            ("ONETIME", "ONETIME"),
                            ("DAYS", "DAYS"),
                            ("MONTHS", "MONTHS"),
                            ("YEARS", "YEARS"),
                        ],
                        verbose_name="fee_frequency_unit",
                    ),
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
                "verbose_name": "FeeSettings",
                "verbose_name_plural": "FeeSettingss",
            },
        ),
    ]
