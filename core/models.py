from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Day(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    
class CourseSchedules(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.ManyToManyField(Day, related_name='course_schedules', blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.room_no} from {self.start_time} to {self.end_time}"

class Colleges(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to='colleges_images',null=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Courses(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='courses_images',null=True)
    college = models.ForeignKey(Colleges, on_delete=models.CASCADE, default=1)

    description = models.CharField(max_length=255)
    prerequisites = models.ManyToManyField('self', related_name='prerequisites_course', blank=True)
    instractor = models.CharField(max_length=30,default='')
    capacity = models.IntegerField(default=0)
    schedule_id = models.ForeignKey(CourseSchedules,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.name

class studentsReg(models.Model):
    id = models.AutoField(primary_key=True)
    student_id= models.ForeignKey(Students, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
