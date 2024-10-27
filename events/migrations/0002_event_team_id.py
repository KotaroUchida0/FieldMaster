# Generated by Django 5.1.2 on 2024-10-27 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="team_id",
            field=models.ForeignKey(
                db_column="team_id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="teams.team",
                verbose_name="チーム",
            ),
        ),
    ]