# Generated by Django 3.2.4 on 2021-08-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
