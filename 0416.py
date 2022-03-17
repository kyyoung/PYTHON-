# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:21:46 2020

@author: KITCOOP
"""

[연습문제]
disease.txt파일을 읽고(컬럼명 생략) 맨 마지막 컬럼 데이터를 
소수점 둘째자리까지 표현 후 다시 새로운 파일에 저장 

c1= open('disease.txt')

v1=c1.readlines()

c1.close()

#Step1 - 파일 불러온 후 저장 
def f_read_txt(file, sep = ' ', fmt = int):
    c1 = open(file, 'r') #커서 선언 
    v1 = c1.readlines()  #fetch 
    c1.close()
    
    outlist = []
    
    for i in v1:
        L1=i.strip().split(sep)
        outlist.append([fmt(i) for i  in L1])
    
    return outlist

L1=f_read_txt('disease.txt', sep='\t', fmt=str)  #sep 구분기호에 그냥 '\t'넣으면 됨 

#Step2 - 컬럼 선택을 위한 array로 변경 
arr1=np.array(L1)
arr1[:, -1]

#Step3 - NA 치환, mapping처리 
arr1[:, -1].replace('NA', 0) #replace함수 array 적용 불가 

f1= lambda x : x.replace('NA', '0')
list(map(f1,arr1[:,-1]))

#step3) 형식 변경 

f1= lambda x : '%.2f' % int(x.replace('NA', '0')) #실제 실수데이터로 바꾸는건 아니고 보여주는거! 
arr1[:,-1]=list(map(f1,arr1[:,-1]))

#step4) 외부 파일에 저장 
def f_write_txt(vname, fname, sep=' ', fmt='%.2f'):
    c1 = open(fname, 'w')
    for i in vname:
        vstr=''
        for j in i : 
            j = fmt % j   #문자열로 바뀜 
            vstr = vstr + j + sep 
        vstr = vstr.rstrip(sep)
        c1.writelines(vstr + '\n')
    c1.close()
    
f_write_txt(arr1, 'disease2.txt', sep='\t', fmt='%s')


#asarray 
-array로의 형 변환 함수 
-얕은 복사 수행 (deep copy 발생 X)

L1=[1,2,3,4]
arr1 = np.array(L1) #정수
arr2=np.array(arr1, dtype='float')  #실수  
arr3=np.asarray(arr1, dtype='float') #실수, 기존데이터의 형 변환시 새로운 객체로 생성 

arr1과 arr2/arr3은 deep copy - 형태가 다름 
#-
arr1[0]=10 
arr2   #변경X, deep copy 발생 O
arr3   #변경X, deep copy 발생 O
#arr1만 변환됨 

#똑같은 데이터 타입을 갖는 배열 재생성 
arr1 = np.array(L1) #정수
arr2=np.array(arr1)  
arr3=np.asarray(arr1) 

arr1[0]=10  #변경
arr2        #변경X, deep copy 발생 O
arr3        #변경O, deep copy 발생 X 

#형변환 함수(벡터연산 가능)
arr1.astype('float')

#예제) 다음 배열의 타입을 실수로 변경 
arr1 = np.array([1,2,3,4])

#1) 형변환 함수 사용(벡터연산 불가)
float(arr1)  #오류, 스칼라에만 적용 가능- 벡터연산 불가  
list(map(lambda x : float(x), arr1)) #가능, 리스트로 출력 

#2) 형변환 메서드 사용(벡터연산 가능)
arr1.astype('float')

#[연습문제 : 다음 값의 10% 인상된 값 출력]
arr2 = np.array(['1,100', '2,200', '3,300'])
list(map(lambda x: int(x.replace(',', ''))*1.1, arr2))

outlist=[]
for i in arr2:
    v1=i.replace(',' , '')
    outlist.append(v1)
    
arr3=np.array(outlist)
arr3 = arr3.astype('float')
arr3 *1.1

#선생님 

f2=lambda x: int(x.replace(',' , ''))  #가능
f3=lambda x: x.replace(',', '' ).astype('int')  #불가능 

list(map(f2,arr2))
list(map(f3,arr2))  #문자열에 astype 메서드 호출 불가 

#산술연산 함수 및 메서드
arr1 = np.arange(1,10).reshape(3,3)
arr1.sum()  #합
arr1.mean() #평균
arr1.var() #분산
arr1.std() #표준편차

np.sum(arr1)
np.mean(arr1)
np.var(arr1)
np.std(arr1)

np.sum(arr1, axis=0)  #[12,15,18]의 값 리턴 행별 총합?
np.sum(arr1, axis=1)

[참고 : 축방향]

[1,2,3]
[4,5,6]
[7,8,9]

in python
행별 :  컬럼을 고정한 채 서로 다른 행 끼리라는 의미, 1컬럼의 1행 2행 3행 [1,4,7]  
컬럼별 : 행을 고정한 채 서로 다른 컬럼끼리라는 의미 [1,2,3]
in R 
행별 :  서로 같은 행끼리 묶어 전달, 컬럼 고정 1행, 2행 ...[1,2,3]
컬럼별 : 같은 컬럼 [1,4,7]

#예제 
arr3= np.arange(1,25).reshape(2,-3,4)
array([[[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]],

       [[13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]]])
    
층별 : 층만 다른 원소의 묶음 
[1,13], [2,14], [3,15] ...     

np.sum(arr3, axis=0) 
np.sum(arr3, axis=1) #행별
np.sum(arr3, axis=2) #열별 

#[참고 :  축 번호] ***** 중요  
# 1) 2차원  
in R 
행 열 
1  2

in python
행 열 
0  1

# 2) 3차원 
in R 
행 열 층 
1  2  3

in python
층 행 열
0  1  2

# 연습문제 
# 다음의 배열에서 각 행별, 열별 총합, 평균, 분산을 구하여라
# 단 분산은 분산함수를 사용하지 않고 직접 계산하여라 
#(분산 = 편차^2합의 평균)

arr4 = np.arange(1,10).reshape(3,3)

np.sum(arr4, axis=0) #행별
np.sum(arr4, axis=1) #열별
np.mean(arr4, axis=0)  #평균
np.var(arr4) #분산 
np.sum((arr4 -np.mean(arr4))**2)/9

#선생님 
arr4.sum(axis=0)
arr4.sum(axis=1)

arr4.mean(axis=0)
arr4.mean(axis=1)

#행별 분산 
np.var(arr4, axis=0) #6
np.mean((arr4 - arr4.mean(axis=0))**2)

#컬럼별 분산 
np.var(arr4, axis=1) #0.66
np.mean((arr4 - arr4.mean(axis=1).reshape(3,1))**2)

#참고 - pandas에서의 분산/ 표준편차 계산식 
from pandas import DataFrame 
df1 = DataFrame(arr4)
df1.var(axis=0) #9 , pandas에서의 분산은 편차제곱의합/(n-1)으로 계산 즉 편차제곱의 합(n-자유도)
df1.var(axis=1) #1

df1.var(axis=0, ddof=0) #9 , 자유도를 0으로 하면 편차제곱의 합/(n)으로 계산, numpy에서의 분산식과 동일함  
df1.var(axis=1, ddof=0) #1


df1.var?  #자유도가 1
np.var?   #자유도가 0 

