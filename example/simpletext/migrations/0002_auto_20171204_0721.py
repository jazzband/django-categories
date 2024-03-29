# Generated by Django 1.10.5 on 2017-12-04 07:21
from __future__ import unicode_literals

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0002_auto_20170217_1111"),
        ("simpletext", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="simplecategory",
            managers=[
                ("tree", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="simpletext",
            name="categories",
            field=models.ManyToManyField(blank=True, related_name="m2mcats", to="categories.Category"),
        ),
        migrations.AddField(
            model_name="simpletext",
            name="primary_category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="categories.Category"
            ),
        ),
        migrations.AddField(
            model_name="simpletext",
            name="secondary_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="simpletext_sec_cat",
                to="categories.Category",
            ),
        ),
    ]
