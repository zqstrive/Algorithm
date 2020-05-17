import re
import numpy as np

lib_text = 'lib.txt'
check_text = 'text.txt'


def read_txt(file):
    str_return = ''
    with open(file,'r') as f:
        str_read = f.read()
        str_return += str_read
    return str_return

def data_process(data_str):
    data_return = []
    data_list = re.split(r'[.?!]',data_str.lower())
    for item in data_list:
        item = item.strip()
        data_return.append(item)
    return data_return


lib_str = read_txt(lib_text)
lib_list = data_process(lib_str)
print(lib_list)

check_str = read_txt(check_text)
check_list = data_process(check_str)
print(check_list)
print('**********')

# for item in check_list:
#     m = len(item.split())
#     item_list = item.split()
#     # print(m)
#     # print(item_list)
#     for iter in lib_list:
#         n = len(iter.split())
#         iter_list = iter.split()
#         word_similarity = np.zeros((m,n))
#         score = np.zeros((m,n))
#         for i in range(m):
#             for j in range(n):
#                 if item_list[i] == iter_list[j]:
#                     word_similarity[i][j] = 1
        # if not np.all(word_similarity==0):
        #     print(word_similarity)

        # for k in range(1,m):
        #     score[k][0] = max(score[k-1][0]-0.5,word_similarity[k][0]-0.5*(k-1))
        # for k in range(1,n):
        #     score[0][k] = max(score[0][k-1]-0.5,word_similarity[0][k]-0.5*(k-1))
        #
        # for k in range(1,m):
        #     for j in range(1,n):
        #         score[k][j] = max(score[k-1][j]-0.5,score[k][j-1]-0.5,score[k-1][j-1]+word_similarity[k][j])
        # print(score)

def lcs_length(m,n,x,y):
    c = np.zeros((m+1,n+1))
    b = np.zeros((m+1,n+1),dtype=np.str)

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '←'
    return c,b

def lcs(i,j,x, b):
    if i == -1 or j == -1:
        return
    if b[i][j] == 1:
        lcs(i-1,j-1,x,b)
        print(x[i],end=' ')
    elif b[i][j] == 2:
        lcs(i-1,j,x,b)
    else:
        lcs(i,j-1,x,b)


def get_text(c,b,check_text,lib_text):
    i,j = c.shape
    i -= 1
    j -= 1
    while c[i][j] != 0:
        if b[i][j] == '↑':  # check有，lib无，故在lib处插入一个*
            lib_text.insert(j,'*')
            i -= 1
        if b[i][j] == '←':
            check_text.insert(i,'*')    #同理
            j -= 1
        if b[i][j] == '↖':
            i -= 1
            j -= 1
    return check_text,lib_text

n_count = 0
for (a,item) in enumerate(check_list):
    for (d,iter) in enumerate(lib_list):
        m = len(item.split())
        n = len(iter.split())
        item_list = item.split()
        iter_list = iter.split()
        c,b = lcs_length(m,n,item_list,iter_list)
        # print(c)
        # if c.size != 0:
        #     max_num = np.max(c)
        #     if max_num/m >0.7:
        #         print(max_num/m)
        #         lcs_dict[a] = d
        #         # lcs(m-1,n-1,item_list,b)
        #         print('**')
        # if '↖' in b:
        if c.size != 0 and m != 0:
            max_num = c[-1][-1]
            if max_num/m > 0.5:
                # print(c)
                item_text,iter_text = get_text(c,b,item_list,iter_list)
                print(item_text)
                print(iter_text)
                n_count += 1

print('相似度 {:.2f}'.format(n_count/len(check_list)))
