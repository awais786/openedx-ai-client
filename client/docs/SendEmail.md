# SendEmail

Serializer for sending an email with optional scheduling.  Fields:     send_to (str): The email address of the recipient. This field is required.     subject (str): The subject line of the email. This field is required.     message (str): The body of the email. This field is required.     schedule (str, optional):     An optional field to specify when the email should be sent.     If provided, this should be a string that can be parsed into a     datetime format or some other scheduling logic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_to** | **str** |  | 
**subject** | **str** |  | 
**message** | **str** |  | 
**schedule** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.send_email import SendEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmail from a JSON string
send_email_instance = SendEmail.from_json(json)
# print the JSON string representation of the object
print(SendEmail.to_json())

# convert the object into a dict
send_email_dict = send_email_instance.to_dict()
# create an instance of SendEmail from a dict
send_email_from_dict = SendEmail.from_dict(send_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


