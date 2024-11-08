# openapi_client.CoursesApi

All URIs are relative to *http://localhost:18000/api/contentstore*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courses_courseware_navigation_sidebar_toggles_retrieve**](CoursesApi.md#courses_courseware_navigation_sidebar_toggles_retrieve) | **GET** /courses/{course_id}/courseware-navigation-sidebar/toggles/ | 
[**courses_courseware_search_enabled_retrieve**](CoursesApi.md#courses_courseware_search_enabled_retrieve) | **GET** /courses/{course_id}/courseware-search/enabled/ | 
[**courses_instructor_api_change_due_date_create**](CoursesApi.md#courses_instructor_api_change_due_date_create) | **POST** /courses/{course_id}/instructor/api/change_due_date | 
[**courses_instructor_api_get_anon_ids_create**](CoursesApi.md#courses_instructor_api_get_anon_ids_create) | **POST** /courses/{course_id}/instructor/api/get_anon_ids | 
[**courses_instructor_api_get_grading_config_create**](CoursesApi.md#courses_instructor_api_get_grading_config_create) | **POST** /courses/{course_id}/instructor/api/get_grading_config | 
[**courses_instructor_api_get_student_enrollment_status_create**](CoursesApi.md#courses_instructor_api_get_student_enrollment_status_create) | **POST** /courses/{course_id}/instructor/api/get_student_enrollment_status | 
[**courses_instructor_api_get_student_progress_url_create**](CoursesApi.md#courses_instructor_api_get_student_progress_url_create) | **POST** /courses/{course_id}/instructor/api/get_student_progress_url | 
[**courses_instructor_api_get_students_who_may_enroll_create**](CoursesApi.md#courses_instructor_api_get_students_who_may_enroll_create) | **POST** /courses/{course_id}/instructor/api/get_students_who_may_enroll | 
[**courses_instructor_api_get_students_who_may_enroll_retrieve**](CoursesApi.md#courses_instructor_api_get_students_who_may_enroll_retrieve) | **GET** /courses/{course_id}/instructor/api/get_students_who_may_enroll | 
[**courses_instructor_api_list_course_role_members_create**](CoursesApi.md#courses_instructor_api_list_course_role_members_create) | **POST** /courses/{course_id}/instructor/api/list_course_role_members | 
[**courses_instructor_api_list_email_content_create**](CoursesApi.md#courses_instructor_api_list_email_content_create) | **POST** /courses/{course_id}/instructor/api/list_email_content | 
[**courses_instructor_api_list_entrance_exam_instructor_tasks_create**](CoursesApi.md#courses_instructor_api_list_entrance_exam_instructor_tasks_create) | **POST** /courses/{course_id}/instructor/api/list_entrance_exam_instructor_tasks | 
[**courses_instructor_api_list_instructor_tasks_create**](CoursesApi.md#courses_instructor_api_list_instructor_tasks_create) | **POST** /courses/{course_id}/instructor/api/list_instructor_tasks | 
[**courses_instructor_api_list_report_downloads_create**](CoursesApi.md#courses_instructor_api_list_report_downloads_create) | **POST** /courses/{course_id}/instructor/api/list_report_downloads | 
[**courses_instructor_api_mark_student_can_skip_entrance_exam_create**](CoursesApi.md#courses_instructor_api_mark_student_can_skip_entrance_exam_create) | **POST** /courses/{course_id}/instructor/api/mark_student_can_skip_entrance_exam | 
[**courses_instructor_api_modify_access_create**](CoursesApi.md#courses_instructor_api_modify_access_create) | **POST** /courses/{course_id}/instructor/api/modify_access | 
[**courses_instructor_api_register_and_enroll_students_create**](CoursesApi.md#courses_instructor_api_register_and_enroll_students_create) | **POST** /courses/{course_id}/instructor/api/register_and_enroll_students | 
[**courses_instructor_api_reset_due_date_create**](CoursesApi.md#courses_instructor_api_reset_due_date_create) | **POST** /courses/{course_id}/instructor/api/reset_due_date | 
[**courses_instructor_api_reset_student_attempts_create**](CoursesApi.md#courses_instructor_api_reset_student_attempts_create) | **POST** /courses/{course_id}/instructor/api/reset_student_attempts | 
[**courses_instructor_api_send_email_create**](CoursesApi.md#courses_instructor_api_send_email_create) | **POST** /courses/{course_id}/instructor/api/send_email | 
[**courses_instructor_api_show_student_extensions_create**](CoursesApi.md#courses_instructor_api_show_student_extensions_create) | **POST** /courses/{course_id}/instructor/api/show_student_extensions | 
[**courses_teams_retrieve**](CoursesApi.md#courses_teams_retrieve) | **GET** /courses/{course_id}/teams/ | 
[**courses_xblock_view_retrieve**](CoursesApi.md#courses_xblock_view_retrieve) | **GET** /courses/{course_id}/xblock/{usage_id}/view/{view_name} | 
[**courses_yt_video_metadata_retrieve**](CoursesApi.md#courses_yt_video_metadata_retrieve) | **GET** /courses/yt_video_metadata | 


# **courses_courseware_navigation_sidebar_toggles_retrieve**
> courses_courseware_navigation_sidebar_toggles_retrieve(course_id)



GET endpoint to return navigation sidebar toggles.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_courseware_navigation_sidebar_toggles_retrieve(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_courseware_navigation_sidebar_toggles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_courseware_search_enabled_retrieve**
> courses_courseware_search_enabled_retrieve(course_id)



Simple GET endpoint to expose whether the user may use Courseware Search for a given course.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_courseware_search_enabled_retrieve(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_courseware_search_enabled_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_change_due_date_create**
> BlockDueDate courses_instructor_api_change_due_date_create(course_id, block_due_date)



Grants a due date extension to a student for a particular unit.  params:     url (str): The URL related to the block that needs the due date update.     due_datetime (str): The new due date and time for the block.     student (str): The email or username of the student whose access is being modified.

### Example


```python
import openapi_client
from openapi_client.models.block_due_date import BlockDueDate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    block_due_date = openapi_client.BlockDueDate() # BlockDueDate | 

    try:
        api_response = api_instance.courses_instructor_api_change_due_date_create(course_id, block_due_date)
        print("The response of CoursesApi->courses_instructor_api_change_due_date_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_change_due_date_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **block_due_date** | [**BlockDueDate**](BlockDueDate.md)|  | 

### Return type

[**BlockDueDate**](BlockDueDate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_anon_ids_create**
> courses_instructor_api_get_anon_ids_create(course_id)



Handle POST request to generate a CSV output.  Returns:     Response: A CSV file with two columns: `user-id` and `anonymized-user-id`.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_get_anon_ids_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_anon_ids_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_grading_config_create**
> courses_instructor_api_get_grading_config_create(course_id)



Post method to return grading config.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_get_grading_config_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_grading_config_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_student_enrollment_status_create**
> courses_instructor_api_get_student_enrollment_status_create(course_id)



Permission: Limited to staff access. Takes query parameter unique_student_identifier

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_get_student_enrollment_status_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_student_enrollment_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_student_progress_url_create**
> StudentProgressUrl courses_instructor_api_get_student_progress_url_create(course_id, student_progress_url)



Post method for validating incoming data and generating progress URL

### Example


```python
import openapi_client
from openapi_client.models.student_progress_url import StudentProgressUrl
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    student_progress_url = openapi_client.StudentProgressUrl() # StudentProgressUrl | 

    try:
        api_response = api_instance.courses_instructor_api_get_student_progress_url_create(course_id, student_progress_url)
        print("The response of CoursesApi->courses_instructor_api_get_student_progress_url_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_student_progress_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **student_progress_url** | [**StudentProgressUrl**](StudentProgressUrl.md)|  | 

### Return type

[**StudentProgressUrl**](StudentProgressUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_students_who_may_enroll_create**
> courses_instructor_api_get_students_who_may_enroll_create(course_id)



Initiate generation of a CSV file containing information about  students who may enroll in a course.  Responds with JSON     {\"status\": \"... status message ...\"}

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_get_students_who_may_enroll_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_students_who_may_enroll_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_get_students_who_may_enroll_retrieve**
> courses_instructor_api_get_students_who_may_enroll_retrieve(course_id)



Initiate generation of a CSV file containing information about

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_get_students_who_may_enroll_retrieve(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_get_students_who_may_enroll_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_list_course_role_members_create**
> courses_instructor_api_list_course_role_members_create(course_id)



Handles POST request to list instructors and staff.  Args:     request (HttpRequest): The request object containing user data.     course_id (str): The ID of the course to list instructors and staff for.  Returns:     Response: A Response object containing the list of instructors and staff or an error message.  Raises:     Http404: If the course does not exist.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_list_course_role_members_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_list_course_role_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_list_email_content_create**
> courses_instructor_api_list_email_content_create(course_id)



List the content of bulk emails sent for a specific course.  Args:     request (HttpRequest): The HTTP request object.     course_id (str): The ID of the course for which to list the bulk emails.  Returns:     HttpResponse: A response object containing the list of bulk email contents.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_list_email_content_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_list_email_content_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_list_entrance_exam_instructor_tasks_create**
> courses_instructor_api_list_entrance_exam_instructor_tasks_create(course_id)



List entrance exam related instructor tasks.  Takes either of the following query parameters     - unique_student_identifier is an email or username     - all_students is a boolean

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_list_entrance_exam_instructor_tasks_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_list_entrance_exam_instructor_tasks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_list_instructor_tasks_create**
> ListInstructorTaskInput courses_instructor_api_list_instructor_tasks_create(course_id, list_instructor_task_input=list_instructor_task_input)



List instructor tasks.

### Example


```python
import openapi_client
from openapi_client.models.list_instructor_task_input import ListInstructorTaskInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    list_instructor_task_input = openapi_client.ListInstructorTaskInput() # ListInstructorTaskInput |  (optional)

    try:
        api_response = api_instance.courses_instructor_api_list_instructor_tasks_create(course_id, list_instructor_task_input=list_instructor_task_input)
        print("The response of CoursesApi->courses_instructor_api_list_instructor_tasks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_list_instructor_tasks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **list_instructor_task_input** | [**ListInstructorTaskInput**](ListInstructorTaskInput.md)|  | [optional] 

### Return type

[**ListInstructorTaskInput**](ListInstructorTaskInput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_list_report_downloads_create**
> courses_instructor_api_list_report_downloads_create(course_id)



List grade CSV files that are available for download for this course.  Takes the following query parameters: - (optional) report_name - name of the report

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_list_report_downloads_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_list_report_downloads_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_mark_student_can_skip_entrance_exam_create**
> UniqueStudentIdentifier courses_instructor_api_mark_student_can_skip_entrance_exam_create(course_id, unique_student_identifier)



### Example


```python
import openapi_client
from openapi_client.models.unique_student_identifier import UniqueStudentIdentifier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    unique_student_identifier = openapi_client.UniqueStudentIdentifier() # UniqueStudentIdentifier | 

    try:
        api_response = api_instance.courses_instructor_api_mark_student_can_skip_entrance_exam_create(course_id, unique_student_identifier)
        print("The response of CoursesApi->courses_instructor_api_mark_student_can_skip_entrance_exam_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_mark_student_can_skip_entrance_exam_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **unique_student_identifier** | [**UniqueStudentIdentifier**](UniqueStudentIdentifier.md)|  | 

### Return type

[**UniqueStudentIdentifier**](UniqueStudentIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_modify_access_create**
> Access courses_instructor_api_modify_access_create(course_id, access)



Modify staff/instructor access of other user. Requires instructor access.

### Example


```python
import openapi_client
from openapi_client.models.access import Access
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    access = openapi_client.Access() # Access | 

    try:
        api_response = api_instance.courses_instructor_api_modify_access_create(course_id, access)
        print("The response of CoursesApi->courses_instructor_api_modify_access_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_modify_access_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **access** | [**Access**](Access.md)|  | 

### Return type

[**Access**](Access.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_register_and_enroll_students_create**
> courses_instructor_api_register_and_enroll_students_create(course_id)



Create new account and Enroll students in this course. Passing a csv file that contains a list of students. Order in csv should be the following email = 0; username = 1; name = 2; country = 3. If there are more than 4 columns in the csv: cohort = 4, course mode = 5. Requires staff access.  -If the email address and username already exists and the user is enrolled in the course, do nothing (including no email gets sent out)  -If the email address already exists, but the username is different, match on the email address only and continue to enroll the user in the course using the email address as the matching criteria. Note the change of username as a warning message (but not a failure). Send a standard enrollment email which is the same as the existing manual enrollment  -If the username already exists (but not the email), assume it is a different user and fail to create the new account. The failure will be messaged in a response in the browser.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_instructor_api_register_and_enroll_students_create(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_register_and_enroll_students_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_reset_due_date_create**
> BlockDueDate courses_instructor_api_reset_due_date_create(course_id, block_due_date)



reset a due date extension to a student for a particular unit. params:     url (str): The URL related to the block that needs the due date update.     student (str): The email or username of the student whose access is being modified.     reason (str): Optional param.

### Example


```python
import openapi_client
from openapi_client.models.block_due_date import BlockDueDate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    block_due_date = openapi_client.BlockDueDate() # BlockDueDate | 

    try:
        api_response = api_instance.courses_instructor_api_reset_due_date_create(course_id, block_due_date)
        print("The response of CoursesApi->courses_instructor_api_reset_due_date_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_reset_due_date_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **block_due_date** | [**BlockDueDate**](BlockDueDate.md)|  | 

### Return type

[**BlockDueDate**](BlockDueDate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_reset_student_attempts_create**
> StudentAttempts courses_instructor_api_reset_student_attempts_create(course_id, student_attempts)



Takes some of the following query parameters - problem_to_reset is a urlname of a problem - unique_student_identifier is an email or username - all_students is a boolean     requires instructor access     mutually exclusive with delete_module     mutually exclusive with delete_module - delete_module is a boolean     requires instructor access     mutually exclusive with all_students

### Example


```python
import openapi_client
from openapi_client.models.student_attempts import StudentAttempts
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    student_attempts = openapi_client.StudentAttempts() # StudentAttempts | 

    try:
        api_response = api_instance.courses_instructor_api_reset_student_attempts_create(course_id, student_attempts)
        print("The response of CoursesApi->courses_instructor_api_reset_student_attempts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_reset_student_attempts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **student_attempts** | [**StudentAttempts**](StudentAttempts.md)|  | 

### Return type

[**StudentAttempts**](StudentAttempts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_send_email_create**
> SendEmail courses_instructor_api_send_email_create(course_id, send_email)



Query Parameters: - 'send_to' specifies what group the email should be sent to    Options are defined by the CourseEmail model in    lms/djangoapps/bulk_email/models.py - 'subject' specifies email's subject - 'message' specifies email's content

### Example


```python
import openapi_client
from openapi_client.models.send_email import SendEmail
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    send_email = openapi_client.SendEmail() # SendEmail | 

    try:
        api_response = api_instance.courses_instructor_api_send_email_create(course_id, send_email)
        print("The response of CoursesApi->courses_instructor_api_send_email_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_send_email_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **send_email** | [**SendEmail**](SendEmail.md)|  | 

### Return type

[**SendEmail**](SendEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_instructor_api_show_student_extensions_create**
> ShowStudentExtension courses_instructor_api_show_student_extensions_create(course_id, show_student_extension)



Handles POST requests to retrieve due date extensions for a specific student within a specified course.  Parameters: - `request`: The HTTP request object containing user-submitted data. - `course_id`: The ID of the course for which the extensions are being queried.  Data expected in the request: - `student`: A required field containing the identifier of the student for whom   the due date extensions are being retrieved. This data is extracted from the   request body.  Returns: - A JSON response containing the details of the due date extensions granted to   the specified student in the specified course.

### Example


```python
import openapi_client
from openapi_client.models.show_student_extension import ShowStudentExtension
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    show_student_extension = openapi_client.ShowStudentExtension() # ShowStudentExtension | 

    try:
        api_response = api_instance.courses_instructor_api_show_student_extensions_create(course_id, show_student_extension)
        print("The response of CoursesApi->courses_instructor_api_show_student_extensions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_instructor_api_show_student_extensions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **show_student_extension** | [**ShowStudentExtension**](ShowStudentExtension.md)|  | 

### Return type

[**ShowStudentExtension**](ShowStudentExtension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_teams_retrieve**
> courses_teams_retrieve(course_id)



Renders the teams dashboard, which is shown on the \"Teams\" tab.  Raises a 404 if the course specified by course_id does not exist, the user is not registered for the course, or the teams feature is not enabled.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 

    try:
        api_instance.courses_teams_retrieve(course_id)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_teams_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_xblock_view_retrieve**
> courses_xblock_view_retrieve(course_id, usage_id, view_name)



Returns the rendered view of a given XBlock, with related resources  Returns a json object containing two keys:     html: The rendered html of the view     resources: A list of tuples where the first element is the resource hash, and         the second is the resource description

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)
    course_id = 'course_id_example' # str | 
    usage_id = 'usage_id_example' # str | 
    view_name = 'view_name_example' # str | 

    try:
        api_instance.courses_xblock_view_retrieve(course_id, usage_id, view_name)
    except Exception as e:
        print("Exception when calling CoursesApi->courses_xblock_view_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **usage_id** | **str**|  | 
 **view_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_yt_video_metadata_retrieve**
> courses_yt_video_metadata_retrieve()



Will hit the youtube API if the key is available in settings :return: youtube video metadata

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:18000/api/contentstore
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:18000/api/contentstore"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CoursesApi(api_client)

    try:
        api_instance.courses_yt_video_metadata_retrieve()
    except Exception as e:
        print("Exception when calling CoursesApi->courses_yt_video_metadata_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

