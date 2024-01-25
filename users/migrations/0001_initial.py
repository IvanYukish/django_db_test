# Generated by Django 5.0.1 on 2024-01-25 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('salary', models.PositiveIntegerField()),
                ('sector', models.CharField(max_length=63)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department')),
            ],
        ),
    ]