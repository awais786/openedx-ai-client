from client.openapi_client import Access, SendEmail, StudentProgressUrl
from client import openapi_client

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJvcGVuZWR4IiwiZXhwIjoxNzMxMDU2MzAzLCJncmFudF90eXBlIjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiaWF0IjoxNzMxMDUyNzAzLCJpc3MiOiJodHRwOi8vbG9jYWwuZWRseS5pby9vYXV0aDIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJhZG1pbiIsInNjb3BlcyI6WyJyZWFkIiwid3JpdGUiLCJlbWFpbCIsInByb2ZpbGUiXSwidmVyc2lvbiI6IjEuMi4wIiwic3ViIjoiYzIwOGU4Yzk3MjFlODJkMmZhOTY4ZmZmYmY0OWRlOGEiLCJmaWx0ZXJzIjpbXSwiaXNfcmVzdHJpY3RlZCI6ZmFsc2UsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwibmFtZSI6ImFkbWluIiwiZmFtaWx5X25hbWUiOiJtaW4iLCJnaXZlbl9uYW1lIjoiYWQiLCJhZG1pbmlzdHJhdG9yIjp0cnVlLCJzdXBlcnVzZXIiOnRydWV9.9G0j3X6QmBF0kbo5kTdEWCjHG4MNHyKq1RHDFsQbFso"

configuration = openapi_client.Configuration(
    api_key_prefix="JWT", host="http://local.edly.io:8000", access_token=access_token
)

api_client = openapi_client.ApiClient(
    configuration=configuration, header_name="Authorization", header_value=f"JWT {access_token}"
)
api_instance = openapi_client.CoursesApi(api_client)
course_id = 'course-v1:edx+cs202+2101'

student_progress_url_data = {
    "unique_student_identifier": "admin",  # Ensure this value is not None
    "course_id": course_id
}

progress_url = StudentProgressUrl(**student_progress_url_data)

print(api_instance.courses_instructor_api_get_student_progress_url_create(
    course_id=course_id,
    student_progress_url=progress_url
))

modify_access_data = {
    "unique_student_identifier": "admin",
    "action": "allow",
    "rolename": "instructor"
}

# Convert the dictionary into a Pydantic model instance
access_instance = Access(**modify_access_data)
response = api_instance.courses_instructor_api_modify_access_create(
    course_id="course-v1:edx+cs202+2101",  # Replace with actual course_id
    access=access_instance  # Pass the dictionary with correct name
)
print(response.to_json())

# import json
# from client.openapi_client.models import send_email
# send_email_data = {
#     "send_to": '["myself", "staff", "cohort:awa"]',
#     "subject": "this is sub",
#     "message": "This is my test",
#     "schedule": "2025-08-29T06:01:00.000Z"
# }
#
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
#
# sendemail = SendEmail(**send_email_data)
# response = api_instance.courses_instructor_api_send_email_create(
#     course_id="course-v1:edx+cs202+2101",  # Replace with actual course_id
#     send_email=sendemail,  # Pass the dictionary with correct name,
#     # _headers=headers
# )
# print(response.to_json())
