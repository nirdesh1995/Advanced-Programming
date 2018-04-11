
class ArrayQueue:
    
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY   #create an empty queue 
        self._data_price = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 
        self._front = 0 
        self._cap_gain = 0 
      
        self._total_shares = 0
    
    def return_value(self):
        return self._cap_gain
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0 
    
    def first(self):   #return but  do not remove first element 
        if self.is_empty( ):
            raise Empty("queue is empty")
        return self._data[self._front]
        
    def dequeue(self):           #remove and return first element of the queue 
        if self.is_empty( ):
            raise Empty("queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1 
        return answer 
    
    def enqueue(self,e):       #Add element to the back of a queue 
        if self._size == len(self._data):
            self._resize(2*len(self._data))
            self._resize(2*len(self._data_price))     #resizing the price storage 
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e[0]
        self._total_shares = self._total_shares + e[0]
        self._data_price[avail] = e[1]
        self._size += 1 
        
    def selling(self,m):
    	
        if m[0] < self._data[self._front]:
            change = self._data[self._front] - m[0]
            self._cap_gain = self._cap_gain + (m[0] *( m[1] - self._data_price[self._front]) )
            self._total_shares = self._total_shares - m[0]
            self._data[self._front] = change
            
            
			
			
        else:
            if m[0] > self._total_shares:
                print ( "sell" , m[0] , "is larger than all the shares", self._total_shares) 
             
            else:
                extra = m[0] - self._data[self._front] 
                m[0] = extra            				#for the next loop 
                self._cap_gain = self._cap_gain + (self._data[self._front] *(m[1]- self._data_price[self._front]) )
                self._total_shares = self._total_shares - m[0]
                self._data[self._front] = None 
                self._data_price[self._front] = None
                self._front = (self._front + 1) % len(self._data)
                self._size -= 1
			
			
                self.selling(m)    #Recursion 
        
    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap 
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0 



store=[]
send= []
execute = ArrayQueue()
try:          
     while True:
        x = input("Input transaction order  : ")
        store.append(x)             #Storing the lines 

except EOFError: 
        for element in store:    			 
            temp = [int(s) for s in element.split() if s.isdigit() ]  #splitting the numbers
            order = element.partition(' ')[0]    #deciding order 
            if order == 'buy': 
                execute.enqueue(temp)          
            else: 
                execute.selling(temp)
                    
       	xyz = execute.return_value()  
       	print("\n")     
        print("Total Capital Gain = " , xyz ) 