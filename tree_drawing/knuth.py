class DrawTree(object):
    def __init__(self, tree, depth=0):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t, depth+1) for t in tree]

def layout(tree):
    dt = DrawTree(tree)
    setup_stack(dt)
    return dt

def setup(tree, i=0):
    
    # this is worst use of recursion I have seen in my life.
    # it should be a crime.
    # so, this draws a binary tree, which is why it only cares about
    # two children.
    
    
    # this is the fake return from the previous level
    if not tree:
        return i
    
    if len(tree.children) > 0: 
        l = tree.children[0]
    else:                      
        l = None # (1) this...
        
    if len(tree.children) > 1: 
        r = tree.children[1]
    else:                      
        r = None

    i = setup(l, i) # (1) does nothing, but it goes deeper. goes to the left by default.
    tree.x = i
    
    # this adds one, it's the only place where we got to the right
    # and we go to the left by default because of how DrawTree is defined.
    i += 1 
    
    # this either keeps i, or it adds one.
    i = setup(r, i)
    
    return i
    

def setup_stack(tree):
    # alternative with a stock instead of recursion
    
    i = 0
    stack = []
    current_node = tree
    
    while True:
        if current_node is not None:
            stack.append(current_node)
            if len(current_node.children) > 0:
                current_node = current_node.children[0]
            else:
                current_node = None
        elif stack:
            current_node = stack.pop()
            current_node.x = i
            i += 1
            
            if len(current_node.children) > 1:
                current_node = current_node.children[1]
            else:
                current_node = None
        else:
            break
