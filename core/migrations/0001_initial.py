# Generated by Django 5.0.4 on 2024-05-24 06:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSchedules',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('room_no', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(null=True, upload_to='courses_images')),
                ('tag', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=255)),
                ('instractor', models.CharField(default='', max_length=30)),
                ('capacity', models.IntegerField(default=0)),
                ('prerequisites', models.ManyToManyField(related_name='prerequisites_course', to='core.courses')),
                ('schedule_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.courseschedules')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='studentsReg',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.students')),
            ],
        ),
    ]
