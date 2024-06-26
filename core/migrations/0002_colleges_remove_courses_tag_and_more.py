# Generated by Django 5.0.4 on 2024-05-24 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(null=True, upload_to='colleges_images')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='courses',
            name='tag',
        ),
        migrations.AlterField(
            model_name='courses',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, related_name='prerequisites_course', to='core.courses'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='schedule_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.courseschedules'),
        ),
        migrations.AlterField(
            model_name='courseschedules',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentsreg',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='college',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.colleges'),
        ),
    ]
