from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.core.validators import validate_email
import base64
import uuid
from django.core.files.base import ContentFile


def employeeFormPage(request):
    try:
        return render(request, 'employee_list.html')
    except Exception as e:
        return JsonResponse({'error': str(e)})

def get_employees(request):
    try:
        employees = Employee.objects.all().values()  # Get all employees
        return JsonResponse(list(employees), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    

# Create a new employee using AJAX with exception handling
@csrf_exempt
def createEmployee(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'error': 'Invalid request method'}, status=405)

        data = json.loads(request.body.decode('utf-8'))
        

        # Extract fields
        requiredFields = [
            'name', 'email', 'gender', 'phoneNo', 'hno', 'street', 'city', 'state',
            'companyName', 'fromDate', 'toDate', 'address', 'qualificationName',
            'description', 'title', 'age', 'percentage', 'addressDetails',
            'qualifications', 'workExperience', 'projects', 'photo'
        ]

        for field in requiredFields:
            if field not in data:
                return JsonResponse({'error': f'Missing field: {field}'}, status=400)
        try:
            validate_email(data['email'])
        except ValidationError:
            return JsonResponse({'error': 'Invalid email format'}, status=400)
        photo_data = data['photo']
        if photo_data:
            if "base64," in photo_data:
                photo_data = photo_data.split("base64,")[1]  # Remove the "base64," part

            try:
                photo_format = "jpeg"  # You can dynamically infer format if needed
                photo_name = f"{uuid.uuid4()}.{photo_format}"
                photo_file = ContentFile(base64.b64decode(photo_data), name=photo_name)
            except Exception as decode_error:
                return JsonResponse({'error': f'Invalid image data: {str(decode_error)}'}, status=400)


        # Create and save employee
        newEmployee = Employee(
    name=data['name'],
    email=data['email'],
    gender=data['gender'],
    phoneNo=data['phoneNo'],
    hno=data['hno'],
    street=data['street'],
    city=data['city'],
    state=data['state'],
    companyName=data['companyName'],
    fromDate=data['fromDate'],
    toDate=data['toDate'],
    qualificationName=data['qualificationName'],
    description=data['description'],
    title=data['title'],
    age=int(data['age']),
    percentage=float(data['percentage']),
    addressDetails=data['addressDetails'],
    qualifications=data['qualifications'],
    workExperience=data['workExperience'],
    projects=data['projects'],
    photo=photo_file  # Store the image file instead of Base64 string
)

    

        newEmployee.save()
        return JsonResponse({'message': 'Employee created successfully'}, status=201)

    except ValueError as ve:
        return JsonResponse({'error': f'Invalid data: {str(ve)}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
@csrf_exempt
def updateEmployee(request, employee_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    try:
        employee = Employee.objects.get(id=employee_id)
        data = json.loads(request.body)
        # Check if email exists in the data and validate it
        if 'email' in data:
            try:
                validate_email(data['email'])
                if not data['email'].endswith('@gmail.com'):
                    return JsonResponse({'error': 'Only Gmail addresses are allowed'}, status=400)
            except ValidationError:
                return JsonResponse({'error': 'Invalid email format'}, status=400)

        for field in data:
            setattr(employee, field, data[field])
        employee.save()
        return JsonResponse({'message': 'Employee updated successfully'})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
@csrf_exempt
def deleteEmployee(request, employee_id):
    try:
        # Fetch the employee from the database by ID
        employee = Employee.objects.get(id=employee_id)

        # Delete the employee
        employee.delete()

        return JsonResponse({'message': 'Employee deleted successfully'})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
