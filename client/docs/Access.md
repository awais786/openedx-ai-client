# Access

Serializer for managing user access changes. This serializer validates and processes the data required to modify user access within a system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_student_identifier** | **str** | Email or username of user to change access | 
**rolename** | **str** | Role name to assign to the user | 
**action** | [**ActionEnum**](ActionEnum.md) | Action to perform on the user&#39;s access  * &#x60;allow&#x60; - allow * &#x60;revoke&#x60; - revoke | 

## Example

```python
from openapi_client.models.access import Access

# TODO update the JSON string below
json = "{}"
# create an instance of Access from a JSON string
access_instance = Access.from_json(json)
# print the JSON string representation of the object
print(Access.to_json())

# convert the object into a dict
access_dict = access_instance.to_dict()
# create an instance of Access from a dict
access_from_dict = Access.from_dict(access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


