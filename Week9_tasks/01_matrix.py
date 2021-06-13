from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = deepcopy(lst)

    def __str__(self):
        table = ''
        lenlst = len(self.lst)
        count = 1
        for lst in self.lst:
            table += '\t'.join(map(str, lst))
            if count < lenlst:
                table += '\n'
            count += 1
        return table

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            result = []
            for i in range(len(self.lst)):
                list1 = self.lst[i]
                list2 = other.lst[i]
                semiresult = []
                for num in range(len(list1)):
                    semiresult.append(list1[num] + list2[num])
                result.append(semiresult)
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = []
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.lst)):
                list1 = self.lst[i]
                semiresult = []
                for num in range(len(list1)):
                    semiresult.append(list1[num] * other)
                result.append(semiresult)
        elif isinstance(other, Matrix):
            if len(self.lst[0]) == len(other.lst):
                pass
            else:
                raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def size(self):
        return (len(self.lst), len(self.lst[0]))

    def transpose(self):
        new_list = []
        for i in range(len(self.lst[0])):
            temp = []
            for j in range(len(self.lst)):
                temp.append(self.lst[j][i])
            new_list.append(temp)
        self.lst = new_list
        return self

    @staticmethod
    def transposed(self):
        a = Matrix(self.lst)
        return a.transpose()


exec(stdin.read())
