# Generated by Django 3.2.3 on 2021-06-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='choices',
            field=models.TextField(blank=True, choices=[('1', 'Choice 1'), ('2', 'Choice 2')], null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='download',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='song_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]