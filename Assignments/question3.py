#question3

'''C-1.27 (40 points) In Section 1.8, we provide three different implementations of a generator
that computes factors of a given integer (see the 2nd page if you do not have the textbook). The
third of those implementations, from page 41, was the most efficient, but we noted that it did
not yield the factors in increasing order. Modify the generator so that it reports factors in
increasing order, while maintaining its general performance advantages.
Hint Either buffer the bigger value from each pair of factors, or repeat the loop in reverse to
avoid the buffer.'''
def factors(): # generator that computes factors
    
    n = eval(input("write the number: "))
    k = 1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
        if k * k == n: # special case if n is perfect square
            yield k

list = []
storage = factors()  #shifting the factors to another list


for i in storage:     #loop
    list.append(i)    #adding to the list
    list.sort()        #sorting the list out in ascending order
print(list)