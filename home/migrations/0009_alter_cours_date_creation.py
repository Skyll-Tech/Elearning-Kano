# Generated by Django 5.1 on 2024-09-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_cours_temps_cours_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='Date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
