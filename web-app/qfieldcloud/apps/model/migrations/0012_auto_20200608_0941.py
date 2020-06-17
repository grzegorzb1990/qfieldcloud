# Generated by Django 2.2.6 on 2020-06-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_delta_deltafile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deltafile',
            name='is_applied',
        ),
        migrations.AddField(
            model_name='deltafile',
            name='file',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deltafile',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'waiting'), (3, 'busy'), (4, 'applied'), (5, 'applied_with_conflicts'), (6, 'error')], default=1),
        ),
        migrations.AddField(
            model_name='deltafile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
