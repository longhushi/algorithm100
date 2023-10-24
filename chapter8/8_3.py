# 矩阵转置
"""
编写一个程序，将一个3行3列的矩阵进行转置。
"""
# 矩阵转置就是把行列互换

def transpose(arr):
    for i in range(3):
        for j in range(3):
            if i<j:
                temp = arr[i][j]
                arr[i][j] = arr[j][i]
                arr[j][i] = temp
    return arr


if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(arr)
    arr = transpose(arr)
    print(arr)