# Generated by Django 4.0 on 2022-04-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_card_unique_active_ip_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='supported_course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]
