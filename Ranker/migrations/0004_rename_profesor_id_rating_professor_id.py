# Generated by Django 4.0.3 on 2022-03-16 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranker', '0003_rename_proffesor_id_rating_profesor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='profesor_id',
            new_name='professor_id',
        ),
    ]