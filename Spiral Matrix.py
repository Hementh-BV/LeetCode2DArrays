def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = (list(zip(*matrix)))[::-1]
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


# Visualization
# Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:
#
#     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
#     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
#     |7 8 9|      |4 7|
# Now look at the first rows we extracted:
#
#     |1 2 3|      |6 9|      |8 7|      |4|      |5|
