from django.urls import path
from . import views
urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('my-courses/', views.myCourses, name='my-courses'),
    path('add-course/<int:pk>', views.addCourse, name='add-course'),
    path('course/<int:pk>', views.courseInfo, name='course'),
    path('delete-course/<int:pk>', views.deleteCourse, name='delete-count'),
    path('colleges/<int:pk>', views.collegeCourses, name='colleges'),
    path('colleges/<int:pk>', views.collegeCourses, name='my-courses'),
]
