# Generated by Django 4.0.5 on 2022-07-01 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_delete_experience'),
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.country', verbose_name='Страна'),
        ),
        migrations.CreateModel(
            name='UserSoft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True, verbose_name='Оценка')),
                ('soft_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.softskill', verbose_name='Гибкий навык')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Гибкий навык пользователя',
                'verbose_name_plural': 'Гибкие навыки пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserHard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0, null=True, verbose_name='Оценка')),
                ('answers_url', models.CharField(blank=True, default='', max_length=256, verbose_name='Ссылка на ответы')),
                ('hard_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.hardskill', verbose_name='Проф навык')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Проф навык пользователя',
                'verbose_name_plural': 'Проф навыки пользователя',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('company_name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата конца')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыты работы',
            },
        ),
    ]