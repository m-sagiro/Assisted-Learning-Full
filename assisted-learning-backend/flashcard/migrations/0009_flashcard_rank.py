# Generated by Django 3.1.4 on 2021-01-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0008_flashcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='rank',
            field=models.IntegerField(default=1, null=True),
        ),
    ]