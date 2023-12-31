# Generated by Django 4.2 on 2023-06-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ews_app', '0002_rename_newletter_news_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=77)),
                ('speech', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapL1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hone', models.CharField(max_length=77)),
                ('h_two', models.CharField(blank=True, max_length=77, null=True)),
                ('h_three', models.CharField(blank=True, max_length=77, null=True)),
                ('h_four', models.CharField(blank=True, max_length=77, null=True)),
                ('h_five', models.CharField(blank=True, max_length=77, null=True)),
                ('h_six', models.CharField(blank=True, max_length=77, null=True)),
                ('Quarter', models.CharField(max_length=3)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapL2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hone', models.CharField(max_length=77)),
                ('h_two', models.CharField(blank=True, max_length=77, null=True)),
                ('h_three', models.CharField(blank=True, max_length=77, null=True)),
                ('h_four', models.CharField(blank=True, max_length=77, null=True)),
                ('h_five', models.CharField(blank=True, max_length=77, null=True)),
                ('h_six', models.CharField(blank=True, max_length=77, null=True)),
                ('Quarter', models.CharField(max_length=3)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapR1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hone', models.CharField(max_length=77)),
                ('h_two', models.CharField(blank=True, max_length=77, null=True)),
                ('h_three', models.CharField(blank=True, max_length=77, null=True)),
                ('h_four', models.CharField(blank=True, max_length=77, null=True)),
                ('h_five', models.CharField(blank=True, max_length=77, null=True)),
                ('h_six', models.CharField(blank=True, max_length=77, null=True)),
                ('Quarter', models.CharField(max_length=3)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapR2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hone', models.CharField(max_length=77)),
                ('h_two', models.CharField(blank=True, max_length=77, null=True)),
                ('h_three', models.CharField(blank=True, max_length=77, null=True)),
                ('h_four', models.CharField(blank=True, max_length=77, null=True)),
                ('h_five', models.CharField(blank=True, max_length=77, null=True)),
                ('h_six', models.CharField(blank=True, max_length=77, null=True)),
                ('Quarter', models.CharField(max_length=3)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
    ]
