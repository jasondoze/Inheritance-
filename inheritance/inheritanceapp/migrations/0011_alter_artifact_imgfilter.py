# Generated by Django 4.0 on 2022-01-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritanceapp', '0010_artifact_imgfilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='imgfilter',
            field=models.CharField(default='', max_length=500),
        ),
    ]