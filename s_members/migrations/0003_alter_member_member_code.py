# Generated by Django 4.2 on 2023-05-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("s_members", "0002_alter_member_created_by_alter_member_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="member_code",
            field=models.CharField(max_length=10, verbose_name="member_code"),
        ),
    ]
