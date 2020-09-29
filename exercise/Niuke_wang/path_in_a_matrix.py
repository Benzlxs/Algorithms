"""
题目描述：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 a b c e s f c s a d e e
矩阵中包含一条字符串"abccee"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。

"""



## recrusive
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix  or  not path :
            return False
        visited = [0] * len(matrix)
        result = ''
        length = 0
        for row in range(rows):
            for col in range(cols):
                if (self.hasPathCore(matrix, path, rows, cols, row, col, visited, result, length)):
                    return True
        del visited
        return False

	# recursive function
    def hasPathCore(self, matrix, path, rows, cols, row, col, visited, result, length):
        if result == path:
            return True
        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and (not visited[row*cols + col])\
            and path[length] == matrix[row*cols + col]):
            length += 1
            visited[row*cols + col] = 1
            result += matrix[row*cols + col]
            hasPath = self.hasPathCore(matrix, path, rows, cols, row-1, col, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row+1, col, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row, col+1, visited, result, length) or \
                      self.hasPathCore(matrix, path, rows, cols, row, col-1, visited, result, length)
            if (not hasPath):
                length -= 1
                visited[row*cols + col] = 0
                result = result[:-1]
        return hasPath        # write code here
