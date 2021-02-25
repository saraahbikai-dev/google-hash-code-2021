import numpy as np
import sys

# Part 1: Parse Input
Overlap_Matrix=None
input_filename= "a_example"
f = open(input_filename, "r")
inp=f.read().splitlines()

logistics = inp[0].split(" ")
n_pizzas = logistics[0]
n_one = logistics[1]

raw=[]
qty=[]
for i in range(1,len(inp)):
    raw.append((inp[i].strip()[1:]).strip())
    qty.append((inp[i].strip()[0]).strip())
print(raw)
n_piztypes = len(raw)

# Part 2: Create Over Lap Matrix

def get_num_overlaps(l1,l2):
    '''
    Returns number of overlapping items from between two input lists
    '''
    return sum([1 for n in l1.split(" ") if n in l2.split(" ")])

def create_overlap_matrix(raw):
    '''
    Returns 2D Overlap Matrix, dimension= number of pizza types
    Also returns "Starter" - Pizza Type that has least overlap with other pizza types.
    '''
    n_piztypes = len(raw)

    # init empty numpy array
    ov_mat=np.zeros(n_piztypes**2).reshape(n_piztypes,n_piztypes)

    for i in range(n_piztypes):
        for j in range(n_piztypes):
            ov_mat[i][j]=get_num_overlaps(raw[i], raw[j])
    
    
    starter = np.argsort(np.sum(ov_mat, axis=1))
    return (ov_mat, starter )
Overlap_Matrix, Starter=create_overlap_matrix(raw)


# Part 3: Allocation
rankie = np.zeroes(n_piztypes*2).reshape(n_piztypes,2)


# Part 4: Create Output (Submission File)