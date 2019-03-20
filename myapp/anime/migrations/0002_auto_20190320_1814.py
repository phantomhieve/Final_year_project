# Generated by Django 2.1.7 on 2019-03-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='has_genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.genre')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='has_genre',
            unique_together={('anime', 'genre')},
        ),
    ]
