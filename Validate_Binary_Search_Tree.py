""""
This program validates a binary search tree with these requirements
1. Left node must be less than root
2. Right node must be greater than root
I solved it by using a recursive function that goes through the tree in preorder root, left subtree, right subtree.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def toString(self):
        print('Value {0}'.format(self.val))

class Solution:
    def isValidBST(self, root):
        # root.toString()
        valid = True

        if root == None:
            return True
        if root.left != None and root.left.val > root.val:
            return False
        else:
            valid = self.isValidBST(root.left)
            if not valid:
                return False
        if root.right != None and root.right.val < root.val:
            return False
        else:
            valid = self.isValidBST(root.right)
            if not valid:
                return False
            
        return valid

def main():
    # This tree corresponds to [5, 4, 3, None, 6, None, 8] which evaluates to True
    root = TreeNode(5)
    left_node = TreeNode(4)
    right_node = TreeNode(6)
    left_node_child1 = TreeNode(3)
    right_node_child1 = TreeNode(8)
    
    root.left = left_node
    root.right = right_node
    
    right_node.right = right_node_child1
    right_node.left = None
    left_node.left = left_node_child1
    left_node.right = None
    left_node_child1.left = left_node_child1.right = None

    sol = Solution()
    print(sol.isValidBST(root))

if __name__=="__main__":
    main()	
