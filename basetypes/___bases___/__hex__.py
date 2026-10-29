"""
Utility class for hexadecimal conversion operations.
Provides methods to convert between bytes and hexadecimal strings.
"""

import binascii


class Hex:
    """
    Utility class for hexadecimal conversion operations.
    Provides methods to convert between bytes and hexadecimal strings.
    """

    @staticmethod
    def bytes_to_hex(data_bytes: bytes) -> str:
        """
        Convert bytes to hexadecimal string.

        Args:
            data_bytes: Input bytes to convert

        Returns:
            Hexadecimal string representation

        Raises:
            ValueError: If input is not bytes type

        Example:
            >>> Hex.bytes_to_hex(b'hello')
            '68656c6c6f'
        """
        if not isinstance(data_bytes, bytes):
            raise ValueError("Input must be of type bytes")
        return binascii.hexlify(data_bytes).decode('ascii')

    @property
    def ihex(self):
        """
        Property that converts the instance to hexadecimal string.
        Assumes the instance is a bytes object.

        Returns:
            Hexadecimal string representation

        Example:
            >>> bytes_data = b'hello'
            >>> bytes_data.ihex
            '68656c6c6f'
        """
        return self.bytes_to_hex(self)