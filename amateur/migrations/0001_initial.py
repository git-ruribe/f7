# Generated by Django 2.0.3 on 2018-03-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]