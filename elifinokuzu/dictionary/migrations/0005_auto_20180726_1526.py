# Generated by Django 2.0.7 on 2018-07-26 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_edge_resorurce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edge',
            old_name='resorurce',
            new_name='resource',
        ),
    ]
