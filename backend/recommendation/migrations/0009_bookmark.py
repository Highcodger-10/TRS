# Generated by Django 4.1.7 on 2023-03-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0008_remove_rating_feedback_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(default='', max_length=300)),
                ('user', models.CharField(default='', max_length=300)),
            ],
        ),
    ]