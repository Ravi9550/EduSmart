# Generated by Django 4.2.3 on 2023-12-22 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_rename_update_at_staff_model_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses'),
        ),
    ]
