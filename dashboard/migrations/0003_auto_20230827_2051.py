# Generated by Django 3.2.8 on 2023-08-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230827_2051'),
        ('dashboard', '0002_remove_feedback_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='practice_paper',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='session',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
        ),
        migrations.AlterField(
            model_name='whatsnew',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
