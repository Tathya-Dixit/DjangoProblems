# Generated by Django 5.1.7 on 2025-03-24 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='paid_amount',
            new_name='remaining_amount',
        ),
    ]
