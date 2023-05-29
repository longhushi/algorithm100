#折半查找
"""
N个有序整数数列已放在一维数组中，利用二分查找法查找整数m在数组中的位置。若找到，则输出其下标值，若未找到，则输出“not be found!”
"""
# 思路就是把当前数据和有序数列中间的数比较，如果大就在后一半找，如果小就在前一半找，如果等于，就是找到了。
# 我自己的是递归做法
def find(num, arr):
    i = int(len(arr)/2)
    if(len(arr)<2 and num!=arr[0]):
        print("not be found!")
        return -1
    else:
        if(num > arr[i]):
            arr2 = arr[i:]
            find(num, arr2)
        elif(num < arr[i]):
            arr2 = arr[:i]
            find(num, arr2)
        else:
            print("find , the index is:{}".format(i))
            return i

# 这是书上和传统的做法        
def find2(num, arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if num < arr[mid]:
            high = mid-1
        else:
            if num > arr[mid]:
                low = mid+1
            else:
                print("find , the index is:{}".format(mid))
                return mid
    print("not be found!")
    
if __name__ == "__main__":
    arr = input('Please input an ordered list of numbers:')
    arr = arr.split(",")
    arr = [int(a) for a in arr]
    num = input('Please enter the number you want to find:')
    num = int(num)
    find2(num,arr)