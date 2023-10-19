from math import atan, cos, sin, pi

def drawt(root, depth, r, rw, rh):
    objects = []
    # child.tree.node is the text stored here
    my_oval = (root.x * rw, depth * rh, r, root.tree.node)
    objects.append(my_oval)
    for child in root.children:
        more_objects = drawt(child, depth + 1, r, rw, rh)
        objects += more_objects
    return objects


def drawconn(root, depth, r, rw, rh):
    objects = []
    for child in root.children:
        p1 = (root.x * rw, depth * rh + r, 0)
        p2 = (child.x * rw, (depth + 1) * rh - r, 0)
        my_line = (p1, p2)
        objects.append(my_line)
        more_lines = drawconn(child, depth + 1, r, rw, rh)
        objects += more_lines
    return objects


def dottedline(x1, y1, x2, y2):
    segment = 5
    if x2 == x1:
        theta = pi / 2
    elif x2 - x1 > 0:
        theta = atan(float(y2 - y1) / float(x2 - x1))
    else:
        theta = pi + atan(float(y2 - y1) / float(x2 - x1))

    dx = cos(theta) * segment
    dy = sin(theta) * segment
    xdir = x1 < x2
    ydir = y1 < y2

    while True:
        if xdir != (x1 < x2) or ydir != (y1 < y2):
            break
        line(x1, y1, x1 + dx, y1 + dy)
        x1, y1 = x1 + 2 * dx, y1 + 2 * dy


def drawthreads(root, depth, r, rw, rh):
    dotted = []
    for child in root.children:
        c = child.thread
        if child.thread:

            p1 = (child.x * rw, (depth + 1) * rh + r, 0)
            p2 = (c.x * rw, (depth + 2) * rh - r, 0)

            #p1=(child.x * rw + (r/2), (depth+1) * rh + (r/2),0)
            #p2=(c.x * rw + (r/2), (depth+2) * rh + (r/2),0)
            line = (p1, p2)

            dotted.append(line)

        drawthreads(child, depth + 1, r, rw, rh)
    return dotted


def main(t):
    
    r = 0.5
    rh = r * 2.5
    rw = r * 2.5
    
    lines = drawconn(t, 0, r, rw, rh)
    dotted_lines = drawthreads(t, 0, r, rw, rh)
    
    circles = drawt(t, 0, r, rw, rh)

    return circles, lines, dotted_lines
