# WRITE YOUR SOLUTION HERE:
	class Node:
	    """ Class is modeling single node in binary tree """
	    def __init__(self, value, left_child: 'Node' = None, right_child: 'Node' = None):
	        self.value = value
	        self.left_child = left_child
	        self.right_child = right_child
	 
	 
	def greatest_node(root: Node):
	    left = root.value
	    right = root.value
    
	    if root.left_child != None:        
	        left = greatest_node(root.left_child)        
	    
	    if root.right_child != None:         
	        right = greatest_node(root.right_child)
	    
	    return left if left > right else right   
	       
	if __name__ == "__main__":
	    tree = Node(7)
	 
	    tree.left_child = Node(3)
	    tree.left_child.left_child = Node(2)
	    tree.left_child.right_child = Node(205)
	    tree.left_child.right_child.right_child = Node(14)
	 
	    tree.right_child = Node(11)
	    tree.right_child.right_child = Node(4)
	    tree.right_child.right_child.left_child = Node(72)    
	    tree.right_child.right_child.right_child = Node(12)
	    tree.right_child.right_child.right_child.left_child = Node(25)
	 
	    print(greatest_node(tree))
	 



