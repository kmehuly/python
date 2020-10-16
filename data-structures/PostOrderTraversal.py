class newNode:  
  
    # Constructor to create a newNode  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None
  

def postorder(head): 
      
    temp = head  
    visited = set() 
    while (temp and temp not in visited):  
          
        # Visited left subtree  
        if (temp.left and temp.left not in visited): 
            temp = temp.left  
              
        # Visited right subtree  
        elif (temp.right and temp.right not in visited): 
            temp = temp.right  
          
        # Print node  
        else: 
            print(temp.data, end = " ")  
            visited.add(temp)  
            temp = head  
  
''' Driver program to test above functions'''
if __name__ == '__main__': 
      
    root = newNode(8)  
    root.left = newNode(3)  
    root.right = newNode(10)  
    root.left.left = newNode(1)  
    root.left.right = newNode(6)  
    root.left.right.left = newNode(4)  
    root.left.right.right = newNode(7)  
    root.right.right = newNode(14)  
    root.right.right.left = newNode(13)  
    postorder(root)
