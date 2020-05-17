def get():
    file = open("text.txt")
    file_ = open("lib.txt")
    file = file.read()
    file_ = file_.read()
    return [list(file),list(file_)]
def split(lib,text):
    lib_ = []
    text_ = []
    str = ""
    finish = ['.','?','!']
    for i in lib:
        if i in finish and str != "":
            str = str.lower()
            lib_.append(str)
            str = ""
        else:
            str += i
    str = ""
    for i in text:
        if i in finish and str!="":
            str = str.lower()
            text_.append(str)
            str = ""
        else:
            str += i
    return lib_,text_
def Words_num(sen):
    result = []
    str =""
    sen_ = list(sen)
    for i in sen_:
        if i.isalpha():
            str += i
        elif str != "":
            result.append(str)
            str = ""
    return result
def  wordSim(temp,lib):
    S = [[0 for col in range(len(lib))] for row in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(lib)):
            if temp[i] == lib[j]:
                S[i][j] = 1
    return S
def get_score(w,temp,lib):
    m = len(temp)
    n = len(lib)
    score = [[0 for col in range(n)] for row in range(m)]
    b = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        score[i][0] = 0
    for i in range(n):
        score[0][i] = 0
    for i in range(m):
        for j in range(n):
            if temp[i]==lib[j]:
                score[i][j] = score[i-1][j-1]+1
                b[i][j] = 1
            elif score[i-1][j] >= score[i][j-1]:
                score[i][j] = score[i-1][j]
                b[i][j] = 2
            else:
                score[i][j] = score[i][j-1]
                b[i][j] = 3
    return score,b
def duplicate_checking(lib,text):
    result = {}
    p = 0
    for i in text:
        TempSentence = Words_num(i)
        p += 1
        m = 0
        for j in lib:
            libSentence = Words_num(j)
            wordSimilarity = wordSim(TempSentence,libSentence)
            score,b = get_score(wordSimilarity,TempSentence,libSentence)
            if(score[-1][-1]>m):
                m = score[-1][-1]
                u = j
                q = score
                w = b
        re = m/len(TempSentence)*100
        result[p] = [len(TempSentence),m,re,i,u,q,w]
    return result
def com_sim(re):
    num = list(re.keys())
    ana = list(re.values())
    sum,sum_ = 0,0
    t=""
    l=""
    for i in num:
        sum += ana[i-1][1]
        sum_ += ana[i-1][0]
        mm = Words_num(ana[i-1][3])
        nn = Words_num(ana[i-1][4])
        mmm = mm.copy()
        nnn = nn.copy()
        m = len(mm)-1
        n = len(nn)-1
        while m>0 and n>0:
                if ana[i-1][6][m][n]==1:
                    m -=1
                    n -=1
                    if(n==0 or m==0):
                        break
                elif ana[i-1][6][m][n]==3:
                    mmm.insert(m+1,"*")
                    n -=1
                else:
                    nnn.insert(n+1,"*")
                    m-=1
        print(str(i)+"Word in Text",end="")
        print(mmm)
        print(str(i)+"Word in lib",end="")
        print(nnn)

    return sum/sum_*100



if __name__ == "__main__":
    text,lib = get()
    lib,text = split(lib,text)
    re = duplicate_checking(lib,text)
    result = com_sim(re)
    print("text.txt与lib.txt的相似度计算为"+str(result)+"%")
