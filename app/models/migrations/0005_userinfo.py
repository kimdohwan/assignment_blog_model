# Generated by Django 2.0.6 on 2018-06-19 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_auto_20180619_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_relations', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='models.User')),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
