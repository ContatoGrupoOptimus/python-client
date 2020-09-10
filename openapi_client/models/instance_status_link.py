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


class InstanceStatusLink(object):
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
        'label': 'str',
        'link': 'str'
    }

    attribute_map = {
        'label': 'label',
        'link': 'link'
    }

    def __init__(self, label=None, link=None):  # noqa: E501
        """InstanceStatusLink - a model defined in OpenAPI"""  # noqa: E501

        self._label = None
        self._link = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if link is not None:
            self.link = link

    @property
    def label(self):
        """Gets the label of this InstanceStatusLink.  # noqa: E501

        Link caption for the button  # noqa: E501

        :return: The label of this InstanceStatusLink.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this InstanceStatusLink.

        Link caption for the button  # noqa: E501

        :param label: The label of this InstanceStatusLink.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def link(self):
        """Gets the link of this InstanceStatusLink.  # noqa: E501

        Reference URL instead of method  # noqa: E501

        :return: The link of this InstanceStatusLink.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InstanceStatusLink.

        Reference URL instead of method  # noqa: E501

        :param link: The link of this InstanceStatusLink.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if not isinstance(other, InstanceStatusLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
