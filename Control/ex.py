import numpy as np

path = np.loadtxt('path1.txt',delimiter='\t',unpack=False)
path_array = np.array(path)
print(path_array)