# Generated by Django 3.0.3 on 2021-05-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
