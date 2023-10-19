import time
from tqdm import tqdm

def gen():
    for x in [1,2,3]:
        time.sleep(0.5)
        yield x

my_gen=gen()
for x in tqdm(my_gen):
    print(x)

for x2 in tqdm(range(10000000)):
    pass
