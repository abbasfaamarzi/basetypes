import random



class DictAttr(dict):
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

    def __getattr__(self, field):
        return self[field]


class Vars:
    inheritance_names = []
    #inheritance_names.extend ( OsKeywords.INHERTAINCENAMES )

    @property
    def api (self) :
        return self.__class__

    @property
    def api_name (self) :
        return self.api.__name__

    @property
    def api_all_dict (self) :
        return self.api.__dict__.items ()

    @property
    def api_vars (self) :
        return DictAttr (
            { k : v for k , v in self.api_all_dict if not callable ( v ) and not isinstance (
                getattr ( self.api , k , None ) , property
            ) and k not in self.inheritance_names and not k.startswith ( "__" ) and not k.startswith ( "_" ) }
        )

    @property
    def api_vars_name (self) :
        return list ( self.api_vars.keys () )

    @property
    def api_vars_value (self) :
        return list ( self.api_vars.values () )

    @property
    def api_type (self) :
        return type ( self ).__name__
