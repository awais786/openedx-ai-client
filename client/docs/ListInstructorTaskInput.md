# ListInstructorTaskInput

Serializer for handling the input data for the problem response report generation API.  Attributes:     unique_student_identifier (str): The email or username of the student.                                       This field is optional, but if provided, the `problem_location_str`                                       must also be provided.     problem_location_str (str): The string representing the location of the problem within the course.                                 This field is optional, unless `unique_student_identifier` is provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_student_identifier** | **str** | Email or username of student | [optional] 
**problem_location_str** | **str** | Problem location | [optional] 

## Example

```python
from openapi_client.models.list_instructor_task_input import ListInstructorTaskInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListInstructorTaskInput from a JSON string
list_instructor_task_input_instance = ListInstructorTaskInput.from_json(json)
# print the JSON string representation of the object
print(ListInstructorTaskInput.to_json())

# convert the object into a dict
list_instructor_task_input_dict = list_instructor_task_input_instance.to_dict()
# create an instance of ListInstructorTaskInput from a dict
list_instructor_task_input_from_dict = ListInstructorTaskInput.from_dict(list_instructor_task_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


