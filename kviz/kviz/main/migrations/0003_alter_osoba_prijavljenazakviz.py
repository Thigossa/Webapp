# Generated by Django 4.1.2 on 2023-02-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_odgovori_tocanodg_odgovori_tocan_odg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='PrijavljenaZaKviz',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.kviz'),
        ),
    ]
