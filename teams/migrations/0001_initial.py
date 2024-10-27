# Generated by Django 5.1.2 on 2024-10-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("team_name", models.CharField(max_length=100, verbose_name="チーム名")),
                (
                    "joined_datetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日"),
                ),
                (
                    "updated_datetime",
                    models.DateTimeField(auto_now=True, verbose_name="更新日時"),
                ),
            ],
            options={"db_table": "teams",},
        ),
    ]