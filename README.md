# Student-Management-System-Django-REST-API-Project
Student Management System is the Django application that uses the Django REST Framework. Here's a brief description of what the project does:

i) Models: The project defines a Django model named Students, which represents student information such as first_name, last_name, address, roll_number, and mobile number.
ii) Serializers: It uses Django REST Framework's serializers to convert the Students model instances into JSON representations that can be easily rendered into HTTP responses. The StudentSerializer class defines how the Students model data should be serialized and deserialized for use in API requests and responses.
iii) Views: The project defines API views using Django REST Framework's APIView. These views handle HTTP requests such as GET, POST, PATCH, and DELETE for managing student data. The views interact with the serializers to validate input data, perform CRUD operations on the Students model, and return appropriate HTTP responses.
iv) Validation: Custom validation logic is implemented in the serializers to ensure that input data meets certain criteria, such as ensuring that the roll_number is a valid integer and that duplicate roll_numbers are not accepted.

Overall, the project serves as a backend API for managing student records, allowing clients to perform CRUD operations on student data through HTTP requests.
