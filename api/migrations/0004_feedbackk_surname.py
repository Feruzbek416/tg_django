# Generated by Django 4.1.3 on 2023-07-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_feedbackk_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackk',
            name='surname',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
