# Generated by Django 2.2.11 on 2020-03-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('user_type', 'user_id'), name='unique_id_by_type'),
        ),
    ]
