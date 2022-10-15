# Generated by Django 4.1.2 on 2022-10-15 01:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]