# Generated by Django 4.0.2 on 2022-02-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_fertilizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='fertilizers',
            field=models.ManyToManyField(to='main_app.Fertilizer'),
        ),
    ]
