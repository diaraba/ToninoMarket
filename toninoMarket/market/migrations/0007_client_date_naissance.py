# Generated by Django 5.0.1 on 2024-01-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_alter_client_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_naissance',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date de naissance'),
        ),
    ]
