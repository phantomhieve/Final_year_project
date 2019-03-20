# Generated by Django 2.1.7 on 2019-03-20 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime', '0003_auto_20190320_1936'),
        ('users', '0002_auto_20190320_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='edits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permanent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.permanent')),
                ('temporary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.temporary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.permanent')),
                ('public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.users')),
                ('special', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.special')),
            ],
        ),
        migrations.CreateModel(
            name='rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='views',
            unique_together={('user', 'anime')},
        ),
        migrations.AlterUniqueTogether(
            name='rates',
            unique_together={('user', 'anime')},
        ),
        migrations.AlterUniqueTogether(
            name='final',
            unique_together={('special', 'public', 'anime')},
        ),
        migrations.AlterUniqueTogether(
            name='edits',
            unique_together={('user', 'temporary', 'permanent')},
        ),
    ]
