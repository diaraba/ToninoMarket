# Generated by Django 5.0.1 on 2024-01-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0020_rename_approvisionnnement_approvisionnement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvisionnement',
            name='date_demande',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date de demande d'approvisionnement"),
        ),
    ]
