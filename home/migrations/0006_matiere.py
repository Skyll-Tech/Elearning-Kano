# Generated by Django 5.1 on 2024-09-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_professeur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_matiere', models.CharField(max_length=50)),
            ],
        ),
    ]
