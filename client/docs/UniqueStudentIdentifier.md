# UniqueStudentIdentifier

Serializer for identifying unique_student.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_student_identifier** | **str** | Email or username of user to change access | 

## Example

```python
from openapi_client.models.unique_student_identifier import UniqueStudentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueStudentIdentifier from a JSON string
unique_student_identifier_instance = UniqueStudentIdentifier.from_json(json)
# print the JSON string representation of the object
print(UniqueStudentIdentifier.to_json())

# convert the object into a dict
unique_student_identifier_dict = unique_student_identifier_instance.to_dict()
# create an instance of UniqueStudentIdentifier from a dict
unique_student_identifier_from_dict = UniqueStudentIdentifier.from_dict(unique_student_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


