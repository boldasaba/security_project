# Generated by Django 4.2.5 on 2023-09-29 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0004_clientpayment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientpayment',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='deployment',
            old_name='Officer_id',
            new_name='Officer',
        ),
    ]