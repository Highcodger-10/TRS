# Generated by Django 4.1.7 on 2023-03-09 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_rename_destination_saverecommendation_recommendations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saverecommendation',
            old_name='total_budget',
            new_name='budget',
        ),
    ]
