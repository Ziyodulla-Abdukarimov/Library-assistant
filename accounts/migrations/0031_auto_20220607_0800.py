# Generated by Django 3.2.12 on 2022-06-07 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_accept_book_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='adadi',
        ),
        migrations.RemoveField(
            model_name='book',
            name='city',
        ),
        migrations.RemoveField(
            model_name='book',
            name='nameda',
        ),
        migrations.RemoveField(
            model_name='book',
            name='numberda',
        ),
        migrations.RemoveField(
            model_name='book',
            name='section',
        ),
    ]
