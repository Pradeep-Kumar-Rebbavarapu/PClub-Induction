# Generated by Django 4.1.4 on 2023-02-16 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.CharField(blank=True, default='1:09:35 am', max_length=225, null=True),
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default=None, null=True)),
                ('parent_name', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('parent_comment', models.TextField(blank=True, default=None, null=True)),
                ('datestamp', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('timestamp', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.blogcomment')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
