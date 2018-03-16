# Generated by Django 2.0.2 on 2018-03-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.EmailField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('created_data', models.DateTimeField()),
                ('email_confirm_key', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Данные пользователей',
                'verbose_name': 'Данные пользователя',
            },
        ),
    ]
