# Generated by Django 4.2.5 on 2023-10-03 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskList_app', '0002_alter_profileimg_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileimg',
            options={'verbose_name': 'Profile Picture'},
        ),
        migrations.AlterModelTable(
            name='profileimg',
            table=None,
        ),
    ]
