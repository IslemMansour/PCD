# Generated by Django 3.2.16 on 2023-03-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_etudiant_room_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='room_member',
        ),
    ]
