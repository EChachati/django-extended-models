# Generated by Django 3.2.24 on 2024-02-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_extended_models_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedmodel2',
            name='related_field1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_extended_models_tests.relatedmodel1'),
        ),
        migrations.AddField(
            model_name='relatedmodel3',
            name='related_field2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_extended_models_tests.relatedmodel2'),
        ),
    ]
