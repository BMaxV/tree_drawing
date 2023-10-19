from tree_drawing import custom_draw
from tree_drawing import knuthdraw
from tree_drawing import demo_trees
from tree_drawing import knuth
from tree_drawing import buchheim
from tree_drawing import figure7
from tree_drawing import draw_ws1
from tree_drawing import draw_ws2
from vector import vector
from geom import geom


def test_selfmade_tree():
    
    # this is your custom input
    
    in_tree={
            "node1":["node2","node3","node4"],
            "node2":["node21","node22"],
            "node3":["node2"],
            "node4":["node5"],
            }
            
    recursion_dict = {}
    
    # end of custom input, the stuff below you can copy.
    
    trees = custom_draw.convert_tree_to_tree_drawing_datastructure(in_tree,recursion_dict)
    print(trees)
    #assert len(trees)==1
    
    
    for tree in trees:
        lines, circles = draw_ws2.main(tree)
        lines = custom_draw.type_convert_tups_lines(lines)
        circles = custom_draw.type_convert_tups_circles(circles)
        my_list = lines + circles
       # for x in my_list:
        # x.scale_to(vector.Vector(0,0,0),0.01)

        view_box_d = geom.make_view_box_d(my_list)

        fl = []
        for x in my_list:
            fl.append(x.as_svg())
        geom.main_svg(fl, "selfmade_tree.svg", view_box_d=view_box_d)
        break

def test_output_knuth():
    
    # this merely does binary trees.
    # it's shit. don't use it.
    # don't even touch this.
    t = demo_trees.trees[5]
    t = knuth.layout(t)

    lines, rects = knuthdraw.main(t)
    # this converts to my custom types
    lines = custom_draw.type_convert_tups_lines(lines)
    rects = custom_draw.type_convert_tups_rectangles(rects)
    # this is my custom drawing code.
    my_list = lines + rects
    for x in my_list:
        x.scale_to(vector.Vector(0, 0, 0), 0.01)
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_knuthdraw.svg", view_box_d=view_box_d)

def test_draw_ws1():
    t = demo_trees.trees[4]
    lines, circles = draw_ws1.main(t)
    lines = custom_draw.type_convert_tups_lines(lines)
    circles = custom_draw.type_convert_tups_circles(circles)
    
    my_list = lines + circles
    
    # for x in my_list:
    # x.scale_to(vector.Vector(0,0,0),0.01)
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_ws1.svg", view_box_d=view_box_d)


def test_draw_ws2():
    t = demo_trees.trees[5]
    lines, circles = draw_ws2.main(t)
    lines = custom_draw.type_convert_tups_lines(lines)
    circles = custom_draw.type_convert_tups_circles(circles)
    my_list = lines + circles
   # for x in my_list:
    # x.scale_to(vector.Vector(0,0,0),0.01)

    view_box_d = geom.make_view_box_d(my_list)

    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_ws2.svg", view_box_d=view_box_d)
    
    
def test_draw_buchheim7(t=None):
    if t == None:
        t = demo_trees.trees[8]
    t = buchheim.buchheim(t)
    
    circles, lines, dotted = figure7.main(t)
    
    lines = custom_draw.type_convert_tups_lines(lines)
    dotted = custom_draw.type_convert_tups_lines(dotted)
    for x in dotted:
        x.style = "stroke:rgb(255,0,0)"
    circles = custom_draw.type_convert_tups_circles(circles)
    my_list = lines + circles + dotted
    
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    
    if t.tree.node == "root": # this is mcguyver'ed I know that this is the default.
        geom.main_svg(fl, "test_buchheim.svg", view_box_d=view_box_d)
    else:
        geom.main_svg(fl, "test_"+t.node+".svg", view_box_d=view_box_d)

def main():
    test_selfmade_tree()
    test_output_knuth()
    test_draw_ws1()
    test_draw_ws2()
    test_draw_buchheim7()

if __name__=="__main__":
    main()

