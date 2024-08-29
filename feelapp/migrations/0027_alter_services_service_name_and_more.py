# Generated by Django 4.1.9 on 2024-08-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feelapp", "0026_brandandproduct_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="service_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="services",
            unique_together={
                ("categories", "subcategory", "childcategory", "service_name")
            },
        ),
    ]
