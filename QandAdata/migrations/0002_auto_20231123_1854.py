# QandAdata/migrations/0002_auto_20231123_1854.py

from django.db import migrations, models

def set_default_user_type(apps, schema_editor):
    Answer = apps.get_model('QandAdata', 'Answer')
    Answer.objects.filter(user_type=None).update(user_type='default_user_type_value')

class Migration(migrations.Migration):

    dependencies = [
        ('QandAdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_type',
            field=models.CharField(default='default_user_type_value', max_length=255),
        ),
        migrations.RunPython(set_default_user_type),
    ]
