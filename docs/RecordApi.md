# bloxonednsdata.RecordApi

All URIs are relative to *https://csp.infoblox.com/api/ddi.dns.data/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_create**](RecordApi.md#record_create) | **POST** /dns/record | Create the Record object.
[**record_delete**](RecordApi.md#record_delete) | **DELETE** /dns/record/{id} | Delete the Record object.
[**record_list**](RecordApi.md#record_list) | **GET** /dns/record | List the Record objects.
[**record_read**](RecordApi.md#record_read) | **GET** /dns/record/{id} | Read the Record object.
[**record_soa_serial_increment**](RecordApi.md#record_soa_serial_increment) | **POST** /dns/record/{id}/serial_increment | SOA serial increment
[**record_update**](RecordApi.md#record_update) | **PATCH** /dns/record/{id} | Update the Record object.


# **record_create**
> DataCreateRecordResponse record_create(body)

Create the Record object.

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
body = bloxonednsdata.DataRecord() # DataRecord | 

try:
    # Create the Record object.
    api_response = api_instance.record_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->record_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataRecord**](DataRecord.md)|  | 

### Return type

[**DataCreateRecordResponse**](DataCreateRecordResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_delete**
> record_delete(id)

Delete the Record object.

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the Record object.
    api_instance.record_delete(id)
except ApiException as e:
    print("Exception when calling RecordApi->record_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_list**
> DataListRecordResponse record_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by)

List the Record objects.

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)

try:
    # List the Record objects.
    api_response = api_instance.record_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, tfilter=tfilter, torder_by=torder_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->record_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 

### Return type

[**DataListRecordResponse**](DataListRecordResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_read**
> DataReadRecordResponse record_read(id, fields=fields)

Read the Record object.

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Record object.
    api_response = api_instance.record_read(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->record_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**DataReadRecordResponse**](DataReadRecordResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_soa_serial_increment**
> DataSOASerialIncrementResponse record_soa_serial_increment(id, body)

SOA serial increment

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxonednsdata.DataSOASerialIncrementRequest() # DataSOASerialIncrementRequest | 

try:
    # SOA serial increment
    api_response = api_instance.record_soa_serial_increment(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->record_soa_serial_increment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**DataSOASerialIncrementRequest**](DataSOASerialIncrementRequest.md)|  | 

### Return type

[**DataSOASerialIncrementResponse**](DataSOASerialIncrementResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_update**
> DataUpdateRecordResponse record_update(id, body)

Update the Record object.

### Example
```python
from __future__ import print_function
import time
import bloxonednsdata
from bloxonednsdata.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonednsdata.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonednsdata.RecordApi(bloxonednsdata.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxonednsdata.DataRecord() # DataRecord | 

try:
    # Update the Record object.
    api_response = api_instance.record_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordApi->record_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**DataRecord**](DataRecord.md)|  | 

### Return type

[**DataUpdateRecordResponse**](DataUpdateRecordResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

