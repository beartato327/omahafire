# Generated by Django 2.2.6 on 2019-10-10 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'permissions': (('view_restricted_document', 'can view restricted documents'),)},
        ),
    ]
