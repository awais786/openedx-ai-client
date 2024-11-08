# OpenAPI Client Generation for LMS Instructor APIs

This guide explains how to generate an OpenAPI 3 schema for LMS instructor APIs and use the generated client to interact with the APIs. We're leveraging `drf-spectacular` in Django Rest Framework (DRF) and `openapi-python-client` to automate the process.

## Prerequisites

- **Django LMS**: Ensure that the LMS is set up with the `drf-spectacular` package.
- **Python**: Python 3.x must be installed.
- **pip**: Make sure you have pip installed for managing Python packages.

## Steps to Generate API Client

### 1. Generate OpenAPI Schema

The `drf-spectacular` package is already implemented in the CMS, and we are adding it to the LMS to generate the schema for instructor APIs.

To generate the OpenAPI schema, run the following command inside your LMS directory:

```bash
python manage.py lms spectacular --format openapi-json > schema.json
```

### 2 Install OpenAPI Python Client Generator
To generate a Python client from the OpenAPI schema, install the openapi-python-client package:

```
pip install openapi-python-client
```

### 3 Generate the API Client
```
openapi-python-client generate --path schema.json --output-path ./generated_client
```

This will generate the client code in the generated_client directory.

### 4 Directory Structure
Once you've successfully generated the client, navigate to the generated_client directory. The directory structure will look something like this:
```
generated_client/
│
├── api/         # Contains logic to interact with API endpoints
├── models/      # Data models representing request and response schemas
└── __init__.py
```

### 5 Using the Generated Client

The generated_client is now ready to use in your project to interact with the LMS instructor APIs.
To modify the generated client to handle CSRF tokens and access tokens for authentication, you can 
extend the generated client by adding methods for retrieving and handling the tokens, 
ensuring that they are automatically used in requests.

Here's an example of how to use it:

from generated_client.authoring_api_client.models.student_progress_url import StudentProgressUrl
from generated_client.authoring_api_client.api.courses import courses_instructor_api_get_student_progress_url_create

# Initialize the client
```
base_url = "http://local.edly.io:8000/"
client_id = 'client-id'
client_secret = 'client-secret'

payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
    'token_type': 'jwt'
}

headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
client = Client(base_url=base_url, headers=headers)
token = client.retrieve_access_token(auth_url='oauth2/access_token', data=payload)
print("Authentication works !!!!!!!! ")

client = AuthenticatedClient(
    base_url=base_url,
    token=token
)

# Creating an instance for student progress data
student_progress_data = StudentProgressUrl(
    unique_student_identifier="admin",
)

# Sending request to retrieve student progress URL
response = courses_instructor_api_get_student_progress_url_create.sync_detailed(
    client=client, course_id='course-v1:edx+cs202+2101', body=student_progress_data
)

# Parsing the response
parsing(response)

print('-----accessing modify access api ------')

# Preparing data to modify access for a student
data = courses_instructor_api_modify_access_create.Access(
    unique_student_identifier='admin',
    rolename='instructor',
    action=ActionEnum.ALLOW  # Use the enum value here
)


# Check response or handle it accordingly
print(response)
```