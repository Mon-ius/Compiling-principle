import re
# Input:
# 6
# S->#E# 
# P->i
# F->P
# T->F
# E->T
# E->E+T

def _find(x,fa):
    if x not in fa.keys():
        return x
    if x == fa[x]:
        return x
    else:
        
        return _find(fa[x],fa)

def _check(x,y,fa):
    if _find(x, fa) == _find(y,fa):
        return True
    return False

def _union(x,y,fa):
    if x not in fa.keys():
        print('ix',x)
        fa[x]=x
    if y not in fa.keys():
        fa[y]=y
        print('ix',y)
    x = _find(x,fa)
    y = _find(y,fa)
    fa[x]= y

def check(x,y,fa):

    if not len(x) == len(y):
        return False
    for i in range(len(x)):
        if x[i].isupper():
            if not _check(x[i],y[i],fa):
                return False
        else:
            if not x[i] == y[i]:
                return False
    return True



class WORD:
    def __init__(self,left):
        # print(left)
        self.left = left
        self.right = []
    def insert(self,right):
        self.right.append(right)
    def print(self):
        message=[]
        st = "{} -> {}".format(self.left,self.right[0])
        print(st,end=' ')
        for m in self.right[1:]:
            print("|{}".format(m),end=' ')
        else:
            print("")
        return message


def dfs(x, vis, VN_set,VN_dic,firstc,lastc):
    if vis[x]:
        return
        # print(x)
    vis[x]=1
    left = VN_set[x].left
    for i in range(len(VN_set[x].right)):
        right = VN_set[x].right[i]
        if right[0].isupper():
            y = VN_dic[right[:1]]-1
            if len(right)>1 and not right[1].isupper():
                firstc[x].add(right[1])
            dfs(y, vis, VN_set,VN_dic,firstc, lastc)
            for it in firstc[y]:
                firstc[x].add(it)
        else:
            firstc[x].add(right[0])

def dfs1(x, vis, VN_set,VN_dic,firstc,lastc):
    if vis[x]:
        return
    vis[x]=1
    left = VN_set[x].left
    for i in range(len(VN_set[x].right)):
        right = VN_set[x].right[i]
        n = len(right)-1
        if right[n].isupper():
            y = VN_dic[right[n:n+1]]-1
            if len(right)>1 and not right[n-1].isupper():
                lastc[x].add(right[1])
            dfs1(y, vis, VN_set,VN_dic,firstc,lastc)
            for it in lastc[y]:
                lastc[x].add(it)
        else:
            lastc[x].add(right[n])



def reduction(src,VN_set,fa):
    for i in range(len(VN_set)):
        for j in range(len(VN_set[i].right)):
            if check(VN_set[i].right[j],src,fa):
                return VN_set.left
    return ""

def move_reduction(src,VN_set,relation):
    fa =dict()
    for i in range(len(VN_set)):
        left = VN_set[i].left
        for j in range(len(VN_set[i].right)):
            right = VN_set[i].right[j]
            if len(left) == 1 and len(right) ==1:
                _union(left[0],right[0],fa)
    print("步骤", "栈", "优先关系", "当前符号", "剩余符号", "动作")
    stk = []
    steps =1
    src +='#'
    stk.append('#')
    i=0
    while(i<len(src)):
        i+=1
        if not len(stk):
            continue
        top = stk[-1]
        for j in stk[::-1]:
            if not j.isupper():
                top = j
                break
        ch = relation[ord(top)][ord(src[i])]
        if ch == '<' or ch == '=':
            tmp = ""
            
            if i == len(src)-1:
                print("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], "None" , "forward"))
            else:
                print("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i],src[i+1:-(1+i)], "forward"))
            stk.append(src[i])
        else:
            tmp =""
            string = ""
            x = len(stk)-2
            if i == len(src):
                print("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], "None" , "statute"))         
            else:  
                print("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], src[i+1:-(1+i)] , "statute"))
            while(1):
                if not len(stk):
                    break
                if x <0:
                    break
                if not stk[x].isupper() and relation[ord(stk[x])][ord(top)] =='<':
                    break
                x-=1
            while(len(stk)):
                string+=stk.pop()
            if len(string):
                string = reduction(string,VN_set,fa)
            for st in string:
                stk.append(st)
            i-=1
        steps+=1

            
def test(text):
    h_text = []
    for s in text:
        e=[]
        for c in s:
            e.append(c)
        h_text.append(e)
    print(h_text)

def lexer(text):
    message = []
    VN_set =[]
    VT = []
    vis = []
    VN_dic =dict()
    
    firstc=[set() for i in range(507)]
    lastc =[set() for i in range(507)]
    
    relation = [ [' ' for i in range(507)] for j in range(507)]

    for s in text:
        used = [int(0) for i in  range(507)]
        for i in range(len(s)):
            if s[i]=='-':
                break
        if s[:i] not in VN_dic.keys():
            word =WORD(s[:i])
            VN_set.append(word)
            VN_dic[s[:i]] = len(VN_set)

        x = VN_dic[s[:i]]-1

        VN_set[x].insert(s[i+2:])
        for k in range(i):
            if not s[k].isupper():
                if used[ord(s[k])]:
                    continue
                VT.append(s[k])
                used[ord(s[k])] = 1
        for k in range(i+2,len(s)):
            if not s[k].isupper():
                if used[ord(s[k])]:
                    continue
                VT.append(s[k])
                used[ord(s[k])] = len(VT)
    print("************VT集*******************")
    tmp = []
    for m in VT:
        tmp.append(str(m))
    print(tmp)
    print("*************产生式*****************")
    for i in range(len(VN_set)):
        message+=VN_set[i].print()
    print("************************************")
    vis = [0 for i in range(507)]
    for i in range(len(VN_set)):
        if vis[i]:
            continue
        else:
            dfs(x, vis, VN_set,VN_dic,firstc,lastc)
    for ss in VN_set:
        print(ss.left,ss.right)
    print("------------firstVT集-------------------")
    for i in range(len(VN_set)):
        print("{} : ".format(VN_set[i].left),end=' ')
        for t in firstc[i]:
            print("{} ".format(t),end=' ')
        else:
            print("")       


    vis = [0 for i in range(507)]
    for i in range(len(VN_set)):
        if vis[i]:
            continue
        else:
            dfs1(x,vis, VN_set,VN_dic,firstc,lastc)

    print("------------lastVT集-------------------")
    for i in range(len(VN_set)):
        print("{} : ".format(VN_set[i].left),end=' ')
        for t in lastc[i]:
            print("{} ".format(t),end=' ')
        else:
            print("")



    for i in range(len(VN_set)):
        for j in range(len(VN_set[i].right)):
            right = VN_set[i].right[j]
            for k in range(len(right)-1):
                if not right[k:k+2].isupper():
                    relation[ord(right[k])][ord(right[k+1])] = '='
                elif  right[k].isupper():
                    x = VN_dic[right[k:k+1]]-1
                    for t in lastc[x]:
                        relation[ord(t)][ord(right[k+1])] = '>'
                elif right[k+1].isupper():
                    x = VN_dic[right[k+1:k+2]]-1
                    for t in firstc[x]:
                        relation[ord(right[k])][ord(t)] = '<'
                    if right[k+2:k+3].isupper():
                        relation[ord(right[k])][ord(right[k+2])] = '='
    for i in range((len(VT)+1)*10):
        print('-',end='')
    print("算符优先关系表",end='')
    for i in range((len(VT)+1)*10):
        print('-',end='')
    print('')

    print("\n|{:^6s}|".format(" "),end='')

    for i in range(len(VT)):
        print('{:^6s}{:^7s}'.format(VT[i],"|"),end='')
    print('')

    for i in range((len(VT)+1)*10):
        print('-',end='')
    print('')

    for i in range(len(VT)):
        print('|{:^4s}{:^5s}'.format(VT[i],"|"),end='')
        for j in range(len(VT)):
            print("{:^5s}{:^5s}".format(relation[ord(VT[i])][ord(VT[j])],"|"),end='')
        print('')
        for i in range((len(VT)+1)*10):
            print('-',end='')
        print('')
    # move_reduction("i+i",VN_set,relation)


# text = ['S->#E#','P->i','F->P','T->F','E->T','E->E+T']
text = ['E->E+T',
    'E->T',
    'T->F',
    'T->T*F',
    'F->P',
    'F->P^F',
    'P->(E)',
    'P->i']
 
 

lexer(text)     
