# Generated by Django 4.0 on 2022-02-11 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_card_is_finished_alter_card_is_paid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pay',
        ),
    ]
