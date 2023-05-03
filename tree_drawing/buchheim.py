
# the relevant text is at the bottom of page 7 of
# "Improving Walker's Algorithm to Run in Linear Time" by Buchheim et al, (2002)
# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.16.8757&rep=rep1&type=pdf

# the may actually be significantly more readable than the code.

# the problem with this is is that the tree doesn't do anything.
# I can't use it for anything, because the tree object holds no data.

class DrawTree:
    def __init__(self, tree, parent=None, depth=0, index=1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = []
        for i, c in enumerate(tree.children):
            self.children.append(DrawTree(c, self, depth+1, i+1))
        
        self.parent = parent
        self.thread = None
        self.mod = 0
        self.ancestor = self
        self.change = self.shift = 0
        self._lmost_sibling = None
        #this is the number of the node in its group of siblings 1..n
        self.index = index

    def left(self):
        # dislike that it's hard to know what the truthiness is here.
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

    def lbrother(self):
        n = None
        if self.parent:
            for node in self.parent.children:
                if node == self:
                    return n
                else:            
                    n = node
        return n

    def get_lmost_sibling(self):
        if not self._lmost_sibling and self.parent and self != self.parent.children[0]:
            self._lmost_sibling = self.parent.children[0]
        return self._lmost_sibling
    lmost_sibling = property(get_lmost_sibling)

    def __str__(self): 
        return f"{self.tree}: x={self.x} mod={self.mod}"
        
    def __repr__(self): 
        return self.__str__()

def buchheim(tree):
    dt = firstwalk(DrawTree(tree))
    r = second_walk(dt)
    if r < 0:
        third_walk(dt, -r)
    return dt

def third_walk(tree, n):
    tree.x += n
    for c in tree.children:
        third_walk(c, n)

def firstwalk(node, distance = 1):
    if len(node.children) == 0:
        if node.lmost_sibling:
            node.x = node.lbrother().x + distance
        else:
            node.x = 0
    else:
        default_ancestor = node.children[0]
        for child in node.children:
            firstwalk(child)
            default_ancestor = apportion(child, default_ancestor, distance)
        execute_shifts(node)

        midpoint = (node.children[0].x + node.children[-1].x) / 2

        ell = node.children[0]
        arr = node.children[-1]
        brother = node.lbrother()
        if brother:
            node.x = brother.x + distance
            node.mod = node.x - midpoint
        else:
            node.x = midpoint
    return node

def apportion(node, default_ancestor, distance):
    w = node.lbrother()
    
    if w is not None:
        #in buchheim notation:
        #i == inner; o == outer; r == right; l == left; r = +; l = -
        vir = vor = node
        vil = w
        vol = node.lmost_sibling
        sir = sor = node.mod # 0 by default
        sil = vil.mod # 0 by default
        sol = vol.mod # 0 by default
        while vil.right() and vir.left():
            vil = vil.right()
            vir = vir.left()
            vol = vol.left()
            vor = vor.right()
            vor.ancestor = node
            shift = (vil.x + sil) - (vir.x + sir) + distance
            if shift > 0:
                move_subtree(ancestor(vil, node, default_ancestor), node, shift)
                sir = sir + shift
                sor = sor + shift
            sil += vil.mod
            sir += vir.mod
            sol += vol.mod
            sor += vor.mod
        
        if vil.right() and not vor.right():
            vor.thread = vil.right()
            vor.mod += sil - sor
        
        else:
            if vir.left() and not vol.left():
                vol.thread = vir.left()
                vol.mod += sir - sol
            default_ancestor = node
    return default_ancestor

def move_subtree(wl, wr, shift):
    subtrees = wr.index - wl.index
    #print wl, wr, wr.index, wl.index, shift, subtrees, shift/subtrees
    wr.change -= shift / subtrees
    wr.shift += shift
    wl.change += shift / subtrees
    wr.x += shift
    wr.mod += shift

def execute_shifts(node):
    shift = change = 0
    for w in node.children[::-1]:
        w.x += shift
        w.mod += shift
        change += w.change
        shift += w.shift + change

def ancestor(vil, node, default_ancestor):
    
    if vil.ancestor in node.parent.children:
        return vil.ancestor
    else:
        return default_ancestor

def second_walk(node, m=0, depth=0, i_min=None):
    node.x += m
    node.y = depth
    
    # reset the minimum to node.x
    if i_min is None or node.x < i_min:
        i_min = node.x
    
    # recursion
    for child in node.children:
        i_min = second_walk(child, m + node.mod, depth+1, i_min)

    # this is only needed because they're shifting too much.
    # need to correct in run 3? or was that the guy who copied their work?
    return i_min

