# Generated by Django 4.0.4 on 2022-05-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publisher',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[('Bullet', 'Bullet'), ('Food', 'Food'), ('Travel', 'Travel'), ('Sport', 'Sport')], max_length=255),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]