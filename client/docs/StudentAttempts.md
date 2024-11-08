# StudentAttempts

Serializer for resetting a students attempts counter or starts a task to reset all students attempts counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**problem_to_reset** | **str** | The identifier or description of the problem that needs to be reset. | 
**unique_student_identifier** | **str** | Email or username of student. | [optional] 
**all_students** | **str** |  | [optional] 
**delete_module** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.student_attempts import StudentAttempts

# TODO update the JSON string below
json = "{}"
# create an instance of StudentAttempts from a JSON string
student_attempts_instance = StudentAttempts.from_json(json)
# print the JSON string representation of the object
print(StudentAttempts.to_json())

# convert the object into a dict
student_attempts_dict = student_attempts_instance.to_dict()
# create an instance of StudentAttempts from a dict
student_attempts_from_dict = StudentAttempts.from_dict(student_attempts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


