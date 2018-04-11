class Stack:
							#”””LIFO Stack implementation using a Python list as underlying storage.”””
	def __init__(self):
							#Create an empty stack.
		self._data = []
		self._track = None
							   # nonpublic list instance
	def track(self):
		return self._track
	def __len__(self):
						#Return the number of elements in the stack.
		return len(self._data)
	
	def is_empty(self):
							#Return True if the stack is empty.
		return len(self._data) == 0
		
	def return_last(self):
		return self._data[-1] 
		
	def return_second_last(self):
		return self._data[-2]
		
	def results(self):
		return self._data[-1]
		
	def operations(self,m):
		
		 
		if len(self._data) == 1: 
			
			self._track = 1 
		else:
			last = self.pop()
			second = self.pop()

			
			if m == '+' :
				temp = second  + last 
			
		
			elif m ==  '-':
				temp = second - last 
			
			elif m ==  '*':
				temp = second * last 
			
			elif m ==  '/':
				temp = second / last 
			
			elif m ==  '%':
				temp = second % last 
			
			elif m ==  '^':
				temp = second ^ last 
		
		
			
			self.push(temp)
	
	
		
	def push(self, e):
								 #Add element e to the top of the stack.
		self._data.append(e)  # new item stored at end of list
	
	def top(self):
								#Return (but do not remove) the element at the top of the stack.
								#Raise Empty exception if the stack is empty.
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]	# the last item in the list
	
	def pop(self):
								  #Remove and return the element from the top of the stack (i.e., LIFO).
									#Raise Empty exception if the stack is empty.
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop( )		 # remove last item from list
 

execute = Stack()

x = input("Enter postfix operation seperate operaters and opperands by space:")
postfix = x.split()

for element in postfix:
	check = element.isdigit()
	if check == True: 
		execute.push(eval(element) )  #add element to the top of stack 
		
		
	else:	   
		execute.operations(element)

   
if execute.track() == 1:
	print ("The postfix expression is invalid.")
	
else:
	answer = execute.return_last()
	print ("The answer is : " , answer)
	
	
