from collections import defaultdict
import re

def read_txt(file):
    str_return = ''
    with open(file,'r') as f:
        str_read = f.read()
        str_return += str_read
    return str_return

file = 'text.txt'
str_return = read_txt(file)
print(str_return)
# str_list = re.split(r'[-()\"\',.?\s]',str_return)
str_list = re.findall(r'[a-z]+',str_return.lower())
str_list = list(' '.join(str_list).lower().split())
# print(' '.join(str_list))
# print(''.join(str_list))
print(str_list)

def word_storage(str_list):
    word_dict = defaultdict(int)
    for word in str_list:
        word_dict[word] += 1
    return word_dict

word_dict = word_storage(str_list)
print(word_dict)

first = 'abcdefghijklmnopqrstuvwxyz'

# array = np.array(word_dict.items())
# print(array)

arr = [(k,v) for k,v in word_dict.items()]
print(arr)
def word_sort(arr):
    for item in arr:
        print(item)
# word_sort(arr)

def quick_sort(arr,left,right):
    if left<right:
        q = Partition(arr,left,right)
        quick_sort(arr,left,q-1)
        quick_sort(arr,q+1,right)

def Partition(arr,left,right):
    i = left
    j = right+1
    x = arr[left]
    i += 1
    j -= 1
    while True:
        while arr[i][0]<x[0] and i<right:
            i += 1
        while arr[j][0]>x[0]:
            j -= 1
        if i>=j:
            break;
        arr[i],arr[j] = arr[j],arr[i]
    arr[left] = arr[j]
    arr[j] = x
    return j

quick_sort(arr,0,len(arr)-1)
print(arr)

print('*************************abc************************')
for item in arr:
    print(item)


def quick_sort_fre(arr,left,right):
    if left<right:
        q = Partition_fre(arr,left,right)
        quick_sort_fre(arr,left,q-1)
        quick_sort_fre(arr,q+1,right)

def Partition_fre(arr,left,right):
    i = left
    j = right+1
    x = arr[left]
    i += 1
    j -= 1
    while True:
        while arr[i][1]<=x[1] and i<right:
            i += 1
        while arr[j][1]>x[1]:
            j -= 1
        if i>=j:
            break
        arr[i],arr[j] = arr[j],arr[i]
    arr[left] = arr[j]
    arr[j] = x
    return j

quick_sort_fre(arr,0,len(arr)-1)
arr_fre = arr[::-1]
print('*******************fre******************8')
for item in arr_fre:
    print(item)