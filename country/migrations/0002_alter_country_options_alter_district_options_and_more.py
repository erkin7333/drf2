# Generated by Django 4.0.4 on 2022-04-29 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Davlat', 'verbose_name_plural': 'Davlatlar'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Tuman', 'verbose_name_plural': 'Tumanlar'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Viloyat', 'verbose_name_plural': 'Viloyatlar'},
        ),
    ]
