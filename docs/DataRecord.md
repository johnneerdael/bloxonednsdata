# DataRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_name_spec** | **str** |  | [optional] 
**absolute_zone_name** | **str** | ReadOnly. The absolute domain name of the zone where this record belongs. | [optional] 
**comment** | **str** | Optional. Comment for the object. | [optional] 
**disabled** | **bool** | Optional. True if the object is disabled. A disabled object is effectively non-existent when generating configuration. | [optional] 
**dns_absolute_name_spec** | **str** |  | [optional] 
**dns_absolute_zone_name** | **str** | ReadOnly. The DNS protocol textual representation of the absolute domain name of the zone where this record belongs. | [optional] 
**dns_name_in_zone** | **str** | ReadOnly. The DNS protocol textual representation of the relative owner name. | [optional] 
**dns_rdata** | **str** | ReadOnly. The DNS protocol textual representation of the record data. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**DataRecordInheritance**](DataRecordInheritance.md) | Optional. Inheritance configuration. | [optional] 
**name_in_zone** | **str** | Required, writeable on create, readonly otherwise. The relative owner name to the zone origin. | [optional] 
**options** | [**TypesJSONValue**](TypesJSONValue.md) |  | [optional] 
**rdata** | [**TypesJSONValue**](TypesJSONValue.md) | Required. JSON representation of resource record data. | [optional] 
**source** | **list[str]** | ReadOnly. RR type-specific non-protocol record source. The source is a combination of indicators, each tracking how resource record appeared in system. Listed below are source indicators with their meaning:   Source indicator     | Description ----------------     | -------------------------------- STATIC               |  Record was created manually by API call to dns/record. Valid for all record types except SOA. SYSTEM               |  Record was created automatically based on name server assignment. Valid for SOA, NS, A, AAAA, PTR record types. DYNAMIC              |  Record was created dynamically by performing dynamic update. STATIC, SYSTEM       |  Record was created manually by API call but it is obfuscated by record generated based on name server assignment. DYNAMIC, SYSTEM      |  Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) |  | [optional] 
**ttl** | **int** | Record time to live value in seconds. | [optional] 
**type** | **str** |  | 
**view** | **str** | The resource identifier. | [optional] 
**view_name** | **str** | ReadOnly. Display name of dns/view. Synthetic field based on parent zone’s view. | [optional] 
**zone** | **str** | The resource identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


