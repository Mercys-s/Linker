# Generated by Django 4.1.2 on 2023-01-21 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название предмета')),
                ('full_title', models.CharField(blank=True, max_length=150, verbose_name='Полное название')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL Предмета')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Категория предмета',
                'verbose_name_plural': 'Категории предметов',
            },
        ),
        migrations.CreateModel(
            name='SubjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Название работы')),
                ('theme', models.CharField(blank=True, max_length=200, verbose_name='Тема')),
                ('docx_file', models.FileField(upload_to='', verbose_name='Docx Файл')),
                ('pdf_file', models.FileField(upload_to='', verbose_name='PDF Файл')),
                ('video', models.FileField(blank=True, upload_to='', verbose_name='Видео')),
                ('author', models.CharField(blank=True, max_length=30, verbose_name='Имя Автора')),
                ('note', models.TextField(blank=True, max_length=1000, verbose_name='Примечание')),
                ('slug', models.SlugField(max_length=40, unique=True, verbose_name='URL Работы')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workflow.subjectcategory', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Практическая/Лабораторная',
                'verbose_name_plural': 'Практические/Лабораторные',
            },
        ),
    ]
