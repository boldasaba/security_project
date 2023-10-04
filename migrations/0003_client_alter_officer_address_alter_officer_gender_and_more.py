# Generated by Django 4.2.5 on 2023-09-28 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0002_alter_officer_address_alter_officer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Client Name')),
                ('contact', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='officer',
            name='address',
            field=models.CharField(blank=True, default='N/P', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2),
        ),
        migrations.AlterField(
            model_name='officer',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Officer_Name'),
        ),
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deployment_date', models.DateField()),
                ('Shift', models.CharField(choices=[('M', 'Morning'), ('E', 'Evening')], max_length=10)),
                ('Officer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.officer')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.client')),
            ],
        ),
    ]