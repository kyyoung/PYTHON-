# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:15:07 2020

@author: KITCOOP
"""

#deep copy 
arr1 = np.arange(1,10)
arr2 = arr1[0:5]  #슬라이스 객체는 deep copy 발생 안함 
arr1[0] = 10 
arr2  #같이 변경되어있음 

arr3 = arr1[0:5].copy() # deep copy 발생 시킴, 기존 객체와 완전하게 다르게 저장함. oracle view와 유사한 개념  
arr1[1] = 20 
arr1 
arr2 #arr1과 같이 변경됨 
arr3

#조건색인(boolean indexing)
L1=[1,2,3,4,5]  #리스트는 벡터연산 불가라 조건색인 불가
L1 >3 
L1[[True,False,False,False,False]]

arr1 = np.arange(1,10).reshape(3,3) #어레이는 가능
arr1[arr1>5]

#예제) 세번째 컬럼의 값이 6인 행 선택 
arr1[arr1[:,2]==6, :]

#예제) 세번째 컬럼의 값이 6이 아닌 행 선택(조건의 부정)
arr1[arr1[:,2]!= 6, :]

arr1[~(arr1[:,2]==6), :]

# =============================================================================
# #np.where
# 조건의 벡터 연산 
# R의 ifelse 구문과 비슷
# 조건에 대한 단순리턴만 가능 
# =============================================================================

#예제) 다음의 배열에서 5보다 크면 'A' 작거나 같으면 'B'리턴 
arr3 = np.arange(1,10)
np.where(arr3>5, 'A', 'B')

#연습문제 
#1. emp.csv 파일의 부서번호를 사용, 부서이름 출력 
#10이면 인사부 20이면 총부무 30이면 재무부 

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
arr1= np.array(L1)

np.where(arr1[:,7]=='10', '인사부', np.where(arr1[:,7]=='20', '총무부', '재무부'))
np.where?
#2. 1부터 25까지 5*5 배열 생성 후 짝수는 그대로 홀수는 0으로 치환 
arr2= np.arange(1,26).reshape(5,5)
np.where(arr2%2==0, arr2, 0)


#전치메서드 
arr2  #[[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
#1. T :  행열 전치 
arr2.T #[1,6,11,16,21]
#2. transpose : 축번호를 전달, 원하는 축의 이동, 축번호 전달 순서 중요 
arr2.transpose(0,1) #[ 1,  2,  3,  4,  5]  arr2.transpose(층=0, 행=1, 열=2) 혹은 (행=0, 열=1)
arr2.transpose(1,0) #[ 1,  6, 11, 16, 21]
#3. swapaxes : 2개의 축 번호를 전달, 원하는 두 축의 전치, 축번호 전달 순서 중요 하지 않음 
arr2.swapaxes(0,1) #[ 1,  6, 11, 16, 21]  (행=0, 열=1) 
arr2.swapaxes(1,0) #[ 1,  6, 11, 16, 21]

# 연습문제 
# 2*3*4 배열 생성 후 층과 행을 전치하여 출력하여라 
arr5 = np.arange(1,25).reshape(2,3,4)
arr5.swapaxes(0,1)  #3*2*4의 배열로 바뀜 
arr5.swapaxes(1,0)

arr5.transpose(1,0,2)

# 누적합, 누적곱 연산 
arr2

arr2.cumsum(axis=1) #컬럼별 누적합
arr2.cumsum(axis=0) #행별 누적합 

arr2.cumprod(axis=1) #컬럼별 누적곱
arr2.cumprod(axis=0) #행별 누적곱 

#최대, 최소 연산 
arr2.max(axis=0) #행의 최대값 
arr2.min(axis=0) #행의 최소값 

arr2.argmin(axis=0) #최소를 갖는 포지션 출력 (위치값 출력), whichmin in R
arr2.argmax(axis=0) #최대를 갖는 포지션 출력 (위치값 출력), whichmax in R 

#불리언 배열 매서드 
(arr2 > 10).sum() #조건에 만족하는 값의 개수 
(arr2 > 10).any() #조건을 만족하는 값이 하나라도 있는지 여부 
(arr2 > 10).all() #모든값이 조건을 만족하는지 여부 

#연습문제 - 다음이 구조를 갖는 array를 생성하자 

arr4 = np.array([1, 500, 5, 2, 200, 2, 3, 200, 7, 4, 50, 9]).reshape(4,3)

#선생님 
arr1= np.array(f_read_txt('a1.txt', ' '))  #텍스트 만들고 불러옴 

#1) 위의 배열에서 두번재 컬럼 값이 300이상인 행 선택 
arr4[arr4[:,1]>=300, ]
arr4[arr4[:,1]>=300, :]

#2) 세번째 컬럼 값이 최대값인 행 선택 
arr4[:,2].max(axis=0) 

#위치값을 얻고 행 출력 
arr4[arr4[:,2].argmax(), :] 


#sort : 정렬 
arr2.sort(axis=0)
arr2.sort

arr3 = np.array([[3,1,10,12],[1,2,10,9]])
arr3.sort(axis=1)
arr3
array([[1,3,10,12],[1,2,9,10]]) #배열을 순차적으로 나열 , 

# 집합연산자
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6]) 

#1. union1d : 합집합
np.union1d(arr1,arr2)

#2. intersect1d : 교집합
np.intersect1d(arr1,arr2)

#3. setdiff1d : 차집합 
np.setdiff1d(arr1,arr2)

#4. in1d : 포함연산자  #arr1이 1 또는 2를 포함하고 있는가? 
np.in1d(arr1,[1,2]) 

#5. setxor1d : 대칭차집합 => (A-B) U (B-A)
np.setxor1d(arr1, arr2)

#6.unique 
np.unique(np.array([1,1,1,2]))


# 연습문제 
# 1~25의 값을 갖는 5*5 배열을 생성 후 2의 배수와 3의 배수를 추출 
arr1 = np.arange(1,26).reshape(5,5)
arr2 =arr4[arr4 % 2 ==0, ]
arr3 =arr4[arr4 % 3 ==0, ]
np.union1d(arr4[arr4 % 2 ==0, ],arr4[arr4 % 3 ==0, ])

arr1[np.in1d(arr1, np.union1d(arr2,arr3))] #오류 arr1과 np.~ 의 배열이 같지 않아서  
arr1[np.in1d(arr1, np.union1d(arr2,arr3)).reshape(5,5)]

# 참고 : reshape시 배열 순서 
# 'C' 순서 : 행 우선순위 
# 'F' 순서 : 컬럼 우선순위

a1 = np.arange(1,10)
a1.reshape(3,3,order='c')  #C 디폴트, 행방향 먼저 채우기
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
  
a1.reshape(3,3,order='F')  # 컬럼 방향 먼저 채우기 
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])