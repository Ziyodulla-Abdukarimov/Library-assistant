# Generated by Django 3.2.12 on 2022-05-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_return_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept_book',
            name='author',
            field=models.CharField(default=1, max_length=100, verbose_name='Муаллифи'),
            preserve_default=False,
        ),
    ]
