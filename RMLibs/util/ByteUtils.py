import struct
from base64 import b64decode


class ByteUtils:
    """
    A set of utilities for bytes and byte arrays
    """
    SIZEOF_INT_16 = 2
    SIZEOF_INT_32 = 4
    SIZEOF_INT_64 = 8
    SIZEOF_FLOAT = 4
    SIZEOF_DOUBLE = 8

    def __init__(self):
        pass

    @staticmethod
    def bytes_to_hex_string(byte_array: bytearray) -> str:
        """
        converts a byte array in a string with hexadecimal representation of the array itself
        :param byte_array: the byte array in input
        :return: the string representing the array in hexadecimal format
        """
        res = ''.join('{:02x}'.format(x) for x in byte_array)
        return res

    @staticmethod
    def bytes_to_short(byte_array: bytearray) -> int:
        """
        Converts the byte array in a short integer
        :param byte_array: the byte array
        :return: the short integer
        """
        res = struct.unpack_from('h', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_unsigned_short(byte_array: bytearray) -> int:
        """
        Converts the byte array in an unsigned short integer
        :param byte_array: the byte array
        :return: the unsigned short integer
        """
        res = struct.unpack_from('H', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_int(byte_array: bytearray) -> int:
        """
        Converts the byte array in an integer
        :param byte_array: the byte array
        :return: the integer
        """
        res = struct.unpack_from('i', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_long(byte_array: bytearray) -> int:
        """
        Converts the byte array in a long integer
        :param byte_array: the byte array
        :return: the long integer
        """
        res = struct.unpack_from('l', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_unsigned_long(byte_array: bytearray) -> int:
        """
        Converts the byte array in an unsigned long integer
        :param byte_array: the byte array
        :return: the unsigned long integer
        """
        res = struct.unpack_from('L', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_unsigned_int(byte_array: bytearray) -> int:
        """
        Converts the byte array in an unsigned integer
        :param byte_array: the byte array
        :return: the unsigned integer
        """
        res = struct.unpack_from('I', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_float(byte_array: bytearray) -> float:
        """
        Converts the byte array to a float
        :param byte_array: the byte array
        :return: the float number
        """
        res = struct.unpack_from('f', byte_array)
        return res[0]

    @staticmethod
    def bytes_to_double(byte_array: bytearray) -> float:
        """
        Converts the byte array to a double precision float
        :param byte_array: the byte array
        :return: the double precision float
        """
        res = struct.unpack_from('d', byte_array)
        return res[0]

    @staticmethod
    def int_to_bytes(value: int, length: int) -> bytearray:
        """
        Converts the integer number to a byte array
        :param value: the integer number
        :param length: the length of the byte array
        :return: the byte array
        """
        result = bytearray()
        for i in range(0, length):
            result.append(value >> (i * 8) & 0xff)
        # END for
        result.reverse()
        return result

    @staticmethod
    def bytes_to_string(byte_array: bytearray) -> str:
        """
        Converts the byte array to a string
        :param byte_array: the byte array
        :return: the string
        """
        return byte_array.decode('utf-8')

    @staticmethod
    def base64_decode(stream: str) -> bytes:
        """
        Converts a base64 decoded string in bytes
        :param stream: the string with the encoded byte stream
        :return: the bytes
        """
        return b64decode(stream)
