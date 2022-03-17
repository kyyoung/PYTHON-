# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:15:46 2020

@author: KITCOOP
"""
 
# NA
import numpy as np
np.nan # R에서 NA와 비슷 
from numpy import nan as NA # nan 명령어에 NA alias 
 

arr1 = np.array([1,2,3,4])
arr1[0] = NA #수정불가 , np.nan는 실수타입이기 때문에 정수로 선언되어있는 배열에 실수를 삽입할 수 없음 
float(arr1) #수정불가, mapping 처리해야함 
list(map(lambda x: float(x), arr1))
arr1 = arr1.astype('float')
arr1[0] = NA #수정가능 
arr1

np.isnan(arr1) #NA 존재 여부 T/F
np.isnan(arr1).any() #NA가 하나라도 있는가?
np.isnan(arr1).sum() #NA 존재하는 개수 

#파일 불러오는 방법 
np.loadtxt(fname,  #파일명 
           dtpye,  #데이터 형식 
           delimiter,  #분리구분기호 
           skiprows,   #skip 할 행 
           usecols )   #불러올 컬럼 

np.loadtxt('test1.txt', dtype='str', delimiter = ':', skiprows=2, usecols=[0,1]) 
#불러들어오는 파일이 문자열타입이기때문에 문자열로 지정, delimiter 분리구분기호, 
#skiprows2개의 행 삭제, usecols 선택한 컬럼 번호 

#파일 저장 방법
np.savetxt(fname,   #파일명 
           X,       #저장할 객체 
           delimiter, #분리구분 기호
           fmt='%.2f')  #출력할 포맷 

# 참고 : profile 만들기 
파이썬 실행시 기본으로 불러와야 할 모듈을 .py파일로 생성, 
"run file명"을 통해 모듈을 동시 호출 
디렉토리 폴더에 profile1.py 파일 저장 
import numpy as np 
import pandas as pd 

from math import trunc 

from numpy import nan as NA 
from pandas import Series 
from pandas import DataFrame 

run profile1 #profile1.py 파일 불러오기 
Series([1,2,3,4])


#연습문제 
#1. 1부터 증가하는 3*4*5 배열 생성 후 
1) 모든 값에 짝수는 *2 홀수는 *3을 연산하여 출력 
arr1=np.arange(1,61)
arr1 = list(map(lambda x: x*2 if x%2==0 else x*3, arr1))
arr1=np.array(arr1).reshape(3,4,5)

#선생님 
np.where(arr1 % 2 ==0, arr1*2, arr1*3)
2) 각 층의 첫번째, 세번째 행의 두번째, 네번재 컬럼 선택하여 NA로 치환 
위의 수정된 배열에서 NA 개수 확인 
층별 누적합 확인 
arr1 = arr1.astype('float')
arr1[:,:,:][:,[0,2], :][:,:,[1,3]] = NA #중복 색인된 결과는 수정 불가  

#선생님 
arr1[np.ix_([0,1,2], [0,2],[1,3])] = NA #수정 가능 
np.isnan(arr1).sum()
arr1.cumsum(axis=0)

#2. emp.csv 파일을 array 형식으로 불러온 뒤 다음 수행(컬럼명 제외)
1) 이름이 smith와 allen의 이름, 부서번호, 연봉출력 
def f_read_txt(file, sep = ' ', fmt = int):
    c1 = open(file, 'r') #커서 선언 
    v1 = c1.readlines()  #fetch 
    c1.close()
    
    outlist = []
    
    for i in v1:
        L1=i.strip().split(sep)
        outlist.append([fmt(i) for i  in L1])
    
    return outlist

L1=f_read_txt('emp.csv', sep=',', fmt=str) 
arr2= np.array(L1)

arr2[1:3, (1,5,7) ]

#선생님 
arr2 = np.loadtxt('emp.csv', delimiter = ',' , dtype = 'str', skiprows=1)
arr2[:,1] in ['SMITH', 'ALLEN'] #불가 
 'SMITH' in ['SMITH', 'ALLEN'] #가능
 
vbool = list(map(lambda x : x in ['SMITH', 'ALLEN'], arr2[:,1]))
arr2[vbool, :]
arr2[np.ix_(vbool, [1,-1,-3])]

#sol1( in1d 함수)
vbool2 = np.in1d(arr2[:,1], ['SMITH', 'ALLEN']) #벡터연산 가능한 포함연산자
arr2[np.ix_(vbool2, [1,-1,-3])]

2) deptno가 30번 직원의 comm 총합 
arr2[1:, 7]=='30'

np.where(arr2[1:, 7]=='30', np.sum(arr2[:,-2]) )

#선생님 
arr2[:,-2]=np.where(arr2[:,-2]=='','0', arr2[:,-2])

(arr2[arr2[:,-1]=='30', -2]).astype('int').sum()

#pandas
-DataFrame 생성 및 전처리에 필요한 기본 함수 내장된 모듈
-주로 NA에 대한 연산이 빠르고 쉽게 되어 있음 
-산술연산에 대해 벡터 연산 가능 
-문자열 처리 벡터연산 불가 => mapping처리 필요(map, apply, applymap)

#Series 
-DataFrame을 구성하는 기본 구조 
-1차원, 하나의 데이터 타입만 허용
-key-value 형식의 자료구조, key는 index를 의미(행번호)
-주로 DataFrame의 컬럼을 표현 

s1=Series([1,2,3,4])
s2=Series([1,2,3,4,'5'])
s3 = Series([1,2,3,4], index = ['a','b','c','d'])
s4 = Series([10,20,30,40], index = ['a','b','c','d'])
s5 = Series([10,20,30,40,50], index = ['A','b','c','d','e']) 

#2. 연산 
s1+1 #Series와 scalar 연산 가능
s3 + s4 #서로 같은 index 갖는 Series 연산 가능 
s3 + s5 #서로 다른 index 갖는 경우 outer join식 연산처리(b,c,d만 연산)
        #데이터 타입 float으로 바뀜, 한쪽에만 존재하는 키가 NaN 처리되기 위해
#3. 색인 
s1[0]
s1[0:3]
s1[[0,3]]
s1[s1>2]

#4. 기타 메서드 

s1.dtype #Series  구성 데이터 타입 
s1.dtypes #복수형가능 

s1.index #Series의 key값(index)
s1.values #Series의 데이터 

#5. reindex
s1 = Series([1,2,3,4], index =['a','b','c','d']) #key값이 없는 경우 : index 설정
s2 = Series(s1, index=['A', 'B', 'C', 'D']) 
#위의 경우 'A', 'B', 'C', 'D' 인덱싱 값이 없어서 NaN으로 치환됨 
s2 = Series(s1, index=['b', 'a', 'c', 'd']) #key값이 부여된 경우 :  index 순서대로 재배치 
s1[['A','B','C','D']]

# 예제 
# 다음의 리스트를 금,화,수,월,목,일,토 인덱스 값을 갖도록 시리즈로 생성 후 월~일 순서로 재배치 
s1 = Series([4,3,1,10,9,5,1], index = ['금','화','수','월','목','일','토'])
s2 = Series(s1, index=['월','화','수','목','금','토','일'])

#6. 인덱스 수정 
s1.index = ['월','화','수','목','금','토','일']

s1.index[0]='a' #index object에 대한 수정 금지 
s1.index #index  object 타입이기때문에 값만 빼와서 수정해야함 
s1.index.values[0] = 'a' # 값만빼온 후 수정해야함

#연습문제 : 다음의 시리즈 첫번째 인덱스 값을 10으로 수정 
s1 = Series([1,2,3,4]) 
s1.index # series  자동생성, range index 
s1.index[0]=10 #에러발생, index object 직접 수정 불가 
s1.index.values[0]=10 # 자동생성된 range index(0,1,2,3 ...)는 원본 수정안됨 

a1 = s1.index.values # index 값을 갖는 새로운 객체 생성 
a1[0] = 10  #수정 후
s1.index = a1 # 다시 index에 덮어쓰는 방식으로 전체를 수정해야함 

#비교 : 색인 직접지정해주는 경우- 위의 값과 눈으로는 결과가 비슷해도 
#색인을 직접 지정해주는 경우, 일부 수정 가능함 
s2= Series([1,2,3,4], index = [0,1,2,3])
s2.index.values[0]=10

