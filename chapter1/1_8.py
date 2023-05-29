# 冒泡排序
"""
对N个整数（数据由键盘输入）进行升序排列
冒泡排序思路：
首先，从表头开始往后扫描数组，在扫描过程中逐对比较相邻两个元素的大小。若相邻两个元素中，前面的元素大于后面的元素，则将它们互换，称之为消去了一个逆序。
在扫描过程中，不断地将两相邻元素中的大者往后移动，最后就将数组中的最大者换到了表的最后，这正是数组中最大元素应有的位置。
然后，在剩下的数组元素中（n-1个元素）重复上面的过程，将次小元素放到倒数第2个位置。不断重复上述过程，直到剩下的数组元素为0为止，此时的数组就变为了有序。
"""
def bubble(arr):
    for i in range(len(arr)): # 从头比较到尾，但是j是从0到数组长度减去i再减去1，因为当前第i步的时候，最后i个数字肯定是最大的，正确了。减一是因为j+1，如果之前不减一会超出数组索引。
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            print(arr)
    return arr

if __name__ == '__main__':
    arr = input('please input a list of numbers: ')
    arr = arr.split(",")
    arr = [int(a) for a in arr]
    print(arr)
    arr = bubble(arr)
    print('after sort, arr: {}'.format(arr))
