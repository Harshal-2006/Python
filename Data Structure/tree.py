class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def isoperator(char):
    return char in "+-*/"

def buildprefix(prefixlist):
    if not prefixlist:
        return None
    token = prefixlist.pop(0)
    node = Node(token)

    if isoperator(token):
        node.left=buildprefix(prefixlist)
        node.right=buildprefix(prefixlist)
    return node

def post(root):
    if root is None:
        return []
    stack1=[]
    stack2=[]
    result=[]

    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().value)

    return result

def deletetree(node):
    if node is None:
        return
    deletetree(node.left)
    deletetree(node.right)
    node = None

if __name__=="__main__":
    prefixip=input("Enter - ")
    prefixtoken=list(prefixip)

    print("prefix - ",prefixip)
    #build tree
    root = buildprefix(prefixtoken)

    print("post")
    postorder = post(root)
    print(" ".join(postorder))
    print("\n")

    print("to delete tree ")
    deletetree(root)
    root = None
    print("deleted tree")
    














    
    





        
