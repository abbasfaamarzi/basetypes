from ___bases___.__hash__ import ObjectHash


class DictObject(ObjectHash, dict):

    def __getattr__(self, field):
        """
        Gets the value of a field if it exists in the dictionary.

        Args:
            field (str): The field name to get the value for.

        Returns:
            The value of the field if it exists, None otherwise.
        """
        if field not in dir(self):
            if field in self.keys():
                return self[field]
            else:
                return None
        else:
            return None

    def __setattr__(self, field, value):
        """
        Sets the value of a field if it does not exist in the object's attributes.

        Args:
            field (str): The field name to set the value for.
            value: The value to set for the field.

        Returns:
            None
        """
        if field not in dir(self):
            self[field] = value
        else:
            return super().__setattr__(field, value)
