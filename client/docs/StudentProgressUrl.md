# StudentProgressUrl

Serializer for course renders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_student_identifier** | **str** |  | 
**course_id** | **str** |  | [optional] 
**progress_url** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.student_progress_url import StudentProgressUrl

# TODO update the JSON string below
json = "{}"
# create an instance of StudentProgressUrl from a JSON string
student_progress_url_instance = StudentProgressUrl.from_json(json)
# print the JSON string representation of the object
print(StudentProgressUrl.to_json())

# convert the object into a dict
student_progress_url_dict = student_progress_url_instance.to_dict()
# create an instance of StudentProgressUrl from a dict
student_progress_url_from_dict = StudentProgressUrl.from_dict(student_progress_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


