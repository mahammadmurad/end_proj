# Generated by Django 4.1.7 on 2023-04-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_project_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
    ]