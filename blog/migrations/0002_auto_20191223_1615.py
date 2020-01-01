# Generated by Django 2.2.8 on 2019-12-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'ブログ', 'verbose_name_plural': 'ブログ'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, verbose_name='タイトル'),
        ),
    ]