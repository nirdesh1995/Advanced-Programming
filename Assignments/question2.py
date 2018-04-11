'''#question2
C-1.21 (30 points) Write a Python function that repeated reads lines from standard input until
an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of
input by typing ctrl-D).
Hint Use a list to store all the lines.
 '''
store=[]
try:          
     while True:
        x = input("enter a line ")
        store.append(x)             #Storing the lines 
    
except EOFError:                    
    for lines in reversed(store):   #Reversing the lines stored
        print(lines)