# Generated by Django 2.1 on 2018-08-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20180813_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='relation',
            new_name='r',
        ),
    ]
