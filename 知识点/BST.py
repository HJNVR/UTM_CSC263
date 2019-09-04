class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
#def delete(self, data):
    def print_tree(self):

        if self.left:
            self.left.print_tree()
        print (self.data)
        if self.right:
            self.right.print_tree()

#BST search
    def TreeSearch(self,k):
        # we want to know whether k is in the tree, and return the node where
        # k is the parent
        if not self.data or self.data == k:
            self.print_tree()
            return
        if k < self.data:
            return self.left.TreeSearch(k)
        else:
            return self.right.TreeSearch(k)

#find the minimum of the BST
# 
    def TreeMinimum(self, Node):
        """ 最小的数字永远是在左边的subtree里
        """
        current = Node

        while(current.left != None):
            current = current.left
        current.print_tree()
        return
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def inorder_successor(self, Node):
        """
        找到比给定的Node的data大， 但是最小的大的Node
        """
        if Node.right:
            return self.TreeMinimum(Node.right)  # 如果trre有右支线，找到右支线的最小值
        p = Node.parent
        while(p is not None):
            if Node != p.right:
                break  # determine wheter Node is the rigth child of parent
            Node = p
            p = p.parent # going up 往上找
        return p.data

    def TreeMaximum(self, Node):
        current = Node
        while(current.right):
            current = current.right
        return current.data
    
    def predecessor(self, Node):
        """
        找到比给定的Node的data小， 但是最大的小的Node
        和successor对称
        """
        if(Node.left):
            return self.TreeMaximum(Node.left)
        p = Node.parent
        while(p is not None):
            if Node != p.left:
                break
            Node = p
            p = p.parent

        return p.data

    def Delete(self, Node):
        """
        Three cases:
        [1] Node has node
        [2] Node has one child
        [3] Node has two children
        """
        if(Node is None):
            return Node
        if(Node.data < self.data):
            self.left.Delete(Node)
        elif(Node.data > self.data):
            self.right.Delete(Node)
        else:
            self.print_tree()
            if(self.left is None and self.right is None):
                self = None
                
           # return (self.data)
        
    
    def minValueNode(self,node): 
        current = node 
  
    # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
  
        return current  
  
# Given a binary search tree and a key, this function 
# delete the key and returns the new root 
    def deleteNode(self, data): 
  
    # Base Case 
        if self is None: 
            return self  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
        if data < self.data: 
            self.left = self.left.deleteNode(data) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
        elif(data > self.data): 
            self.right = self.right.deleteNode(data) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
        else: 
          
        # Node with only one child or no child 
            if self.left is None : 
                temp = self.right  
                self = None 
                return temp  
              
            elif self.right is None : 
                temp = self.left  
                self = None
                return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
            temp = self.minValueNode(self.right) 
  
        # Copy the inorder successor's content to this node 
            self.key = temp.key 
  
        # Delete the inorder successor 
            self.right = self.right.deleteNode(temp.key) 
  
  
        return self

    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1
        
    def maxDepth(self): 
        if self is None: 
            return 0 ;
        else: 
      
        # Compute the depth of each subtree 
            lDepth = self.left.maxDepth() 
            rDepth = self.rightmaxDepth() 
  
        # Use the larger one 
            if (lDepth > rDepth): 
                return lDepth+1
            else: 
                return rDepth+1















        
