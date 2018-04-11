# setting global variables to be used within the function 


def testing(a,b,control):
    
    if b >= control:     #setting base case
        
        return a      #returning sorted list
    
    else :           #setting up the recursion 
        if a[b] %2  == 0 : 
            
            return testing(a,b+1,control)    
        else : 
            a.append(a[b])
            a.remove(a[b])
            
            return testing(a,b,control-1)
                
                
#sorting the input into a list of integers 
sequence = [int(x) for x in input("enter a sequence of numbers seperated by space").split()] 

# calling the function 


	
