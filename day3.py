#1D
import numpy as np

a = [1, 2, 3, 4]

arr = np.array(a)

print("List in python :", a)

print("Numpy Array in python :", arr)


#multi
import numpy as np
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
sample_array = np.array([list_1,
                        list_2,
                        list_3])
print("Numpy multi dimensional array in python\n",
     sample_array)

#PARAMETERS OF A NUMPY ARRAY - SHAPE
import numpy as np
sample_array = np.array([[0, 4, 2],
                      [3, 4, 5],
                      [23, 4, 5],
                      [2, 34, 5],
                      [5, 6, 7]])
 
print("shape of the array :", sample_array.shape)

#data type

import numpy as np

sample_array_1 = np.array([[0, 4, 2]])

sample_array_2 = np.array([0.2, 0.4, 2.4])

print("Data type of the array 1 :", sample_array_1.dtype)

print("Data type of array 2 :", sample_array_2.dtype)


#different Ways of Creating Numpy Array

import numpy as np
arr = np.array([3,4,5,5])

print("Array :",arr)



import numpy as np

var = "Geekforgeeks"
arr = np.fromiter(var, dtype = 'U2')

print("fromiter() array :",
     arr)



import numpy as np

np.arange(1, 20 , 2, 
          dtype = np.float32)



import numpy as np

np.linspace(3.5, 10, 3, 
            dtype = np.int32)



import numpy as np

np.empty([4, 3],
         dtype = np.int32,
         order = 'f')



import numpy as np

np.ones([4, 3],
        dtype = np.int32,
        order = 'f')




import numpy as np
np.zeros([4, 3], 
         dtype = np.int32,
         order = 'f')




