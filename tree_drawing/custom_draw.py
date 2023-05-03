import knuthdraw
import draw_ws1
import draw_ws2
import figure7

from demo_trees import trees

# my custom drawing modules
from geom import geom
from vector import vector


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
        x, y, r = circ
        pos = vector.Vector(x, y, 0)
        new_circles.append(
            geom.circle(radius=r, local_position=pos))
    return new_circles


def draw_main():
    test_output_knuth()
    test_draw_ws1()
    test_draw_ws2()
    test_draw_buchheim7()


def test_draw_buchheim7():
    circles, lines, dotted = figure7.main()
    lines = type_convert_tups_lines(lines)
    dotted = type_convert_tups_lines(dotted)
    for x in dotted:
        x.style = "stroke:rgb(255,0,0)"
    circles = type_convert_tups_circles(circles)
    my_list = lines + circles + dotted
   # for x in my_list:
    # x.scale_to(vector.Vector(0,0,0),0.01)
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_buchheim.svg", view_box_d=view_box_d)


def test_draw_ws2():
    lines, circles = draw_ws2.main()
    lines = type_convert_tups_lines(lines)
    circles = type_convert_tups_circles(circles)
    my_list = lines + circles
   # for x in my_list:
    # x.scale_to(vector.Vector(0,0,0),0.01)

    view_box_d = geom.make_view_box_d(my_list)

    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_ws2.svg", view_box_d=view_box_d)


def test_draw_ws1():
    lines, circles = draw_ws1.main()
    lines = type_convert_tups_lines(lines)
    circles = type_convert_tups_circles(circles)
    my_list = lines + circles
    # for x in my_list:
    # x.scale_to(vector.Vector(0,0,0),0.01)
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_ws1.svg", view_box_d=view_box_d)


def test_output_knuth():

    # ok, so the trees are just nodes, having children, etc..
    # so the logical next step is probably.

    t = layout(trees[5])
    # print(t, dir(t))

    lines, rects = knuthdraw.main(t)
    # this converts to my custom types
    lines = type_convert_tups_lines(lines)
    rects = type_convert_tups_rectangles(rects)
    # this is my custom drawing code.
    my_list = lines + rects
    for x in my_list:
        x.scale_to(vector.Vector(0, 0, 0), 0.01)
    view_box_d = geom.make_view_box_d(my_list)
    fl = []
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl, "test_knuthdraw.svg", view_box_d=view_box_d)


if __name__ == "__main__":
    draw_main()
