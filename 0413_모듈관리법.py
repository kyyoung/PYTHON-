# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:23:14 2020

@author: KITCOOP
"""

def fsum(v1,v2):
    result=[]
    for i, j in zip(v1,v2):
        result.append(i+j)
    return result

#save as , 디폴트 디렉토리 --> my_func.py 파일로 저장 
#ipython에서 실행하는 방법 
# cmd --> ipython 실행 하면 됨 

