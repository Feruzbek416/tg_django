# Generated by Django 4.1.3 on 2023-06-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_feedbackk_delete_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackk',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]