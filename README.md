# Forked thingy

the original code was written by billmill, but it's a "do what you want" license, so I'm doing that. renaming things, and I'm rewriting things to be hopefully more reusable.

I started with knuthdraw to see how strongly the code depends on the original drawing software, and the answer is "not much". So I cut out those parts, made the recursion more explicit. And wrote some code to use my custom drawing functions, (which I'm not sharing atm).

Looks like this, so the code does work, it just takes some tweaking. We'll see how much time I can invest into rewriting other bits as well.

![test_knuthdraw.svg](test_knuthdraw.svg)
![test_ws1.svg](test_ws1.svg)
![test_ws2.svg](test_ws2.svg)
![test_buchheim.svg](test_buchheim.svg)

# old readme
The following repository contains implementations of the functions described in the article "Drawing Presentable Trees" published in Python Magazine.

Check it out at http://billmill.org/pymag-trees/

All code and text contained herein is free for anyone to use as they see fit. It is licensed under the WTFPL, which can be found in the LICENSE file.
