# coding: utf-8

"""
    DNS Data API

    The DNS Data is a BloxOne DDI service providing primary authoritative zone support. DNS Data is authoritative for all DNS resource records and is acting as a primary DNS server. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DataRecord(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'absolute_name_spec': 'str',
        'absolute_zone_name': 'str',
        'comment': 'str',
        'disabled': 'bool',
        'dns_absolute_name_spec': 'str',
        'dns_absolute_zone_name': 'str',
        'dns_name_in_zone': 'str',
        'dns_rdata': 'str',
        'id': 'str',
        'inheritance_sources': 'DataRecordInheritance',
        'name_in_zone': 'str',
        'options': 'TypesJSONValue',
        'rdata': 'TypesJSONValue',
        'source': 'list[str]',
        'tags': 'TypesJSONValue',
        'ttl': 'int',
        'type': 'str',
        'view': 'str',
        'view_name': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'absolute_name_spec': 'absolute_name_spec',
        'absolute_zone_name': 'absolute_zone_name',
        'comment': 'comment',
        'disabled': 'disabled',
        'dns_absolute_name_spec': 'dns_absolute_name_spec',
        'dns_absolute_zone_name': 'dns_absolute_zone_name',
        'dns_name_in_zone': 'dns_name_in_zone',
        'dns_rdata': 'dns_rdata',
        'id': 'id',
        'inheritance_sources': 'inheritance_sources',
        'name_in_zone': 'name_in_zone',
        'options': 'options',
        'rdata': 'rdata',
        'source': 'source',
        'tags': 'tags',
        'ttl': 'ttl',
        'type': 'type',
        'view': 'view',
        'view_name': 'view_name',
        'zone': 'zone'
    }

    def __init__(self, absolute_name_spec=None, absolute_zone_name=None, comment=None, disabled=None, dns_absolute_name_spec=None, dns_absolute_zone_name=None, dns_name_in_zone=None, dns_rdata=None, id=None, inheritance_sources=None, name_in_zone=None, options=None, rdata=None, source=None, tags=None, ttl=None, type=None, view=None, view_name=None, zone=None):  # noqa: E501
        """DataRecord - a model defined in Swagger"""  # noqa: E501

        self._absolute_name_spec = None
        self._absolute_zone_name = None
        self._comment = None
        self._disabled = None
        self._dns_absolute_name_spec = None
        self._dns_absolute_zone_name = None
        self._dns_name_in_zone = None
        self._dns_rdata = None
        self._id = None
        self._inheritance_sources = None
        self._name_in_zone = None
        self._options = None
        self._rdata = None
        self._source = None
        self._tags = None
        self._ttl = None
        self._type = None
        self._view = None
        self._view_name = None
        self._zone = None
        self.discriminator = None

        if absolute_name_spec is not None:
            self.absolute_name_spec = absolute_name_spec
        if absolute_zone_name is not None:
            self.absolute_zone_name = absolute_zone_name
        if comment is not None:
            self.comment = comment
        if disabled is not None:
            self.disabled = disabled
        if dns_absolute_name_spec is not None:
            self.dns_absolute_name_spec = dns_absolute_name_spec
        if dns_absolute_zone_name is not None:
            self.dns_absolute_zone_name = dns_absolute_zone_name
        if dns_name_in_zone is not None:
            self.dns_name_in_zone = dns_name_in_zone
        if dns_rdata is not None:
            self.dns_rdata = dns_rdata
        if id is not None:
            self.id = id
        if inheritance_sources is not None:
            self.inheritance_sources = inheritance_sources
        if name_in_zone is not None:
            self.name_in_zone = name_in_zone
        if options is not None:
            self.options = options
        if rdata is not None:
            self.rdata = rdata
        if source is not None:
            self.source = source
        if tags is not None:
            self.tags = tags
        if ttl is not None:
            self.ttl = ttl
        self.type = type
        if view is not None:
            self.view = view
        if view_name is not None:
            self.view_name = view_name
        self.zone = zone

    @property
    def absolute_name_spec(self):
        """Gets the absolute_name_spec of this DataRecord.  # noqa: E501


        :return: The absolute_name_spec of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._absolute_name_spec

    @absolute_name_spec.setter
    def absolute_name_spec(self, absolute_name_spec):
        """Sets the absolute_name_spec of this DataRecord.


        :param absolute_name_spec: The absolute_name_spec of this DataRecord.  # noqa: E501
        :type: str
        """

        self._absolute_name_spec = absolute_name_spec

    @property
    def absolute_zone_name(self):
        """Gets the absolute_zone_name of this DataRecord.  # noqa: E501

        ReadOnly. The absolute domain name of the zone where this record belongs.  # noqa: E501

        :return: The absolute_zone_name of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._absolute_zone_name

    @absolute_zone_name.setter
    def absolute_zone_name(self, absolute_zone_name):
        """Sets the absolute_zone_name of this DataRecord.

        ReadOnly. The absolute domain name of the zone where this record belongs.  # noqa: E501

        :param absolute_zone_name: The absolute_zone_name of this DataRecord.  # noqa: E501
        :type: str
        """

        self._absolute_zone_name = absolute_zone_name

    @property
    def comment(self):
        """Gets the comment of this DataRecord.  # noqa: E501

        Optional. Comment for the object.  # noqa: E501

        :return: The comment of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DataRecord.

        Optional. Comment for the object.  # noqa: E501

        :param comment: The comment of this DataRecord.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def disabled(self):
        """Gets the disabled of this DataRecord.  # noqa: E501

        Optional. True if the object is disabled. A disabled object is effectively non-existent when generating configuration.  # noqa: E501

        :return: The disabled of this DataRecord.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this DataRecord.

        Optional. True if the object is disabled. A disabled object is effectively non-existent when generating configuration.  # noqa: E501

        :param disabled: The disabled of this DataRecord.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def dns_absolute_name_spec(self):
        """Gets the dns_absolute_name_spec of this DataRecord.  # noqa: E501


        :return: The dns_absolute_name_spec of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._dns_absolute_name_spec

    @dns_absolute_name_spec.setter
    def dns_absolute_name_spec(self, dns_absolute_name_spec):
        """Sets the dns_absolute_name_spec of this DataRecord.


        :param dns_absolute_name_spec: The dns_absolute_name_spec of this DataRecord.  # noqa: E501
        :type: str
        """

        self._dns_absolute_name_spec = dns_absolute_name_spec

    @property
    def dns_absolute_zone_name(self):
        """Gets the dns_absolute_zone_name of this DataRecord.  # noqa: E501

        ReadOnly. The DNS protocol textual representation of the absolute domain name of the zone where this record belongs.  # noqa: E501

        :return: The dns_absolute_zone_name of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._dns_absolute_zone_name

    @dns_absolute_zone_name.setter
    def dns_absolute_zone_name(self, dns_absolute_zone_name):
        """Sets the dns_absolute_zone_name of this DataRecord.

        ReadOnly. The DNS protocol textual representation of the absolute domain name of the zone where this record belongs.  # noqa: E501

        :param dns_absolute_zone_name: The dns_absolute_zone_name of this DataRecord.  # noqa: E501
        :type: str
        """

        self._dns_absolute_zone_name = dns_absolute_zone_name

    @property
    def dns_name_in_zone(self):
        """Gets the dns_name_in_zone of this DataRecord.  # noqa: E501

        ReadOnly. The DNS protocol textual representation of the relative owner name.  # noqa: E501

        :return: The dns_name_in_zone of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._dns_name_in_zone

    @dns_name_in_zone.setter
    def dns_name_in_zone(self, dns_name_in_zone):
        """Sets the dns_name_in_zone of this DataRecord.

        ReadOnly. The DNS protocol textual representation of the relative owner name.  # noqa: E501

        :param dns_name_in_zone: The dns_name_in_zone of this DataRecord.  # noqa: E501
        :type: str
        """

        self._dns_name_in_zone = dns_name_in_zone

    @property
    def dns_rdata(self):
        """Gets the dns_rdata of this DataRecord.  # noqa: E501

        ReadOnly. The DNS protocol textual representation of the record data.  # noqa: E501

        :return: The dns_rdata of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._dns_rdata

    @dns_rdata.setter
    def dns_rdata(self, dns_rdata):
        """Sets the dns_rdata of this DataRecord.

        ReadOnly. The DNS protocol textual representation of the record data.  # noqa: E501

        :param dns_rdata: The dns_rdata of this DataRecord.  # noqa: E501
        :type: str
        """

        self._dns_rdata = dns_rdata

    @property
    def id(self):
        """Gets the id of this DataRecord.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataRecord.

        The resource identifier.  # noqa: E501

        :param id: The id of this DataRecord.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inheritance_sources(self):
        """Gets the inheritance_sources of this DataRecord.  # noqa: E501

        Optional. Inheritance configuration.  # noqa: E501

        :return: The inheritance_sources of this DataRecord.  # noqa: E501
        :rtype: DataRecordInheritance
        """
        return self._inheritance_sources

    @inheritance_sources.setter
    def inheritance_sources(self, inheritance_sources):
        """Sets the inheritance_sources of this DataRecord.

        Optional. Inheritance configuration.  # noqa: E501

        :param inheritance_sources: The inheritance_sources of this DataRecord.  # noqa: E501
        :type: DataRecordInheritance
        """

        self._inheritance_sources = inheritance_sources

    @property
    def name_in_zone(self):
        """Gets the name_in_zone of this DataRecord.  # noqa: E501

        Required, writeable on create, readonly otherwise. The relative owner name to the zone origin.  # noqa: E501

        :return: The name_in_zone of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._name_in_zone

    @name_in_zone.setter
    def name_in_zone(self, name_in_zone):
        """Sets the name_in_zone of this DataRecord.

        Required, writeable on create, readonly otherwise. The relative owner name to the zone origin.  # noqa: E501

        :param name_in_zone: The name_in_zone of this DataRecord.  # noqa: E501
        :type: str
        """

        self._name_in_zone = name_in_zone

    @property
    def options(self):
        """Gets the options of this DataRecord.  # noqa: E501


        :return: The options of this DataRecord.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DataRecord.


        :param options: The options of this DataRecord.  # noqa: E501
        :type: TypesJSONValue
        """

        self._options = options

    @property
    def rdata(self):
        """Gets the rdata of this DataRecord.  # noqa: E501

        Required. JSON representation of resource record data.  # noqa: E501

        :return: The rdata of this DataRecord.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """Sets the rdata of this DataRecord.

        Required. JSON representation of resource record data.  # noqa: E501

        :param rdata: The rdata of this DataRecord.  # noqa: E501
        :type: TypesJSONValue
        """

        self._rdata = rdata

    @property
    def source(self):
        """Gets the source of this DataRecord.  # noqa: E501

        ReadOnly. RR type-specific non-protocol record source. The source is a combination of indicators, each tracking how resource record appeared in system. Listed below are source indicators with their meaning:   Source indicator     | Description ----------------     | -------------------------------- STATIC               |  Record was created manually by API call to dns/record. Valid for all record types except SOA. SYSTEM               |  Record was created automatically based on name server assignment. Valid for SOA, NS, A, AAAA, PTR record types. DYNAMIC              |  Record was created dynamically by performing dynamic update. STATIC, SYSTEM       |  Record was created manually by API call but it is obfuscated by record generated based on name server assignment. DYNAMIC, SYSTEM      |  Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment.  # noqa: E501

        :return: The source of this DataRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DataRecord.

        ReadOnly. RR type-specific non-protocol record source. The source is a combination of indicators, each tracking how resource record appeared in system. Listed below are source indicators with their meaning:   Source indicator     | Description ----------------     | -------------------------------- STATIC               |  Record was created manually by API call to dns/record. Valid for all record types except SOA. SYSTEM               |  Record was created automatically based on name server assignment. Valid for SOA, NS, A, AAAA, PTR record types. DYNAMIC              |  Record was created dynamically by performing dynamic update. STATIC, SYSTEM       |  Record was created manually by API call but it is obfuscated by record generated based on name server assignment. DYNAMIC, SYSTEM      |  Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment.  # noqa: E501

        :param source: The source of this DataRecord.  # noqa: E501
        :type: list[str]
        """

        self._source = source

    @property
    def tags(self):
        """Gets the tags of this DataRecord.  # noqa: E501


        :return: The tags of this DataRecord.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DataRecord.


        :param tags: The tags of this DataRecord.  # noqa: E501
        :type: TypesJSONValue
        """

        self._tags = tags

    @property
    def ttl(self):
        """Gets the ttl of this DataRecord.  # noqa: E501

        Record time to live value in seconds.  # noqa: E501

        :return: The ttl of this DataRecord.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DataRecord.

        Record time to live value in seconds.  # noqa: E501

        :param ttl: The ttl of this DataRecord.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def type(self):
        """Gets the type of this DataRecord.  # noqa: E501


        :return: The type of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataRecord.


        :param type: The type of this DataRecord.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def view(self):
        """Gets the view of this DataRecord.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The view of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this DataRecord.

        The resource identifier.  # noqa: E501

        :param view: The view of this DataRecord.  # noqa: E501
        :type: str
        """

        self._view = view

    @property
    def view_name(self):
        """Gets the view_name of this DataRecord.  # noqa: E501

        ReadOnly. Display name of dns/view. Synthetic field based on parent zone’s view.  # noqa: E501

        :return: The view_name of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this DataRecord.

        ReadOnly. Display name of dns/view. Synthetic field based on parent zone’s view.  # noqa: E501

        :param view_name: The view_name of this DataRecord.  # noqa: E501
        :type: str
        """

        self._view_name = view_name

    @property
    def zone(self):
        """Gets the zone of this DataRecord.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The zone of this DataRecord.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this DataRecord.

        The resource identifier.  # noqa: E501

        :param zone: The zone of this DataRecord.  # noqa: E501
        :type: str
        """
        if zone is None:
            raise ValueError("Invalid value for `zone`, must not be `None`")  # noqa: E501

        self._zone = zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DataRecord, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other