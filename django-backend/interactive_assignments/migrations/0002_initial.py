# Generated by Django 5.1.5 on 2025-01-25 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interactive_assignments', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='users.user'),
        ),
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='interactive_assignments.assignment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='users.user'),
        ),
    ]
