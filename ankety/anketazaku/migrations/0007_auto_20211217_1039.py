# Generated by Django 2.2.12 on 2021-12-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketazaku', '0006_question_rightanswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='answer_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='rightanswer',
        ),
        migrations.AddField(
            model_name='question',
            name='rightone',
            field=models.CharField(default='', max_length=200),
        ),
    ]
