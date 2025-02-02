# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OutboundMessages(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total_messages': 'int',
        'first100': 'list[OutboundMessage]'
    }

    attribute_map = {
        'total_messages': 'totalMessages',
        'first100': 'first100'
    }

    def __init__(self, total_messages=None, first100=None):  # noqa: E501
        """OutboundMessages - a model defined in OpenAPI"""  # noqa: E501

        self._total_messages = None
        self._first100 = None
        self.discriminator = None

        if total_messages is not None:
            self.total_messages = total_messages
        if first100 is not None:
            self.first100 = first100

    @property
    def total_messages(self):
        """Gets the total_messages of this OutboundMessages.  # noqa: E501

        Total number of messages in the queue  # noqa: E501

        :return: The total_messages of this OutboundMessages.  # noqa: E501
        :rtype: int
        """
        return self._total_messages

    @total_messages.setter
    def total_messages(self, total_messages):
        """Sets the total_messages of this OutboundMessages.

        Total number of messages in the queue  # noqa: E501

        :param total_messages: The total_messages of this OutboundMessages.  # noqa: E501
        :type: int
        """

        self._total_messages = total_messages

    @property
    def first100(self):
        """Gets the first100 of this OutboundMessages.  # noqa: E501


        :return: The first100 of this OutboundMessages.  # noqa: E501
        :rtype: list[OutboundMessage]
        """
        return self._first100

    @first100.setter
    def first100(self, first100):
        """Sets the first100 of this OutboundMessages.


        :param first100: The first100 of this OutboundMessages.  # noqa: E501
        :type: list[OutboundMessage]
        """

        self._first100 = first100

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OutboundMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
