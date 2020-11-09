# Generated by Django 2.1b1 on 2018-07-24 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('format', models.CharField(choices=[('PNG', 'PNG'), ('JPG', 'JPG'), ('JPEG', 'JPEG'), ('Exif', 'Exif'), ('GIF', 'GIF'), ('WEBP', 'WEBP'), ('SVG', 'SVG')], max_length=20)),
                ('tags', models.CharField(max_length=250)),
                ('original_pic', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer_name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Photographer'),
        ),
        migrations.AddField(
            model_name='collection',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Photo'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
