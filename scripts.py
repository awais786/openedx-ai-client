from generated_client.authoring_api_client.api.verify_student.verify_student_status_retrieve import *
from generated_client.authoring_api_client.models.student_progress_url import StudentProgressUrl
from generated_client.authoring_api_client.api.courses import courses_instructor_api_get_anon_ids_create
from generated_client.authoring_api_client.api.courses import courses_instructor_api_get_student_progress_url_create
from generated_client.authoring_api_client.api.courses import courses_instructor_api_list_course_role_members_create
from generated_client.authoring_api_client.api.courses import courses_instructor_api_modify_access_create
from generated_client.authoring_api_client.models.action_enum import ActionEnum
from generated_client.authoring_api_client.models.unique_student_identifier import UniqueStudentIdentifier
from generated_client.authoring_api_client.api.courses import \
    courses_instructor_api_mark_student_can_skip_entrance_exam_create
import json

base_url = "http://local.edly.io:8000/"
course_id='course-v1:edx+cs202+2101'
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


def parsing(response):
    # Check the status code
    if response.status_code == 200:
        try:
            parsed_json = json.loads(response.content)  # Manually parse the JSON response
            print(parsed_json)  # Print the parsed JSON
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
    else:
        # Print the error response content
        print(f"Error {response.status_code}: {response.content.decode('utf-8')}")


data = {
    "unique_student_identifier": "admin",
    "course_id": "course-v1:edX+DemoX+2024"
}

print('-----accessing anon ids api------')
response = courses_instructor_api_get_anon_ids_create.sync_detailed(
    client=client, course_id=course_id
)
parsing(response)

print('-----accessing progress api ------')

student_progress_data = StudentProgressUrl(
    unique_student_identifier="admin",
)

response = courses_instructor_api_get_student_progress_url_create.sync_detailed(
    client=client, course_id=course_id, body=student_progress_data
)
#
parsing(response)
#
print('-----accessing modify access api ------')

data = courses_instructor_api_modify_access_create.Access(
    unique_student_identifier='admin',
    rolename='instructor',
    action=ActionEnum.ALLOW  # Use the enum value here
)
response = courses_instructor_api_modify_access_create.sync_detailed(
    client=client,
    course_id=course_id,
    body=data
)

print('-----accessing create role members api ------')

response = courses_instructor_api_list_course_role_members_create.sync_detailed(
    client=client, course_id=course_id, body={'rolename': 'instructor'}
)

parsing(response)

print('-----accessing skip student entrance exam api ------')

data = UniqueStudentIdentifier(unique_student_identifier="admin")
response = courses_instructor_api_mark_student_can_skip_entrance_exam_create.sync_detailed(
    client=client, course_id=course_id, body=data
)
parsing(response)

#
# docker run --rm -v /Users/awais.qureshi/Documents/devstack/todo/schema.yaml:/local/schema.yaml -v /Users/awais.qureshi/Documents/devstack/todo/client:/local/out openapitools/openapi-generator-cli generate -i openapitools/openapi-generator-cli generate -i /local/schema.yaml -g python -o /local/out

