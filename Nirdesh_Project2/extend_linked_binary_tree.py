

from linked_binary_tree import LinkedBinaryTree

class ExtendedLinkedBinaryTree(LinkedBinaryTree):


  #########################################################################

  def preorder_next(self,p):

    kids = self.num_children(p)

    #----------------For Internal Nodes--------------------#
    if  kids >= 1 : 
      if self.left(p) == None: 
        return (self.right(p).element())
      else:
        return (self.left(p).element())
    
    #----------------For External Nodes ---------------------#
    else: 
      parent = self.parent(p)
      root = self.root()
      if p == self.left(parent) and self.right(parent) != None: 
        return (self.right(parent).element())
      else: 
         
        while self.right(parent) == p or self.right(parent) == None: 
          p = self.parent(p)
          parent = self.parent(p)
        
        return (self.right(parent).element())

#############################################################################

  def inorder_next(self,p):              #left ---- Node----right 

    kids = self.num_children(p)
#----------------------------------For Internal  Nodes -------------------#


    if kids >= 1: 
      mark = 0
      x = p



      if self.right(p) != None:
        temp = self.right(p)
      
      else: 
        temp = p  
        mark = 1
        parent = self.parent(temp)

        
        while self.right(parent) == temp: 
          temp = self.parent(temp)
        
        temp = self.parent(temp)  
        node = self._validate(temp)
        return self.Position(self,node).element()

        

  #----------------------------------For External  Nodes ____________________#



      while self.left(temp) != None: 
        temp = self.left(temp)
      if mark == 0: 
        node = self._validate(temp)
        return self.Position(self,node).element()

    else: 
      parent = self.parent(p)
      while self.right(parent) == p:
        p = self.parent(p)
        parent = self.parent(p)

      p = self.parent(p)
      node = self._validate(p)
      return self.Position(self,node).element()




###################################################################################

  def postorder_next(self,p):          #left ----Right---- Node




    kids = self.num_children(p)
    parent = self.parent(p)

    #--------------------For Internal Nodes ------------------------#
    if kids >= 1: 
      if self.right(parent) == p: 
        node = self._validate(parent)
        return self.Position(self,node).element()
      
      else: 
        if self.right(parent) == None: 
          node = self._validate(parent)
          return self.Position(self,node).element()
        else: 

          temp = self.right(parent)
          while self.num_children(temp) >= 1:
            if self.left(temp) != None:
              temp = self.left(temp)
            else:
              temp = self.right(temp)

          node = self._validate(temp)
          return self.Position(self,node).element()

#----- For External Nodes ---------------------------#

    else: 
      if self.right(parent) == p:
        node = self._validate(parent)
        return self.Position(self,node).element()
      elif self.right(parent) == None: 
        node = self._validate(parent)
        return self.Position(self,node).element()
      else: 
        temp = self.right(parent)
        while self.left(temp) != None :
            temp = self.left(temp)
        node = self._validate(temp)
        return self.Position(self,node).element()



      
##########################################################################



  def delete_subtree(self, p):
    
    node = self._validate(p)
    parent = node._parent
  
    if parent._left == node:
        parent._left = None
    
    else:
        parent._right = None
        
    node._parent = node             
    self._size -= 1
    
    return node._element


################################################################

    
    


    

#--------------------------Test block-----------------------------# 



if __name__ == '__main__':

  #-----------------------------------My tree and positions -----------#
  T = ExtendedLinkedBinaryTree()
  T._add_root(23)
  three = T._add_right(T.root(),63)
  nine = T._add_right(three,80)

  eight = T._add_left(three,32)
  ten = T._add_right(eight,60)
  eleven = T._add_left(ten,50)
  

  two = T._add_left(T.root(),15)
  five = T._add_right(two, 20)
  four  =T._add_left(two, 8)
  six = T._add_left(five, 19)
  seven = T._add_right(five,22)
  twelve = T._add_left(eleven, 33)
  thirteen = T._add_right(eleven, 44)
  fourteen = T._add_left(thirteen, 55)
  fifteen = T._add_right(thirteen, 66)
  x = T._add_right(ten, 100)
  y = T._add_left(x,200)
  z = T._add_right(x,300)
  k = T._add_left(z,400)

#------------------------------------Calling methods and testing ---------#


#For preorder testing

  store = [] 
  gen = T.preorder() 
  for i in gen:
    store.append(i.element()) 
  print ()
  print("-------------Testing Preorder_next() ---------------------")
  print ()
  print("Preorder values using inbuilt method :")
  print ()
  print (store)
  print()
  print("Element in Position P = 60")
  print("Element in Return Position : ")
  print(T.preorder_next(ten))
  print()
  print("Element in Position P = 50 ")
  print("Element in Return Position : ")
  print(T.preorder_next(eleven))
  print()
  print("Element in Position P = 400 ")
  print("Element in Return Position : ")
  print(T.preorder_next(k))
  print()
  print("Element in Position P = 33")
  print("Element in Return Position : ")
  print(T.preorder_next(twelve))




  store2 = [] 
  gen2 = T.inorder() 
  for i in gen2:
    store2.append(i.element()) 
  print ()
  print("-------------Testing Inorder_next() ---------------------")
  print ()
  print("Inorder values using inbuilt method :")
  print ()
  print (store2)
  print()
  print("Element in Position P = 60")
  print("Element in Return Position : ")
  print(T.inorder_next(ten))
  print()
  print("Element in Position P = 50 ")
  print("Element in Return Position : ")
  print(T.inorder_next(eleven))
  print()
  print("Element in Position P = 400 ")
  print("Element in Return Position : ")
  print(T.inorder_next(k))
  print()
  print("Element in Position P = 33")
  print("Element in Return Position : ")
  print(T.inorder_next(twelve))


  store3 = [] 
  gen3 = T.postorder() 
  for i in gen3:
    store3.append(i.element()) 
  print ()
  print("-------------Testing Postorder_next() ---------------------")
  print ()
  print("Postorder values using inbuilt method :")
  print ()
  print (store3)
  print()
  print("Element in Position P = 60")
  print("Element in Return Position : ")
  print(T.postorder_next(ten))
  print()
  print("Element in Position P = 50 ")
  print("Element in Return Position : ")
  print(T.postorder_next(eleven))
  print()
  print("Element in Position P = 400 ")
  print("Element in Return Position : ")
  print(T.postorder_next(k))
  print()
  print("Element in Position P = 33")
  print("Element in Return Position : ")
  print(T.postorder_next(twelve))

  print ()
  print("-------------Testing delete_subtree() ---------------------")
  print("Inorder of the complete tree before deletion :")
  print ()
  print(store2) 
  print("After deletion of subtree rooted at position with Element: 32")
  T.delete_subtree(eight)
  store4 = [] 
  gen4 = T.inorder() 
  for i in gen4:
    store4.append(i.element())
  print ()
  print("Inorder of new tree :")
  print(store4)




  
 
    

 

  

   
 



  
  
