import copy
from __iter__ import IterChain
from __dict__ import ObjectHash, DictObject


class LedgerPagesChain(ObjectHash, IterChain, dict):

    def new_page(self, data : dict):
        self.current_index = self.length +  1
        data["previous_hash"] = "0"
        if self.current_index >1:
            data["previous_hash"] = self.hasher(self[self.current_index -1])

        self[self.current_index] = data

    def update_page(self, data : dict, page_index = None):
        page_index = page_index if page_index else self.current_index
        self[page_index] = data

    def delete_page(self, page_index = None):
        page_index = page_index if page_index else self.current_index
        del self[page_index]

    @property
    def current_page(self):
        if self.current_index_value:
            return DictObject(self.current_index_value)
        return None

    def generate_chain(self):
        last_index = copy.copy(self.current_index)
        for page_index in sorted ( self.keys () ) :
            self.current_index = page_index
            if self.current_index > 1 :
                print ( 'previous' , self.current_index )
                self.current_page['previous_hash'] = self.hasher ( self[self.current_index - 1] )

        else:
            self.current_index = last_index

    @property
    def is_valid_chain(self):
        last_index = copy.copy ( self.current_index )

        for page_index in sorted(self.keys()):
            self.current_index = page_index
            if self.current_index >1:
                if not self.current_page['previous_hash'] == self.hasher(self[self.current_index -1]):
                    self.current_index = last_index
                    return False

        else:
           self.current_index = last_index


        return True

    def generate_previous_hash(self):
        try:
            self[self.current_index]['previous_hash'] = self.hasher(self[self.current_index])
            print(self[self.current_index])
        except TypeError:
            self[self.current_index]['previous_hash'] = "0"



# ============ UTILITY FUNCTIONS ============


