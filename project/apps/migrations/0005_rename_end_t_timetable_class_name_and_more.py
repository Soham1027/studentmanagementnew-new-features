# Generated by Django 4.1.7 on 2023-04-04 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_timetable_date_t'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='end_t',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='class_t',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='section_t',
            new_name='section_name',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='start_t',
            new_name='start_time',
        ),
    ]