import numpy as np

# Python3 program to convert a list
# of integers into a single integer
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = str(" ".join(s))
    return(res)

array = np.random.randint(100, size=(200, 200))
#print(array)
with open('200-200.txt', 'w') as f:
    for line in array :
        f.write(f"{  convert( line ) }\n")