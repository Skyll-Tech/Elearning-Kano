# Generated by Django 5.1 on 2024-08-20 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_classe_alter_produit_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classe',
            old_name='nomClasse',
            new_name='nom_Classe',
        ),
    ]
