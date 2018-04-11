
class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'            # streamline memory
        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                           # user's element
            self._prev = prev                                 # previous node reference
            self._next = next                                 # next node reference
#-------------------------- list constructor --------------------------
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0                                      # number of elements
#-------------------------- public accessors --------------------------
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
#-------------------------- nonpublic utilities --------------------------
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
    
        def element(self):
            return self._node._element
      
        def __eq__(self, other):
     
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            return not (self == other)               # opposite of __eq__
    
#------------------------------- utility methods -------------------------------
    def _validate(self, p):
   
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None                              # boundary violation
        else:
            return self.Position(self, node)         # legitimate position
    
#------------------------------- accessors -------------------------------
    def first(self):
        return self._make_position(self._header._next)
    def last(self):
        return self._make_position(self._trailer._prev)
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
#------------------------------- mutators -------------------------------
  # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
   
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
   
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element
   
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element       # temporarily store old element
        original._element = e               # replace with new element
        return old_value                    # return the old element value
		
		
#-----------------------------------------------------------------------------------		
		
		
    def find(self, e):

    	
        temp = self.first()                  #start from the first element 
        try:
            while (temp.element()) != e:   #keep looping until a match is found 
                temp = self.after(temp)
            return self._make_position(temp)    #send position of first instance 
        
        except:
            return None                       	#if none is found send  None 
            
if __name__ == "__main__":

    L = PositionalList()
    L.add_first(1)
    L.add_first(2)
    L.add_first(3)
    L.add_last(4)
    L.add_first(6)
    L.add_first(8)
    L.add_first(8)
    L.add_first(8)
    L.add_first(8) 
    
       
    result = L.find(0)
    
    if result == None:
        print("not found")
    else:
        print(result)
    
        
    result = L.find(8)
    if result == None:
        print("not found")
    else:
        print(result)

