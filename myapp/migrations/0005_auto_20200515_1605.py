# Generated by Django 3.0.6 on 2020-05-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200515_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinput',
            name='post_key',
            field=models.CharField(blank=True, default='rpsems', editable=False, max_length=6, unique=True),
        ),
    ]
