# Generated by Django 5.1.2 on 2024-10-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_customuser_name_alter_customuser_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="bat_throw",
            field=models.CharField(
                choices=[
                    ("RR", "右投げ右打ち"),
                    ("RL", "右投げ左打ち"),
                    ("LR", "左投げ右打ち"),
                    ("LL", "左投げ左打ち"),
                ],
                max_length=2,
                verbose_name="投打",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="position",
            field=models.CharField(
                choices=[("P", "ピッチャー"), ("C", "キャッチャー"), ("IF", "内野手"), ("OF", "外野手")],
                max_length=50,
                verbose_name="ポジション",
            ),
        ),
    ]
