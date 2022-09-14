import knuthdraw

#my custom drawing modules
from geom import geom
from vector import vector

def type_convert_tups_lines(lines):
    new_lines=[]
    for line in lines:
        new_lines.append(geom.Line.from_two_points(*line))
    return new_lines

def type_convert_tups_rectangles(rects):
    new_rects=[]
    for rect in rects:
        new_rects.append(geom.rectangle(d_vec=(rect[0],rect[1],0),local_position=(rect[2],rect[3],0)))
        
    return new_rects
    
def draw_main():
    lines, rects = knuthdraw.main()
    # this converts to my custom types
    lines = type_convert_tups_lines(lines)
    rects = type_convert_tups_rectangles(rects)
    # this is my custom drawing code.
    my_list=lines+rects
    for x in my_list:
        print(x.local_position)
        x.scale_to(vector.Vector(0,0,0),0.01)
    view_box_d=geom.make_view_box_d(my_list)
    fl=[]
    for x in my_list:
        fl.append(x.as_svg())
    geom.main_svg(fl,"test_knuthdraw.svg",view_box_d=view_box_d)
    
if __name__=="__main__":
    draw_main()
