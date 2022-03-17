# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:22:43 2020

@author: KITCOOP
"""
from numpy import nan as NA 
from numpy import isnan

dir("numpy")


L1 = [1,NA,2,NA,3,NA,4]
L2 = [1,2,3,4,5,6,7]

L1=[NA,1,2]

1. nvl([NA,1,2], 0) = [0,1,2]

def nvl(x, y) :
    for i in x:
        if isnan(i):
            result=[y]
        else:
            result.append(i)
    return(result)

nvl([NA, 1,2], 0)

2. nvl2([NA,1,2],'not na', 'na') = ['na','not na', 'not na']

def nvl2(x, y, z) :
    for i in x:
        if isnan(i):
               result=[z]
        else:
            result.append(y)
    return(result)
    
nvl2([NA,1,2], 'not na', 'na')    

3. f_fillna(L1,'ffill') = [1,1,2,2,3,3,4] #이전값으로 치환

def f_fillna(x,y):
    for i in x:
        if isnan(i):
            result=x[i-1]
                
    len(L1)        
    return(result)
    
  

4. f_fillna(L1,'bfill') = [1,2,2,3,3,4,4] #이후값으로 치환 
   
   
5. f_shift(L2,1) = [1,1,2,3,4,5,6] #이전값으로 치환

def f_shift(x,y):
    inlist=[]
    outlist=[]
    for i in range(0,len(x)):
        if i==0:
            result=[1]
        else:
            inlist=x[i-y]
            outlist.append(inlist)            
    return(result+outlist)
    
f_shift(L2,1)


6. f_shift(L2,2) = [1,1,1,2,3,4,5] #이후값으로 치환

def f_shift(x,y):
    inlist=[]
    outlist=[]
    for i in range(0,len(x)):
        if i==0:
            result=[1]
        else:
            result=x[i-y]
            outlist.append(result)
    return(outlist)
    
f_shift(L2,2)


