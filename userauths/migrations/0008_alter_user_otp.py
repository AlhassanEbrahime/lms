# Generated by Django 5.1.2 on 2024-11-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]