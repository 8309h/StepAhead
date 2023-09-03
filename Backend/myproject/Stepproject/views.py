from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
 


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
import json
# import jwt
from rest_framework.decorators import api_view
from .models import StudentModel
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.
# just basic checking route
def welcome_path(request):
    return HttpResponse("Welcome to the Django Greetings App!")

    # views.py
from django.http import JsonResponse
from .models import Department
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_department(request):
    if request.method == 'POST':
        try:
            data = request.data  # Assuming you're using Django Rest Framework

            # Extract department data from the request data
            name = data.get('name')
            # Add more fields as needed

            # Validate required fields
            if not all([name]):
                return JsonResponse({"ok": False, "msg": "Department name is required."})

            # Create and save the department
            department = Department(name=name)
            department.save()

            return JsonResponse({"ok": True, "msg": "Department created successfully."})

        except Exception as e:
            return JsonResponse({"ok": False, "msg": f"Error creating department: {str(e)}"})

# views.py
from django.http import JsonResponse
from .models import Department
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serialized_departments = [department.name for department in departments]  # Modify as needed
        return JsonResponse({"departments": serialized_departments})

# views.py
from django.http import JsonResponse
from .models import Department
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_department(request, department_id):
    if request.method == 'GET':
        try:
            department = Department.objects.get(id=department_id)
            serialized_department = {"name": department.name}  # Modify as needed
            return JsonResponse(serialized_department)
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)


# views.py
from django.http import JsonResponse
from .models import Department
from rest_framework.decorators import api_view

@api_view(['PUT'])
def update_department(request, department_id):
    if request.method == 'PUT':
        try:
            data = request.data  # Assuming you're using Django Rest Framework

            # Extract updated department data from the request data
            name = data.get('name')
            # Add more fields as needed

            # Validate required fields
            if not all([name]):
                return JsonResponse({"ok": False, "msg": "Department name is required."})

            # Update the department
            department = Department.objects.get(id=department_id)
            department.name = name
            department.save()

            return JsonResponse({"ok": True, "msg": "Department updated successfully."})

        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": f"Error updating department: {str(e)}"})


# views.py
from django.http import JsonResponse
from .models import Department
from rest_framework.decorators import api_view

@api_view(['DELETE'])
def delete_department(request, department_id):
    if request.method == 'DELETE':
        try:
            department = Department.objects.get(id=department_id)
            department.delete()
            return JsonResponse({"ok": True, "msg": "Department deleted successfully."})
        except Department.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": f"Error deleting department: {str(e)}"})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            data = request.data

            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            role = data.get('role', 'student')  # Default to 'student' if role is not provided

            # Validate required fields
            if not all([name, email, password]):
                return JsonResponse({"ok": False, "msg": "All fields (name, email, password) are required."})

            # Check if user with the same email already exists
            if StudentModel.objects.filter(email=email).exists():
                return JsonResponse({"ok": False, "msg": "User with this email already exists."})

            # Hash the password
            pass_hash = make_password(password)

            # Create and save the user
            user = StudentModel(name=name, email=email, pass_hash=pass_hash, role=role)
            user.save()

            return JsonResponse({"ok": True, "msg": "Registered Successfully."})
        except Exception as e:
            return JsonResponse({"ok": False, "msg": f"Registration failed. Error: {str(e)}"})


# Import necessary modules# Import necessary modules
from django.http import JsonResponse
from django.contrib.auth import login
import jwt
from .models import StudentModel
from rest_framework.decorators import api_view

# login route
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            email = data.get('email')
            password = data.get('password')  # Get the user-entered password

            user = StudentModel.objects.filter(email=email).first()

             # Validate required fields
            if not all([email, password]):
                return JsonResponse({"ok": False, "msg": "All fields are required to fill"})
            
            if not user:
                return JsonResponse({"ok": False, "msg": "User with this email not found"})

            
            if not check_password(password, user.pass_hash):  # Compare the passwords
                return JsonResponse({"ok": False, "msg": "Invalid email or password"})

            payload = {"userId": user.id}
            secret_key = "harshal"  # Replace with your actual secret key
            # token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')  # Decode the bytes to string

            response = {
                "ok": True,
                # "token": token,
                "msg": "Login Successful",
                "id": user.id,
                "userName": user.name,
                "role":user.role
            }

            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok": False, "msg": str(e)})
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import InstructorModel

# Create a new instructor
@api_view(['POST'])
def create_instructor(request):
    if request.method == 'POST':
        try:
            data = request.data

            instructor = InstructorModel(**data)
            instructor.save()

            return Response({"ok": True, "msg": "Instructor created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"ok": False, "msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Update information for a specific instructor
@api_view(['PUT'])
def update_instructor(request, instructorID):
    try:
        instructor = InstructorModel.objects.get(InstructorID=instructorID)
        data = request.data

        for key, value in data.items():
            setattr(instructor, key, value)

        instructor.save()

        return Response({"ok": True, "msg": "Instructor updated successfully"})
    except InstructorModel.DoesNotExist:
        return Response({"ok": False, "msg": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"ok": False, "msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Delete an instructor record
@api_view(['DELETE'])
def delete_instructor(request, instructorID):
    try:
        instructor = InstructorModel.objects.get(InstructorID=instructorID)
        instructor.delete()

        return Response({"ok": True, "msg": "Instructor deleted successfully"})
    except InstructorModel.DoesNotExist:
        return Response({"ok": False, "msg": "Instructor not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"ok": False, "msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Import necessary modules
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course
from Stepproject.serializers import CourseSerializer 

# Create a new course
@api_view(['POST'])
def create_course(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve a list of all courses
@api_view(['GET'])
def list_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

# Retrieve details of a specific course
@api_view(['GET'])
def get_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return JsonResponse({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)

# Update information for a specific course
@api_view(['PUT'])
def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return JsonResponse({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a course
@api_view(['DELETE'])
def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return JsonResponse({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        course.delete()
        return JsonResponse({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
