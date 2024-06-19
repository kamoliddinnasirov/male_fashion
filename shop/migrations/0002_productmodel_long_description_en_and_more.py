# Generated by Django 5.0.6 on 2024-06-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='long_description_en',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_ru',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_uz',
            field=models.TextField(null=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_en',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='short description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=60, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=60, null=True, verbose_name='title'),
        ),
    ]
