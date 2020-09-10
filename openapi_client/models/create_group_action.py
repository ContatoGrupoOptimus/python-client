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


class CreateGroupAction(object):
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
        'group_name': 'str',
        'chat_ids': 'list[str]',
        'phones': 'list[int]',
        'message_text': 'str'
    }

    attribute_map = {
        'group_name': 'groupName',
        'chat_ids': 'chatIds',
        'phones': 'phones',
        'message_text': 'messageText'
    }

    def __init__(self, group_name=None, chat_ids=None, phones=None, message_text=None):  # noqa: E501
        """CreateGroupAction - a model defined in OpenAPI"""  # noqa: E501

        self._group_name = None
        self._chat_ids = None
        self._phones = None
        self._message_text = None
        self.discriminator = None

        self.group_name = group_name
        if chat_ids is not None:
            self.chat_ids = chat_ids
        if phones is not None:
            self.phones = phones
        if message_text is not None:
            self.message_text = message_text

    @property
    def group_name(self):
        """Gets the group_name of this CreateGroupAction.  # noqa: E501

        Name of the group being created  # noqa: E501

        :return: The group_name of this CreateGroupAction.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CreateGroupAction.

        Name of the group being created  # noqa: E501

        :param group_name: The group_name of this CreateGroupAction.  # noqa: E501
        :type: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def chat_ids(self):
        """Gets the chat_ids of this CreateGroupAction.  # noqa: E501

        **Required if phones is not set**  An array of new participients chatIds.   # noqa: E501

        :return: The chat_ids of this CreateGroupAction.  # noqa: E501
        :rtype: list[str]
        """
        return self._chat_ids

    @chat_ids.setter
    def chat_ids(self, chat_ids):
        """Sets the chat_ids of this CreateGroupAction.

        **Required if phones is not set**  An array of new participients chatIds.   # noqa: E501

        :param chat_ids: The chat_ids of this CreateGroupAction.  # noqa: E501
        :type: list[str]
        """

        self._chat_ids = chat_ids

    @property
    def phones(self):
        """Gets the phones of this CreateGroupAction.  # noqa: E501

        **Required if chatIds is not set**  An array of phones starting with the country code. You do not need to add your number.   USA example: [17472822486'].  # noqa: E501

        :return: The phones of this CreateGroupAction.  # noqa: E501
        :rtype: list[int]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this CreateGroupAction.

        **Required if chatIds is not set**  An array of phones starting with the country code. You do not need to add your number.   USA example: [17472822486'].  # noqa: E501

        :param phones: The phones of this CreateGroupAction.  # noqa: E501
        :type: list[int]
        """

        self._phones = phones

    @property
    def message_text(self):
        """Gets the message_text of this CreateGroupAction.  # noqa: E501

        The text of the message that will be sent to the group when it is created. If you do not set a parameter, the message will not be sent  # noqa: E501

        :return: The message_text of this CreateGroupAction.  # noqa: E501
        :rtype: str
        """
        return self._message_text

    @message_text.setter
    def message_text(self, message_text):
        """Sets the message_text of this CreateGroupAction.

        The text of the message that will be sent to the group when it is created. If you do not set a parameter, the message will not be sent  # noqa: E501

        :param message_text: The message_text of this CreateGroupAction.  # noqa: E501
        :type: str
        """

        self._message_text = message_text

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
        if not isinstance(other, CreateGroupAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
