'''
### #Question1
C-1.14 (30 points) Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose produce (multiplication
of the two elements in this pair) is odd.
Hint Note that both numbers in the pair must be odd.
###
'''

list=[]                             #creating a list
x = input("Please enter a sequence of integer values seperated by comma : ")
x = x.split(",")                    #taking the input correctly
for i in x:
        if eval(i) % 2 != 0:       #Calculating if a number is odd or even
            list.append(i)           #storing the odd ones in a list
    
    
print ("the following pair of numbers produce odd multiplication pairs")        
print (list)                        #Displaying the output
