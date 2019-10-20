# Generated by Django 2.2.6 on 2019-10-20 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='manuscript',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='speech',
            name='speech2text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='speech',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='speech',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
