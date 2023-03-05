# python3

import sys
import threading
import numpy
from collections import defaultdict

def compute_height(n, parents, augstums):
    # Write this function
    max_height = 0
    # Your code here
    if augstums[n] != 0:
        return augstums[n]
    if parents[n] == -1:
        augstums_n = 1
    else:
        augstums_n = 1 + compute_height(parents[n], parents, augstums)
        augstums[n] = augstums_n
    return augstums_n


def main():
    # implement input form keyboard and from files
    input=input().strip()
    if input=='i':
        number = int(input().strip())
        parentsl= map(int, number)
        plist=list(parentsl)
    elif input == 'F':
        filename = input().strip()
        with open(filename,'r') as f:
            num_nodes = int(f.readline().strip())
            list=map(int, f,readline().split())
            plist=list(list)
    else:
    raise ValueError("nav korekts input")
    
    augstums =defaultdict(int)
    tree_height = 0
    for i in range(number):
        augstums_n = compute_tree_height(i, plist, augstums)
        if augstums_n > tree_height:
            tree_height = augstums_n
        if tree_height == number:
            break
            
    print(tree_height)

if __name__ == '__main__':
    main()
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
