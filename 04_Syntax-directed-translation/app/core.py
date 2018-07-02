#-*- coding=utf-8 -*-

# (t1+p)*(2+2)


###################################        grammar         #####################################
'''
基本文法：
M -> +E|-E|E
E -> TE~
E~ -> +TE~|-TE~|&
T -> FT~
T~ -> *FT~|/FT~|&
F -> (E)|indentifer|digit
'''
class Analy_Gram():    
    def __init__(self,dic,word,grammar,quaternary,results):
        self.message =[]
        self.i=0  
        try:           
            
            self.m(dic,word,grammar,quaternary,results)
        except:
            self.message.append('@Error in grammer analysis.') 
            exit(0)
    def m(self,dic,word,grammar,quaternary,results):   
        if(word[self.i]=='+'):
            self.i+=1
            grammar.append('M -> +E')
            self.e(dic,word,grammar,quaternary,results)
        elif(word[self.i]=='-'):
            self.i+=1
            grammar.append('M -> -E')
            self.e(dic,word,grammar,quaternary,results)
        else:
            grammar.append('M -> E')
            self.e(dic,word,grammar,quaternary,results)
        if(self.i is not len(word)-1):  
            self.message.append('@Error in grammer analysis, there should be operator before ( ')
            exit(0)
        else:
           
            self.message.append('||Analysing complete,The grammer tree is :')
            for i in grammar:
                self.message.append(i)

            self.message.append('||Analysing end.')
            results['grammer']=self.message
            
    def e(self,dic,word,grammar,quaternary,results):    
        grammar.append('E -> TE1')
        self.t(dic,word,grammar,quaternary,results)
        self.e1(dic,word,grammar,quaternary,results)
    def e1(self,dic,word,grammar,quaternary,results):   
        if(word[self.i]=='+'):
            self.i+=1
            grammar.append('E1 -> +TE1')
            self.t(dic,word,grammar,quaternary,results)
            self.e1(dic,word,grammar,quaternary,results)
        elif(word[self.i]=='-'):
            self.i+=1
            grammar.append('E1 -> -TE1')
            self.t(dic,word,grammar,quaternary,results)
            self.e1(dic,word,grammar,quaternary,results)
        else:
            grammar.append('E1 -> &')
    def t(self,dic,word,grammar,quaternary,results):    
        grammar.append('T -> FT1')
        self.f(dic,word,grammar,quaternary,results)
        self.t1(dic,word,grammar,quaternary,results)
    def t1(self,dic,word,grammar,quaternary,results):   
        if(word[self.i]=='*'):
            self.i+=1
            grammar.append('T1 -> *FT1')
            self.f(dic,word,grammar,quaternary,results)
            self.t1(dic,word,grammar,quaternary,results)
        elif(word[self.i]=='/'):
            self.i+=1
            grammar.append('T1 -> /FT1')
            self.f(dic,word,grammar,quaternary,results)
            self.t1(dic,word,grammar,quaternary,results)
        else:
            grammar.append('T1 -> &')
    def f(self,dic,word,grammar,quaternary,results):     
        if(word[self.i]=='('):
            grammar.append('F -> (E)')
            self.i+=1
            self.e(dic,word,grammar,quaternary,results)
            if(word[self.i]!=')'):
                raise Exception
            self.i+=1
        elif(dic[word[self.i]]==1):
            grammar.append('F -> Indentifer '+str(word[self.i]))
            self.i+=1
        elif(dic[word[self.i]]==2):
            grammar.append('F -> Digit '+str(word[self.i]))
            self.i+=1
        else:
            raise Exception
 
 
 
#######################################       Sema        #######################################
 
class Analy_Sema:
    def __init__(self,dic,word,grammar,quaternary,results):
        self.message =[]
        self.message.append('Quaternary :')
        self.i=0   
        self.flag=0   
        self.m(dic,word,grammar,quaternary,results)
        for i in quaternary:        
            self.message.append(i)
        
        results['sema'] = self.message
        
    def m(self,dic,word,grammar,quaternary,results):       
        if(word[self.i]=='+'):
            self.i+=1
            ret1=self.e(dic,word,grammar,quaternary,results)
            quaternary.append('(+,0,'+ret1+',out)')
            self.flag+=1
        elif(word[self.i]=='-'):
            self.i+=1
            ret2=self.e(dic,word,grammar,quaternary,results)
            quaternary.append('(-,0,'+ret2+',out)')
            self.flag+=1
        else:
            ret3=self.e(dic,word,grammar,quaternary,results)
            quaternary.append('(=,'+ret3+',0,out)')
    def e(self,dic,word,grammar,quaternary,results):        
        ret1=self.t(dic,word,grammar,quaternary,results)
        ret2,ret3=self.e1(dic,word,grammar,quaternary,results)
        if(ret2!='&'):     
            self.flag+=1
            quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
            return 'T'+str(self.flag)
        else:
            return ret1
    def e1(self,dic,word,grammar,quaternary,results):        
        if(word[self.i]=='+'):
            self.i+=1
            ret1=self.t(dic,word,grammar,quaternary,results)
            ret2,ret3=self.e1(dic,word,grammar,quaternary,results)
            if(ret2=='&'):
                return '+',ret1
            else:
                self.flag+=1
                quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
                return '+','T'+str(self.flag)
        elif(word[self.i]=='-'):
            self.i+=1
            ret1=self.t(dic,word,grammar,quaternary,results)
            ret2,ret3=self.e1(dic,word,grammar,quaternary,results)
            if(ret2=='&'):
                return '-',ret1
            else:
                self.flag+=1
                quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
                return '-','T'+str(self.flag)
        else:
            return '&','&'
    def t(self,dic,word,grammar,quaternary,results):        
        ret1=self.f(dic,word,grammar,quaternary,results)
        ret2,ret3=self.t1(dic,word,grammar,quaternary,results)
        if(ret2!='&'):
            self.flag+=1
            quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
            return 'T'+str(self.flag)
        else:
            return ret1
    def t1(self,dic,word,grammar,quaternary,results):       
        if(word[self.i]=='*'):
            self.i+=1
            ret1=self.f(dic,word,grammar,quaternary,results)
            ret2,ret3=self.t1(dic,word,grammar,quaternary,results)
            if(ret2=='&'):
                return '*',ret1
            else:
                self.flag+=1
                quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
                return '*','T'+str(self.flag)
        elif(word[self.i]=='/'):
            self.i+=1
            ret1=self.f(dic,word,grammar,quaternary,results)
            ret2,ret3=self.t1(dic,word,grammar,quaternary,results)
            if(ret2=='&'):          
                return '/',ret1
            else:
                self.flag+=1
                quaternary.append('('+ret2+','+ret1+','+ret3+',T'+str(self.flag)+')')
                return '/','T'+str(self.flag)
        else:
            return '&','&'
    def f(self,dic,word,grammar,quaternary,results):      
        if(word[self.i]=='('):
            self.i+=1
            ret1=self.e(dic,word,grammar,quaternary,results)
            self.i+=1
            return str(ret1)
        elif(dic[word[self.i]]==1):        
            temp=self.i
            self.i+=1
            return word[temp]
        elif(dic[word[self.i]]==2):       
            temp=self.i
            self.i+=1
            return word[temp]
def lexer(string):
    dic={}  
    word=[]   
    grammar=[]  
    quaternary=[]  
    results={}
    letter='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='0123456789'
    operater='+-*/()'

    type_dic={1:'Identifier',2:'Number',3:'Operator'}
    analysis= []

    m=0
    state=0      #1：为Identifier 2：为Number串 3：为Operator
    for i in range(len(string)):
        if string[i] in operater :  
            if state==1:        
                tmp = "|| {} Is {},Type Code： {} "
                analysis.append(tmp.format(string[m:i],type_dic[state],state))
                dic[string[m:i]]=1
                word.append(string[m:i])
            elif state==2:     
                tmp = "|| {} Is {},Type Code： {} "
                analysis.append(tmp.format(string[m:i],type_dic[state],state))                
                dic[string[m:i]]=2
                word.append(string[m:i])
            m=i+1
            state=3
            tmp = "|| {} Is {},Type Code： {} "
            analysis.append(tmp.format(string[i],type_dic[state],state))            
            dic[string[i]]=3
            word.append(string[i])
        elif string[i] in number:    
            if i==m:        
                state=2
        elif string[i] in letter:
            if state==2:   
                analysis.append('|| {} Error'.format(type_dic[state]))
                exit(0)
            if i==m:       
                state=1
        else:              
            analysis.append('|| {} Error'.format(type_dic[state]))
            exit(0)
    if state==1:       
        tmp = "|| {} Is {},Type Code： {} "
        analysis.append(tmp.format(string[m:],type_dic[state],state))  

        dic[string[m:]]=1
        word.append(string[m:])
    elif state==2:      
        tmp = "|| {} Is {},Type Code： {} "
        analysis.append(tmp.format(string[m:],type_dic[state],state))  
        dic[string[m:]]=2
        word.append(string[m:])
    word.append('#')
    tmp = 'Symbol stack: {} '
    analysis.append(tmp.format(word))
    analysis.append('Correct')
    results['analysis'] =analysis
    Analy_Gram(dic,word,grammar,quaternary,results)
    Analy_Sema(dic,word,grammar,quaternary,results)
    return results
 

if __name__=='__main__':
    text='(t1+p)*(2+2)'
    res=lexer(text)
    for h,r in res.items():
        for i in r:
            print(i)

