"""
Mixin class for indexing operations on sequence types.
Provides properties and methods for element access and index management.
"""


class Indexing :
    """
    Mixin class for indexing operations on sequence types.
    Provides properties and methods for element access and index management.
    """

    current_index = 0

    @property
    def first_element (self) :
        """
        Property to get the first element of the sequence.

        Returns:
            The first element of the sequence

        Example:
            >>> my_list = [1, 2, 3]
            >>> my_list.first_element
            1
        """
        return self[0]

    @property
    def last_element (self) :
        """
        Property to get the last element of the sequence.

        Returns:
            The last element of the sequence

        Example:
            >>> my_list = [1, 2, 3]
            >>> my_list.last_element
            3
        """
        if self:
            return self[-1]

        return None

    def set_index (self , value) :
        """
        Set the current index to the position of a specific value.

        Args:
            value: Value to find and set as current index

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.set_index('b')
            >>> my_list.current_index
            1
        """
        self.current_index = self.index ( value )