
def min_max(a,b,control,maxx = None , minn = None): 

    if b >= control:   #setting base case
        return  maxx, minn      #returning the final min and max values 
    
    else :           #setting up the recursion 
        if maxx == None: maxx = a[0]
        elif minn == None: minn = a[0]
        elif a[b] >= maxx : 

            maxx = a[b]
            
        elif a[b] <= minn: 
            minn = a[b]
            
        return min_max(a,b+1,control,maxx,minn)    

if __name__=="__main__": 
    
    sequence = [int(x) for x in input("enter a sequence of numbers seperated by space").split()] 	
    the_end = min_max(sequence, 0, len(sequence))
    print ("the maximum and minimum values are ") 
    print (the_end)
