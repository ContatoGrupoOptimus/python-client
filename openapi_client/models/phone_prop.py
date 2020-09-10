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


class PhoneProp(object):
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
        'phone': 'int'
    }

    attribute_map = {
        'phone': 'phone'
    }

    def __init__(self, phone=None):  # noqa: E501
        """PhoneProp - a model defined in OpenAPI"""  # noqa: E501

        self._phone = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone

    @property
    def phone(self):
        """Gets the phone of this PhoneProp.  # noqa: E501

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :return: The phone of this PhoneProp.  # noqa: E501
        :rtype: int
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PhoneProp.

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :param phone: The phone of this PhoneProp.  # noqa: E501
        :type: int
        """

        self._phone = phone

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
        if not isinstance(other, PhoneProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
