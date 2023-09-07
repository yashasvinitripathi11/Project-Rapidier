# Generated by Django 3.2.8 on 2023-09-06 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20230905_2157'),
        ('dashboard', '0006_assignment_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
            preserve_default=False,
        ),
    ]
