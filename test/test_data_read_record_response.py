# coding: utf-8

"""
    DNS Data API

    The DNS Data is a BloxOne DDI service providing primary authoritative zone support. DNS Data is authoritative for all DNS resource records and is acting as a primary DNS server. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bloxonednsdata
from bloxonednsdata.models.data_read_record_response import DataReadRecordResponse  # noqa: E501
from bloxonednsdata.rest import ApiException


class TestDataReadRecordResponse(unittest.TestCase):
    """DataReadRecordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataReadRecordResponse(self):
        """Test DataReadRecordResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = bloxonednsdata.models.data_read_record_response.DataReadRecordResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
