
sequence = [int(x) for x in input("enter a sequence of numbers seperated by space").split()]



start = 0
finish = len(sequence)-1
end = (len(sequence)) -1 


def rearrange(number,start,end):
    
    final_arranged=[]
    
    if  start == finish:
        return final_arranged 
    
    elif (number[start]%2) == 0:
        final_arranged.insert(start, number[start])
        start = start +1 
        return rearrange(number,start,end)
    
    elif (number[start]%2) == 1:
        final_arranged.insert(start, number[end])
        end = end -1 
        return rearrange(number,start,end)

final = rearrange(sequence,start,end)
print (final)
