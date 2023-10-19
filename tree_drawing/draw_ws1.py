from . import ws1

# draw_ws1 and draw_ws2 are the same, the tree is different.
# and they use ws1 and ws2 respectively.
# that's all.


def drawt(root, depth, r, rw, rh):
    objects = []
    my_oval = (root.x * rw, depth * rh, r)
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


def main(t):
    t = ws1.layout(t)

    r = 0.5
    rh = r * 2.5
    rw = r * 2.5

    lines = drawconn(t, 0, r, rw, rh)
    circles = drawt(t, 0, r, rw, rh)

    return lines, circles
