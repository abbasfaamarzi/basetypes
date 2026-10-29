"""
Mixin class for enhanced iteration operations on sequence types.
Provides navigation, movement, and traversal methods.
"""

import copy


class Iter :
    """
    Mixin class for enhanced iteration operations on sequence types.
    Provides navigation, movement, and traversal methods.
    """

    loop = False

    @property
    def current_index_value (self) :
        """
        Property to get the value at current index.

        Returns:
            Value at the current index position

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.current_index = 1
            >>> my_list.current_index_value
            'b'
        """
        return self[self.current_index]

    @property
    def last_value_index (self) :
        """
        Property to get the index of the last element.

        Returns:
            Index of the last element

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.last_value_index
            2
        """
        return self.index ( self.last_element )

    @property
    def next (self) :
        """
        Method to get the next element in the sequence.

        Returns:
            The next element in the sequence

        Raises:
            StopIteration: If the end of the sequence is reached

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.current_index = 0
            >>> my_list.next
            'b'
        """
        if self.current_index_value == self.last_element :
            if self.loop :
                self.current_index = 0
                return self.current_index_value
            else :
                raise StopIteration ( "End of sequence reached" )
        else :
            self.current_index += 1
            return self.current_index_value

    @property
    def previous (self) :
        """
        Method to get the previous element in the sequence.

        Returns:
            The previous element in the sequence

        Raises:
            StopIteration: If the beginning of the sequence is reached

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.current_index = 1
            >>> my_list.previous
            'a'
        """
        if self.current_index_value == self.first_element :
            if self.loop :
                self.current_index = copy.copy ( self.last_value_index )
                return self.last_element
            else :
                raise StopIteration ( "Beginning of sequence reached" )
        else :
            self.current_index -= 1
            return self.current_index_value

    def move_element (self , element_index , insert_index) :
        """
        Move an element from one position to another.

        Args:
            element_index: Index of element to move
            insert_index: Index where to insert the element

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.move_element(0, 2)
            >>> my_list
            ['b', 'a', 'c']
        """
        pop_element = self.pop ( element_index )
        self.insert ( insert_index , pop_element )

    def move_current_value_to_index (self , element_index) :
        """
        Move the current element to a new position.

        Args:
            element_index: Target index for the current element

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.current_index = 0
            >>> my_list.move_current_value_to_index(2)
            >>> my_list
            ['b', 'a', 'c']
        """
        self.move_element ( self.current_element , element_index )

    def nex_block (self) :
        """
        Move to the next element without returning it.

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.current_index = 0
            >>> my_list.nex_block()
            >>> my_list.current_index
            1
        """
        _ = self.next

    @property
    def both_end_of_the_lis (self) :
        """
        Property to get both first and last elements.

        Returns:
            Tuple containing first and last elements

        Example:
            >>> my_list = ['a', 'b', 'c']
            >>> my_list.both_end_of_the_lis
            ('a', 'c')
        """
        return self.first_element , self.last_element



"""
Mixin class for enhanced iteration operations on sequence types.
Provides navigation, movement, and traversal methods.
"""

import copy
import random


class IterChain :
    """
    Mixin class for enhanced iteration operations on sequence types.
    Provides navigation, movement, and traversal methods.
    """

    loop = False
    current_index = 0

    @property
    def length (self) :
        return len ( self )

    @property
    def current_index_value (self) :
        """
        Property to get the value at current index.

        Returns:
            Value at the current index position

        Example:
            >>> my_chian_list = {1:{}, 2:{}.3:{},}
            >>> my_chian_list.current_index = 1
            >>> my_chian_list.current_index_value
            'b'
        """
        return self.get ( self.current_index , None )

    @property
    def last_value_index (self) :
        """
        Property to get the index of the last element.

        Returns:
            Index of the last element

        Example:
            >>> my_chian_list = {1:{}, 2:{}.3:{},}
            >>> my_chian_list.last_value_index
            2
        """
        return max ( self.keys () )

    @property
    def new_index (self) :
        if self.length>1 :
            return self.last_value_index + 1
        return 1

    @property
    def last_element (self) :
        return self[self.last_value_index]

    @property
    def first_element (self) :
        return self[1]

    @property
    def next (self) :
        """
        Method to get the next element in the sequence.

        Returns:
            The next element in the sequence

        Raises:
            StopIteration: If the end of the sequence is reached

        Example:
            >>> my_chian_list = {1:{}, 2:{}.3:{},}
            >>> my_chian_list.current_index = 1
            >>> my_chian_list.next
            '{}'
        """
        if self.current_index_value == self.last_value_index :
            if self.loop :
                self.current_index = 1
                return self.current_index_value
            else :
                return None
        else :
            self.current_index += 1
            return self.current_index_value

    @property
    def previous (self) :
        """
        Method to get the previous element in the sequence.

        Returns:
            The previous element in the sequence

        Raises:
            StopIteration: If the beginning of the sequence is reached

        Example:
            >>> my_chian_list = {1:{}, 2:{}.3:{},}
            >>> my_chian_list.current_index = 1
            >>> my_chian_list.previous
            '{}'
        """
        if self.length > 1 :
            if self.current_index == 1 :
                if self.loop :
                    self.current_index = self.last_value_index
                    return self.current_index_value
                else :
                    return None
            else :
                self.current_index -= 1
                return self.current_index_value

        return None

    @property
    def both_end_of_the_lis (self) :
        """
        Property to get both first and last elements.

        Returns:
            Tuple containing first and last elements

        Example:
            >>> my_chian_list = {1:{}, 2:{}.3:{},}
            >>> my_chian_list.both_end_of_the_lis
            ('{}', '{}')
        """
        return self.first_element , self.last_element


if __name__ == "__main__" :
    class ChainDict ( IterChain , dict ) :
        pass


    chain = ChainDict (
        { index : { chr ( random.randrange ( ord ( "a" ) , ord ( "z" ) ) ) : 1 } for index in range ( 1 , 5 ) }
    )
    print ( chain )
    print ( 'previous' , chain.previous )
    print ( 'current_index_value' , chain.current_index_value )
    print ( 'next' , chain.next )
    print ( 'current_index_value' , chain.current_index_value )
    print ( 'previous' , chain.previous )
