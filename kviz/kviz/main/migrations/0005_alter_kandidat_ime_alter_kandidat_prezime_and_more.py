# Generated by Django 4.1.4 on 2023-02-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_kandidat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidat',
            name='ime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='kandidat',
            name='prezime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='ime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='prezime',
            field=models.CharField(max_length=50),
        ),
    ]
