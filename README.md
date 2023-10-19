# Forked thingy

the original code was written by billmill, but it's a "do what you want" license, so I'm doing that. renaming things, and I'm rewriting things to be hopefully more reusable.

I started with knuthdraw to see how strongly the code depends on the original drawing software, and the answer is "not much". So I cut out those parts, made the recursion more explicit. And wrote some code to use my custom drawing functions, (which I'm not sharing atm).

Looks like this, so the code does work, it just takes some tweaking. We'll see how much time I can invest into rewriting other bits as well.

![test_knuthdraw.svg](tests/test_knuthdraw.svg)
![test_ws1.svg](tests/test_ws1.svg)
![test_ws2.svg](tests/test_ws2.svg)
![test_buchheim.svg](tests/test_buchheim.svg)

# how to

This is the "self made" tree in tests/regular_tests.py

```
def test_selfmade_tree():
    
    # this is your custom input
    
    in_tree={
            "node1":["node2","node3","node4"],
            "node2":["node21","node22"],
            "node3":["node2"],
            "node4":["node5"],
            }
    
    # I put stuff in for preventing drawing recursive trees, but that doesn't really work right now.
    recursion_dict = {}
        
    # this creates trees for all root nodes in "in_tree"
    trees = custom_draw.convert_tree_to_tree_drawing_datastructure(in_tree,recursion_dict)
    
    for tree in trees:
        lines, circles = draw_ws2.main(tree)
        
        # so, those do use my custom drawing code, but
        # don't worry about it, lines are defined as lists of
        # two points [(x1,y1),(x2,y2)]
        # and circles as [radius, x, y, text]
        
        lines = custom_draw.type_convert_tups_lines(lines)
        circles = custom_draw.type_convert_tups_circles(circles)
        my_list = lines + circles
        view_box_d = geom.make_view_box_d(my_list)

        fl = []
        for x in my_list:
            fl.append(x.as_svg())
        geom.main_svg(fl, "selfmade_tree.svg", view_box_d=view_box_d)
        break
```

Careful with recursion, I meant to write something to prevent it, but it looks like that's not working right now.

![selfmade_tree.svg](tests/selfmade_tree.svg)

# original license.

...WTFPL

which is a bit inconvenient so I'm relicensing the stuff I did and changed and the new code as MIT.

# old readme
The following repository contains implementations of the functions described in the article "Drawing Presentable Trees" published in Python Magazine.

Check it out at http://billmill.org/pymag-trees/

All code and text contained herein is free for anyone to use as they see fit. It is licensed under the WTFPL, which can be found in the LICENSE file.

