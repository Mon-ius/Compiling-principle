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
        fa[x]=x
    if y not in fa.keys():
        fa[y]=y
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
        self.left = left
        self.right = []
    def insert(self,right):
        self.right.append(right)
    def put(self):
        message=""
        st = "{} -> {} ".format(self.left,self.right[0])
        message+= st
        for m in self.right[1:]:
            message+="|{} ".format(m)
        return message


def dfs(x, vis, VN_set,VN_dic,firstc,lastc):
    if vis[x]:
        return
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

def move_reduction(src,VN_set,relation,output):
    fa =dict()
    for i in range(len(VN_set)):
        left = VN_set[i].left
        for j in range(len(VN_set[i].right)):
            right = VN_set[i].right[j]
            if len(left) == 1 and len(right) ==1:
                _union(left[0],right[0],fa)
    output.append("Steps Stack Priority Sympol(N) Sympol(L) Action")
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
                output.append("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], "None" , "forward"))
            else:
                output.append("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i],src[i+1:-(1+i)], "forward"))
            stk.append(src[i])
        else:
            tmp =""
            string = ""
            x = len(stk)-2
            if i == len(src):
                output.append("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], "None" , "statute"))         
            else:  
                output.append("{} {} {} {} {} {}".format(tmp+str(steps+48),stk,tmp+ch,tmp+src[i], src[i+1:-(1+i)] , "statute"))
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

def lexer(text):
    output=[]
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
    output.append("---------------VT-------------------")

    tmp = []
    for m in VT:
        tmp.append(str(m))
    output.append(tmp)
    output.append("-----------Production---------------")
    for i in range(len(VN_set)):
        output.append(VN_set[i].put())
    output.append("------------------------------------")
    vis = [0 for i in range(507)]
    for i in range(len(VN_set)):
        if vis[i]:
            continue
        else:
            dfs(i, vis, VN_set,VN_dic,firstc,lastc)

    output.append("------------firstVT-----------------")

    
    for i in range(len(VN_set)):
        message = ""
        message+="{} : ".format(VN_set[i].left)
        for t in firstc[i]:
            message+="{} ".format(t)
        output.append(message)  
    vis = [0 for i in range(507)]
    for i in range(len(VN_set)):
        if vis[i]:
            continue
        else:
            dfs1(i,vis, VN_set,VN_dic,firstc,lastc)

    output.append("-------------lastVT-----------------")
    for i in range(len(VN_set)):
        message = ""
        message+="{} : ".format(VN_set[i].left)
        for t in lastc[i]:
            message+="{} ".format(t)
        output.append(message)

    for i in range(len(VN_set)):
        for j in range(len(VN_set[i].right)):
            right = VN_set[i].right[j]
            for k in range(len(right)-1):
                if not right[k:k+1].isupper() and not right[k+1:k+2].isupper():
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
    message = ""
    for i in range((len(VT)+1)):
        message+= '-'
    message+="Sympol Priority Table"
    for i in range((len(VT)+1)):
        message+= '-'
    output.append(message)

    message = ""
    message+="\n|{:^6s}|".format(" ")

    for i in range(len(VT)):
        message+='{:^6s}{:^7s}'.format(VT[i],"|")
    output.append(message)

    message = ""
    for i in range((len(VT)+1)*5):
        message+='-'
    output.append(message)

    for i in range(len(VT)):
        message = ""
        message+='|{:^4s}{:^5s}'.format(VT[i],"|")
        for j in range(len(VT)):
            message+="{:^5s}{:^5s}".format(relation[ord(VT[i])][ord(VT[j])],"|")
        output.append(message)
        message = ""
        for i in range((len(VT)+1)*5):
            message+= '-'
        output.append(message)
    # move_reduction("i+i",VN_set,relation,output)
    return output


# text = ['S->#E#','P->i','F->P','T->F','E->T','E->E+T']
# text = ['E->E+T',
#     'E->T',
#     'T->F',
#     'T->T*F',
#     'F->P',
#     'F->P^F',
#     'P->(E)',
#     'P->i']
 
 

# lexer(text)
# print(output)  
