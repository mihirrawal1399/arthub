# Generated by Django 2.2.1 on 2019-07-07 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20180724_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='display_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='photo',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photographer',
            name='profile_pic',
            field=models.ImageField(default='default-profile.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='format',
            field=models.CharField(choices=[('PNG', 'PNG'), ('JPG', 'JPG'), ('JPEG', 'JPEG'), ('Exif', 'Exif'), ('TIF', 'TIF'), ('GIF', 'GIF'), ('WEBP', 'WEBP'), ('SVG', 'SVG')], max_length=20),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]