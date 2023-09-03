from django.urls import path
from . import views

urlpatterns = [
    path("",views.welcome_path,name="welcome"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
     path('instructors/', views.create_instructor, name='create_instructor'),

    # Update information for a specific instructor (PUT)
    path('instructors/<int:instructorID>/', views.update_instructor, name='update_instructor'),

    # Delete an instructor record (DELETE)
    path('instructors/<int:instructorID>/', views.delete_instructor, name='delete_instructor'),
    path('courses/', views.create_course, name='create_course'),

    # Retrieve a list of all courses
    path('courses/', views.list_courses, name='list_courses'),

    # Retrieve details of a specific course
    path('courses/<int:course_id>/', views.get_course, name='get_course'),

    # Update information for a specific course
    path('courses/<int:course_id>/', views.update_course, name='update_course'),

    # Delete a course
    path('courses/<int:course_id>/', views.delete_course, name='delete_course'),
    
    # path("get_all_users/",views.get_all_users,name="get_all_users")
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]