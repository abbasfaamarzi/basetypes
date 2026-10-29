"""
Utility class for byte conversion operations.
Provides methods to convert between hexadecimal strings and bytes.
"""

import binascii


class Bytes :
    """
    Utility class for byte conversion operations.
    Provides methods to convert between hexadecimal strings and bytes.
    """

    @staticmethod
    def hex_to_bytes (hex_string: str) -> bytes :
        """
        Convert hexadecimal string to bytes.

        Args:
            hex_string: Hexadecimal string to convert

        Returns:
            Bytes representation

        Raises:
            ValueError: If input is not string or has invalid format

        Example:
            >>> Bytes.hex_to_bytes('68656c6c6f')
            b'hello'
        """
        if not isinstance ( hex_string , str ) :
            raise ValueError ( "Input must be of type string" )

        # Remove any non-hex characters and normalize to lowercase
        clean_hex = ''.join (
            c for c in hex_string if c.lower () in '0123456789abcdef'
        ).lower ()

        if len ( clean_hex ) % 2 != 0 :
            raise ValueError ( "Hex string must have even length" )

        return binascii.unhexlify ( clean_hex )

    @property
    def ibytes (self) :
        """
        Property that converts the instance to bytes.
        Assumes the instance is a hexadecimal string.

        Returns:
            Bytes representation of the hexadecimal string

        Example:
            >>> hex_string = '68656c6c6f'
            >>> hex_string.ibytes
            b'hello'
        """
        return self.hex_to_bytes ( self )