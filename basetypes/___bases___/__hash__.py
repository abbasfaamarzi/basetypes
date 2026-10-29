"""
Utility class for hashing operations.
Provides methods for creating and verifying SHA-256 hashes.
"""

import hashlib
import json


class Hash:
    """
    Utility class for hashing operations.
    Provides methods for creating and verifying SHA-256 hashes.
    """

    @staticmethod
    def get_hash(data):
        if isinstance(data, (dict, list)):
            text = json.dumps(data, sort_keys=True)
        return hashlib.sha256(str(data).encode()).hexdigest()

    def hasher(self, text=None):
        """
        Hash text using SHA-256 algorithm.

        Args:
            text: Text to hash. If None, uses the instance itself

        Returns:
            Hexadecimal string representation of the hash

        Example:
            >>> Hash().hasher('hello')
            '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730...'
        """
        text = text if text else self
        return Hash.get_hash(text)

    def is_valid(self, text, text_hash):
        """
        Verify if the hash of text matches the provided hash.

        Args:
            text: Original text to verify
            text_hash: Hash to compare against

        Returns:
            Boolean indicating if the hash is valid

        Example:
            >>> Hash().is_valid('hello', expected_hash)
            True
        """
        return self.hasher(text) == text_hash


class ObjectHash(Hash):

    @property
    def ihash (self) :
        return self.hasher(self)

    def ihash_eq_hash_of(self, text):
        return self.is_valid(self, text)