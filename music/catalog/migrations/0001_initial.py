# Generated by Django 3.2.3 on 2021-05-31 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True, help_text='Give some info about the artist', null=True)),
                ('song_total', models.IntegerField()),
                ('choices', models.TextField(choices=[('1', 'Choice 1'), ('2', 'Choice 2')])),
                ('favorite', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(upload_to='uploads')),
                ('download', models.FileField(upload_to='uploads')),
            ],
        ),
    ]
