# Generated by Django 3.0.6 on 2020-05-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200516_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinput',
            name='post_key',
            field=models.CharField(blank=True, default='ww589u', editable=False, max_length=6),
        ),
    ]