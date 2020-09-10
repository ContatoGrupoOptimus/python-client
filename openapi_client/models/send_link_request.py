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


class SendLinkRequest(object):
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
        'chat_id': 'str',
        'phone': 'int',
        'body': 'str',
        'preview_base64': 'str',
        'title': 'str',
        'description': 'str'
    }

    attribute_map = {
        'chat_id': 'chatId',
        'phone': 'phone',
        'body': 'body',
        'preview_base64': 'previewBase64',
        'title': 'title',
        'description': 'description'
    }

    def __init__(self, chat_id=None, phone=None, body=None, preview_base64=None, title=None, description=None):  # noqa: E501
        """SendLinkRequest - a model defined in OpenAPI"""  # noqa: E501

        self._chat_id = None
        self._phone = None
        self._body = None
        self._preview_base64 = None
        self._title = None
        self._description = None
        self.discriminator = None

        if chat_id is not None:
            self.chat_id = chat_id
        if phone is not None:
            self.phone = phone
        self.body = body
        self.preview_base64 = preview_base64
        self.title = title
        if description is not None:
            self.description = description

    @property
    def chat_id(self):
        """Gets the chat_id of this SendLinkRequest.  # noqa: E501

        **Required if phone is not set**  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. Used instead of the phone parameter.  # noqa: E501

        :return: The chat_id of this SendLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """Sets the chat_id of this SendLinkRequest.

        **Required if phone is not set**  Chat ID from the message list. Examples: 17633123456@c.us for private messages and 17680561234-1479621234@g.us for the group. Used instead of the phone parameter.  # noqa: E501

        :param chat_id: The chat_id of this SendLinkRequest.  # noqa: E501
        :type: str
        """

        self._chat_id = chat_id

    @property
    def phone(self):
        """Gets the phone of this SendLinkRequest.  # noqa: E501

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :return: The phone of this SendLinkRequest.  # noqa: E501
        :rtype: int
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SendLinkRequest.

        **Required if chatId is not set**  A phone number starting with the country code. You do not need to add your number.   USA example: 17472822486.  # noqa: E501

        :param phone: The phone of this SendLinkRequest.  # noqa: E501
        :type: int
        """

        self._phone = phone

    @property
    def body(self):
        """Gets the body of this SendLinkRequest.  # noqa: E501

        HTTP or HTTPS link, for example *https://wikimedia.org*  # noqa: E501

        :return: The body of this SendLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendLinkRequest.

        HTTP or HTTPS link, for example *https://wikimedia.org*  # noqa: E501

        :param body: The body of this SendLinkRequest.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def preview_base64(self):
        """Gets the preview_base64 of this SendLinkRequest.  # noqa: E501

        Base64-encoded file with mime data, for example *data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...* for link's preview  # noqa: E501

        :return: The preview_base64 of this SendLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._preview_base64

    @preview_base64.setter
    def preview_base64(self, preview_base64):
        """Sets the preview_base64 of this SendLinkRequest.

        Base64-encoded file with mime data, for example *data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ...* for link's preview  # noqa: E501

        :param preview_base64: The preview_base64 of this SendLinkRequest.  # noqa: E501
        :type: str
        """
        if preview_base64 is None:
            raise ValueError("Invalid value for `preview_base64`, must not be `None`")  # noqa: E501

        self._preview_base64 = preview_base64

    @property
    def title(self):
        """Gets the title of this SendLinkRequest.  # noqa: E501

        Title for send link  # noqa: E501

        :return: The title of this SendLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SendLinkRequest.

        Title for send link  # noqa: E501

        :param title: The title of this SendLinkRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this SendLinkRequest.  # noqa: E501

        Description for send link  # noqa: E501

        :return: The description of this SendLinkRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SendLinkRequest.

        Description for send link  # noqa: E501

        :param description: The description of this SendLinkRequest.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, SendLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
