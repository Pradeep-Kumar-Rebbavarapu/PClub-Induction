# Generated by Django 4.1.4 on 2023-02-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='descr',
            new_name='desc',
        ),
        migrations.AlterField(
            model_name='blog',
            name='datestamp',
            field=models.CharField(blank=True, default='23rd February 2023', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.CharField(blank='2:14:11 am', max_length=225, null=True),
        ),
    ]