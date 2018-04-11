class Empty(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'         # streamline memory usage
        def __init__(self, element, next):
            self._element = element
            self._next = next
  
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0                          # number of queue elements
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element             
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                     # removed head had been the tail
        return answer
    def enqueue(self, e):
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                   # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1
        
    
    
    def rotate(self):  
                
        if self.is_empty():
        	raise Empty('Queue is empty')
        else:									#chancing pointers 
            temp = self._head
            self._head = self._head._next    		
            self._tail._next = temp
            self._tail = temp
            temp._next = None
            
            
            
if __name__ =='__main__':
	Q = LinkedQueue()
	
	try:
		Q.dequeue()
		Q.rotate()
		
	except Empty as e:
		print(e.value)  
	
	try: 
		Q.enqueue(10)
		Q.enqueue(11)
		Q.enqueue(102)
		Q.enqueue(1034)
		Q.enqueue(1045)
		Q.enqueue(1056)
		Q.enqueue(2000)
		Q.enqueue(9999)
	except Empty as e: 
		print(e.value) 
		
	for i in range(len(Q)): 
		print(Q.first())
		Q.rotate()

	