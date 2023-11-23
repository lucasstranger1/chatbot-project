# Generated by Django 3.1.14 on 2023-11-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandAdata', '0002_auto_20231123_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user_type',
            field=models.CharField(choices=[('healthcare_giver', 'Healthcare Giver'), ('parent', 'Parent'), ('educator', 'Educator')], default='user_type', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_type',
            field=models.CharField(choices=[('healthcare_giver', 'Healthcare Giver'), ('parent', 'Parent'), ('educator', 'Educator')], max_length=20),
        ),
    ]
