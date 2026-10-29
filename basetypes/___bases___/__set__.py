"""
Mixin class for enhanced set operations.
Provides additional methods for set manipulation and operations.
"""


class SetOperation:
    """
    Mixin class for enhanced set operations.
    Provides additional methods for set manipulation and operations.
    """

    def add_element(self, element):
        """
        Add an element to the set.

        Args:
            element: Element to add to the set

        Example:
            >>> my_set = {1, 2, 3}
            >>> my_set.add_element(4)
            >>> my_set
            {1, 2, 3, 4}
        """
        self.add(element)

    def remove_element(self, element):
        """
        Remove an element from the set (if exists).

        Args:
            element: Element to remove from the set

        Example:
            >>> my_set = {1, 2, 3}
            >>> my_set.remove_element(2)
            >>> my_set
            {1, 3}
        """
        self.discard(element)

    def union(self, other_set):
        """
        Return the union of this set and another set.

        Args:
            other_set: Another set to union with

        Returns:
            New set containing all elements from both sets

        Example:
            >>> set1 = {1, 2}
            >>> set2 = {2, 3}
            >>> set1.union(set2)
            {1, 2, 3}
        """
        return self | other_set

    def intersection(self, other_set):
        """
        Return the intersection of this set and another set.

        Args:
            other_set: Another set to intersect with

        Returns:
            New set containing common elements

        Example:
            >>> set1 = {1, 2, 3}
            >>> set2 = {2, 3, 4}
            >>> set1.intersection(set2)
            {2, 3}
        """
        return self & other_set

    def difference(self, other_set):
        """
        Return the difference between this set and another set.

        Args:
            other_set: Another set to compare with

        Returns:
            New set containing elements in this set but not in other_set

        Example:
            >>> set1 = {1, 2, 3}
            >>> set2 = {2, 3, 4}
            >>> set1.difference(set2)
            {1}
        """
        return self - other_set

    def symmetric_difference(self, other_set):
        """
        Return the symmetric difference between this set and another set.

        Args:
            other_set: Another set to compare with

        Returns:
            New set containing elements in either set but not both

        Example:
            >>> set1 = {1, 2, 3}
            >>> set2 = {2, 3, 4}
            >>> set1.symmetric_difference(set2)
            {1, 4}
        """
        return self ^ other_set

    def contains(self, element):
        """
        Check if element exists in the set.

        Args:
            element: Element to check for existence

        Returns:
            Boolean indicating if element exists in the set

        Example:
            >>> my_set = {1, 2, 3}
            >>> my_set.contains(2)
            True
        """
        return element in self

    def clear_set(self):
        """
        Remove all elements from the set.

        Example:
            >>> my_set = {1, 2, 3}
            >>> my_set.clear_set()
            >>> my_set
            set()
        """
        self.clear()

    def get_elements(self):
        """
        Get all elements of the set.

        Returns:
            The set itself

        Example:
            >>> my_set = {1, 2, 3}
            >>> my_set.get_elements()
            {1, 2, 3}
        """
        return self