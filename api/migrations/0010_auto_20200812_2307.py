# Generated by Django 3.0.8 on 2020-08-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200812_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='zupei_type',
            field=models.CharField(blank=True, default='', max_length=45, null=True),
        ),
    ]