# BlockDueDate

Serializer for handling block due date updates for a specific student. Fields:     url (str): The URL related to the block that needs the due date update.     due_datetime (str): The new due date and time for the block.     student (str): The email or username of the student whose access is being modified.     reason (str): Reason why updating this.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**due_datetime** | **str** |  | 
**student** | **str** | Email or username of user to change access | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.block_due_date import BlockDueDate

# TODO update the JSON string below
json = "{}"
# create an instance of BlockDueDate from a JSON string
block_due_date_instance = BlockDueDate.from_json(json)
# print the JSON string representation of the object
print(BlockDueDate.to_json())

# convert the object into a dict
block_due_date_dict = block_due_date_instance.to_dict()
# create an instance of BlockDueDate from a dict
block_due_date_from_dict = BlockDueDate.from_dict(block_due_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


