# Generated by Django 2.0.1 on 2018-02-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Season',
            new_name='Period',
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'Period', 'verbose_name_plural': 'Periods'},
        ),
        migrations.RenameField(
            model_name='contentatom',
            old_name='seasons',
            new_name='periods',
        ),
        migrations.RenameField(
            model_name='memoir',
            old_name='season',
            new_name='period',
        ),
    ]
