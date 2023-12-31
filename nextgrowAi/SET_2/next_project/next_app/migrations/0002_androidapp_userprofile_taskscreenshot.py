# Generated by Django 4.1.5 on 2023-07-31 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('next_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appname', models.CharField(max_length=100)),
                ('Applink', models.URLField()),
                ('App_category', models.CharField(choices=[('Entertaiment', 'Entertaiment'), ('Entertaiment2', 'Entertaiment2')], default='category1', max_length=50)),
                ('Sub_category', models.CharField(choices=[('Social_Media', 'Social_Media'), ('Social_Media1', 'Social_Media1')], default='sub_category1', max_length=50)),
                ('App_img', models.ImageField(upload_to='App_img/')),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('tasks_completed', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskScreenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_description', models.CharField(max_length=200)),
                ('screenshot_img', models.ImageField(upload_to='task_screenshots/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
