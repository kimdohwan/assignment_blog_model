# Generated by Django 2.0.6 on 2018-06-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='models.Post'),
        ),
    ]
