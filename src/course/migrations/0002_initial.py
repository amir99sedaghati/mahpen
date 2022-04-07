# Generated by Django 4.0 on 2022-03-29 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user_management.user'),
        ),
        migrations.AddField(
            model_name='content',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_comment', to='course.commnet'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='course.commnet'),
        ),
        migrations.AddField(
            model_name='commnet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user_management.user'),
        ),
        migrations.AddField(
            model_name='card',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.user'),
        ),
    ]
