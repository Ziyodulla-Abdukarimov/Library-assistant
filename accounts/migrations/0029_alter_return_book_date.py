# Generated by Django 3.2.12 on 2022-06-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_remove_check_respite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return_book',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='olingan vaqti'),
        ),
    ]
