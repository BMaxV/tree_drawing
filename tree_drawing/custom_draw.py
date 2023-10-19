from . import knuthdraw
from . import knuth
from . import draw_ws1
from . import draw_ws2
from . import figure7
from . import buchheim
from . import demo_trees
from . import gen
# my custom drawing modules
from geom import geom
from vector import vector

import textwrap

def type_convert_tups_lines(lines):
    new_lines = []
    for line in lines:
        new_lines.append(geom.Line.from_two_points(*line))
    return new_lines


def type_convert_tups_rectangles(rects):
    new_rects = []
    for rect in rects:
        pos = vector.Vector(*(rect[2], rect[3], 0))
        d_vec = vector.Vector(*(rect[0], rect[1], 0))
        new_rects.append(
            geom.rectangle(d_vec=d_vec, local_position=pos))

    return new_rects


def type_convert_tups_circles(circles):
    new_circles = []
    for circ in circles:
        text=None
        if len(circ)==4:
            x, y, r, text = circ
        else:
            x, y, r = circ
        pos = vector.Vector(x, y, 0)
        new_circles.append(
            geom.circle(radius=r, local_position=pos))
        if text!=None:
            new_circles.append(geom.Text(local_position=pos,text=text))
    return new_circles


def draw_main():
    test_output_knuth()
    test_draw_ws1()
    test_draw_ws2()
    test_draw_buchheim7()


def convert_tree_to_tree_drawing_datastructure(in_tree,recursion_dict):
    nodes = {}
    trees = []
    
    for x in in_tree:
        if x not in nodes:
            nodes[x]=gen.Tree(x)
        for value in in_tree[x]:
            if value not in nodes:
                nodes[value] = gen.Tree(value)
    
    for x in in_tree:
        root = nodes[x]
        for value in in_tree[x]:
            if value in recursion_dict:
                root.children.append(gen.Tree("recursive '"+value+"'")) #add an empty one.
            else:
                root.children.append(nodes[value])
        trees.append(root)
    
    return trees
    
def buchheimtree_draw(in_tree, recursion_dict):
    
    trees = convert_tree_to_tree_drawing_datastructure(in_tree,recursion_dict)
        
    for x in trees:
        test_draw_buchheim7(x)
        
def test_draw_buchheim7(t=None,output_fn_prefix="codetree_"):
    if t == None:
        t = demo_trees.trees[8]
    t = buchheim.buchheim(t)
    
    circles, lines, dotted = figure7.main(t)
    
    lines = type_convert_tups_lines(lines)
    dotted = type_convert_tups_lines(dotted)
    for x in dotted:
        x.style = "stroke:rgb(255,0,0)"
    circles = type_convert_tups_circles(circles)
    my_list = lines + circles + dotted
    
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    
    if t.tree.node == "root": # this is mcguyver'ed I know that this is the default.
        geom.main_svg(fl, output_fn_prefix+ "root.svg", view_box_d=view_box_d)
    else:
        geom.main_svg(fl, output_fn_prefix + t.tree.node + ".svg", view_box_d=view_box_d)

def dict_convert(t,my_dict=None):
    if my_dict==None:
        my_dict={}
    nodename=str(id(t))
    my_dict[nodename]=[]
    for child in t.children:
        my_dict[nodename] = dict_convert(child)
        
    return my_dict




if __name__ == "__main__":
    draw_main()
