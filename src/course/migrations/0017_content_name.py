# Generated by Django 3.2.13 on 2022-04-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_alter_card_is_counter_added_to_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
