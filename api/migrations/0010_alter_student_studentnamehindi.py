# Generated by Django 3.2.7 on 2021-10-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20211011_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudentNameHindi',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]