# Generated by Django 4.1.7 on 2023-04-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_alter_timetable_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]