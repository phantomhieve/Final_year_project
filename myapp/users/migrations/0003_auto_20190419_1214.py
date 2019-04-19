# Generated by Django 2.1.7 on 2019-04-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190320_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='u_name',
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='dob',
            field=models.DateField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=225, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]