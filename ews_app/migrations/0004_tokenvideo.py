# Generated by Django 4.2 on 2023-06-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ews_app', '0003_roadmap_roadmapl1_roadmapl2_roadmapr1_roadmapr2'),
    ]

    operations = [
        migrations.CreateModel(
            name='tokenVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media/video', verbose_name='Video')),
            ],
        ),
    ]