# Generated by Django 3.2.13 on 2022-04-25 17:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220425_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
