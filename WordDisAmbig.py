import string
import glob
import timeit
from collections import OrderedDict
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
start_time = timeit.default_timer()
dic={}
###########################################################
def context(ind, text):
    global dic
    tokens=0
    j=0
    i=ind-10
    if i<0:
        i=0
    mycontext=[]
    
    while i!=ind:
        mycontext.append(0)
        mycontext[j]=text[i]
        if text[i] in dic:
            dic[text[i]]+=1
        else:
            dic[text[i]]=1
        j +=1
        i +=1
        tokens +=1
    i=ind+10
    if i>len(text):
        i=len(text)-1
        #mycontext[j]=text[ind]
    ind2=ind
    while ind2<i and ind2 <len(text)-1:
        mycontext.append(0)
        mycontext[j]=text[ind2+1]
        if text[ind2+1] in dic:
            dic[text[ind2+1]]+=1
        else:
            dic[text[ind2+1]]=1
        j +=1
        ind2 +=1
        tokens +=1

    
    mycontext.append(text[ind])
    #mycontext[20]=text[ind]
    return mycontext,tokens;
########################################################### 
context1=[]
count1=count2=count3=count4=count5=count6=0
dicw1={}
dicw2={}
dicw3={}
dicw4={}
dicw5={}
dicw6={}
tokens1=tokens2=tokens3=tokens4=tokens5=tokens6=0
contextIndex=0
seudowords=['country', 'told','political', 'world','analysis', 'study']
def createconstextlist(allTokens):
    global count1
    global count2
    global count3
    global count4
    global count5
    global count6
    global tokens1
    global tokens2
    global tokens3
    global tokens4
    global tokens5
    global tokens6
    global context1
    global contextIndex
    global dicw1
    global dicw2
    global dicw3
    global dicw4
    global dicw5
    global dicw6
    tokens=0
    for i in range(len(allTokens)):
        for j in range(len(allTokens[i])):
            if count1<50 and seudowords[0]==allTokens[i][j]:
                context1.append([])
                context1[contextIndex],tokens=context(j,allTokens[i])[:]
                if count1<=40:
                    
                    tokens1 +=tokens
                    for index in range(len(context1[contextIndex])):
                        if context1[contextIndex][index] in dicw1:
                            dicw1[context1[contextIndex][index]] +=1
                        else:
                            dicw1[context1[contextIndex][index]] =1

                tokens=0
                contextIndex +=1
                count1 +=1
        for i in range(len(allTokens)):
            for j in range(len(allTokens[i])):
                if count2<50 and seudowords[1]==allTokens[i][j]:
                    context1.append([])
                    context1[contextIndex],tokens=context(j,allTokens[i])[:]
                    if count2<=40:
                        tokens2 +=tokens
                        for index in range(len(context1[contextIndex])):
                            if context1[contextIndex][index] in dicw2:
                                dicw2[context1[contextIndex][index]] +=1
                            else:
                                dicw2[context1[contextIndex][index]] =1
                    tokens=0
                    contextIndex +=1
                    count2 +=1
        for i in range(len(allTokens)):
            for j in range(len(allTokens[i])):
                if count3<50 and seudowords[2]==allTokens[i][j]:
                    context1.append([])
                    context1[contextIndex],tokens=context(j,allTokens[i])[:]
                    if count3<=40:
                        tokens3 +=tokens
                        for index in range(len(context1[contextIndex])):
                            if context1[contextIndex][index] in dicw3:
                                dicw3[context1[contextIndex][index]] +=1
                            else:
                                dicw3[context1[contextIndex][index]] =1
                    tokens=0
                    contextIndex +=1
                    count3 +=1
        for i in range(len(allTokens)):
            for j in range(len(allTokens[i])):
                if count4<50 and seudowords[3]==allTokens[i][j]:
                    context1.append([])
                    context1[contextIndex],tokens=context(j,allTokens[i])[:]
                    if count4<=40:
                        tokens4 +=tokens
                        for index in range(len(context1[contextIndex])):
                            if context1[contextIndex][index] in dicw4:
                                dicw4[context1[contextIndex][index]] +=1
                            else:
                                dicw4[context1[contextIndex][index]] =1
                    tokens=0
                    contextIndex +=1
                    count4 +=1
        for i in range(len(allTokens)):
            for j in range(len(allTokens[i])):
                if count5<50 and seudowords[4]==allTokens[i][j]:
                    context1.append([])
                    context1[contextIndex],tokens=context(j,allTokens[i])[:]
                    if count5<=40:
                        tokens5 +=tokens
                        for index in range(len(context1[contextIndex])):
                            if context1[contextIndex][index] in dicw5:
                                dicw5[context1[contextIndex][index]] +=1
                            else:
                                dicw5[context1[contextIndex][index]] =1
                    tokens=0
                    contextIndex +=1
                    count5 +=1
        for i in range(len(allTokens)):
            for j in range(len(allTokens[i])):
                if count6<50 and seudowords[5]==allTokens[i][j]:
                    context1.append([])
                    context1[contextIndex],tokens=context(j,allTokens[i])[:]
                    if count1<=40:
                        tokens6 +=tokens
                        for index in range(len(context1[contextIndex])):
                            if context1[contextIndex][index] in dicw6:
                                dicw6[context1[contextIndex][index]] +=1
                            else:
                                dicw6[context1[contextIndex][index]] =1
                    tokens=0
                    contextIndex +=1
                    count6 +=1

    return;
unihashtable={}
lochashtable={}
files=glob.glob('/Users/mohammed/Dropbox/mywork/python/files/*.html')
#contextfile=open('/Users/mohammed/Dropbox/mywork/python/ff/out.txt','w')
numDocs=0
allTokens=[]
for html in files:
    open_html=open(html)
    soup=BeautifulSoup(open_html)
    open_html.close()
    [s.extract() for s in soup (['title','head','script',['document']])]
    ########################################################### removing punctuations
    punc=set(string.punctuation)
    text = ''.join(ch for ch in soup.text if ch not in punc and not ch.isdigit())
    ########################################################### removing stopwords
    stops=set(stopwords.words("english"))
    text = ' '.join([word for word in text.split() if word not in stops])
    text=text.encode('utf-8').lower()
    #print text
    #print "#############################"
    ########################################################### creating array of words
    predata=text.split()
    allTokens.append([])
    allTokens[numDocs]=predata[:]
    numDocs +=1 
    for i in range(len(predata)):
               
                # print i
    ########################################################### building frequency dictionary
        if predata[i] in unihashtable:
            unihashtable[predata[i]]+=1
        else:
            unihashtable[predata[i]]=1
###########################################################    
#contextfile.close()
no_of_unigrams=sum(unihashtable.values())
#print no_of_unigrams
dictionary=OrderedDict(sorted(unihashtable.items(), key=lambda t: t[1],reverse=True))
#out=open('/Users/mohammed/Dropbox/mywork/python/output.txt','w')
#i=0
#for k,v in dictionary.items():
#    out.write("%s %s\n"%(k,v))
#    i +=1
#    if i==3:
#        break

#out.close()
#to return contexts +/- 10 from the document
createconstextlist(allTokens)
#print count1
#print count2
#print count3
#print count4
#print count5
#print count6
#for i in range(len(context1)):
#    print context1[i]
#country', 'told','political', 'world','analysis', 'study
#to calculate the probability of each class or word in suedo words
pw=[]
pw.append(0)
pw[0]=count1/(len(context1)*1.0)
pw.append(0)
pw[1]=count2/(len(context1)*1.0)
pw.append(0)
pw[2]=count3/(len(context1)*1.0)
pw.append(0)
pw[3]=count4/(len(context1)*1.0)
pw.append(0)
pw[4]=count5/(len(context1)*1.0)
pw.append(0)
pw[5]=count6/(len(context1)*1.0)
#print tokens2
#print tokens3
#print tokens4
#print tokens5
#print tokens6
#print tokens1

v=len(dic)
#print v
ppp=[]
for w in range(40,50):
    for k in range(6):
        prop=1.0
        for i in range(len(context1[w])-1):
            d=context1[w][i]
            if k==0 and bool(dicw1) and dicw1.has_key(d):
                prop =prop*(dicw1[d]+1.0)/(tokens1+v)
            elif k==1 and bool(dicw2) and dicw2.has_key(d):
                prop =prop*(dicw2[d]+1.0)/(tokens2+v)
            elif k==2 and bool(dicw3) and dicw3.has_key(d):
                prop =prop*(dicw3[d]+1.0)/(tokens3+v)
            elif k==3 and bool(dicw4) and dicw4.has_key(d):
                prop =prop*(dicw4[d]+1.0)/(tokens4+v)
            elif k==4 and bool(dicw5) and dicw5.has_key(d):
                prop =prop*(dicw5[d]+1.0)/(tokens5+v)
            elif k==5 and bool(dicw6) and dicw6.has_key(d):
                prop =prop*(dicw6[d]+1.0)/(tokens6+v)
        ppp.append(0)
        ppp[k]=pw[k]*prop
        print k,"- ",ppp[k]
elapsed = timeit.default_timer() - start_time
print elapsed