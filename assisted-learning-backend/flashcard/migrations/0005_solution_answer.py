# Generated by Django 3.1.4 on 2020-12-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0004_remove_solution_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='answer',
            field=models.TextField(default='Test'),
            preserve_default=False,
        ),
    ]