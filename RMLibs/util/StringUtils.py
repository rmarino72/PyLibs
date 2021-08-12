import base64


class StringUtils:
    """
    A set of utilities to manage strings
    """

    @staticmethod
    def empty_string(string_value: str) -> bool:
        """
        Verifies if the String is empty
        :param string_value: the string to verify
        :return: True or False
        """
        if string_value is None:
            return True
        return not (string_value.strip())

    @staticmethod
    def string_to_bytes(string_value: str) -> bytes:
        """
        Converts the String into a byte array
        :param string_value: the string
        :return: the byte array
        """
        return bytes(string_value, 'utf8')

    @staticmethod
    def encode_string_base64(string_value: str) -> str:
        """
        Returns the string encoded in BASE 64 format
        :param string_value: the string to encode
        :return: the encoded string
        """
        encoded_bytes: bytes = base64.b64encode(string_value.encode("utf-8"))
        encoded_string: str = str(encoded_bytes, "utf-8")
        return encoded_string

    @staticmethod
    def decode_string_base64(encoded_string: str) -> str:
        """
        Decodes the string from BASE 64 format
        :param encoded_string: the encoded string
        :return: the decoded string
        """
        decoded_bytes: bytes = base64.b64decode(encoded_string)
        decoded_string: str = str(decoded_bytes)
        return decoded_string
