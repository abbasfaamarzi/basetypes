"""
Base types module containing utility classes for various data type operations.
This module provides mixins and utility classes for enhanced operations on
standard Python data types.
"""

from _chain_ import IterChain
from __hash__ import Hash, ObjectHash

from __bytes__ import Bytes
from __hex__ import Hex
from __iter__ import Iter, IterChain
from __index__ import Indexing
from __name__ import SnakePascalName
from __set__ import SetOperation
from _magics_ import Vars


__all__ = [
    'IterChain',
    'Bytes',
    'Hash',
    'Hex',
    'Iter',
    'Indexing',
    'SnakePascalName',
    'SetOperation',
    "ObjectHash",
    "Vars"
]

__version__ = '1.0.0'
__author__ = 'AbsFrFi'
__description__ = 'Utility classes for enhanced data type operations in Python'