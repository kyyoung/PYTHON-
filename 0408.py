# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:33:27 2020

@author: KITCOOP
"""

# -자료구조
# In R 
# v1 <- c(1,2,3,4) 
# v1[c(1,3)] #벡터색인 가능 
# v1[ v1<2] # 조건색인 가능 
# =============================================================================

# In Python
 L1 = [1,2,3,4,5]
 L1[1:4]
 L1[[1,3]] #벡터 색인(여러값을 묶어 색인값으로 전달)은 색인 안됨, list indices must be integers or slices, not list
 L1 <2 # 비교연산 불가, --> 원소별로 계산이 되지 않기 때문
 lambda x : x <2 --> lambda를 사용하여 원소별로 계산 되게 사용 mapply in R  
 list(map(lambda x: x <2, L1)) #map 함수를 사용하여 각 원소별 비교 가능 
 L1[list(map(lambada x: x <2, L1))] #조건 색인 불가, 각 원소별 연산 불가 하기 때문 

# 시리즈 In Pyhton from 판다스 
 from pandas import Series 
 s1 = Series([1,2,3,4,5])
 s1[[0,3]] #벡터 색인 가능 
 s1 <2  #조건 전달 가능 
 s1[s1<2] #조건 색인 가능 
 
# 파이썬에서 헷갈리는 것 : 똑같은 이름으로 메서드, 함수, numpy, pandas에서도 존재함 --> 해당 데이터에 맞는 메서드 혹은 함수를 불러서 쓰는 것이 관건  
 s1.mean() 
 np.mean() 
 pd.mean()
 
 import pandas
 dir(pandas) #pandas에 있는 함수 목록 
 
# =============================================================================

#리스트 주요 메서드 
L1 = [1,2,3,4,5]
L2 = [1,5,2,3,4]

L1.append(6) ; L1    #원소추가 
L1.extend([7]) ; L1  #원소추가, 리스트 확장 
L1.insert(0,10); L1  #0번째 위치에 10 삽입 

L1.remove(3) ; L1    #특정 원소 삭제, 위치기반 아님 
L1.pop() ; L1        #마지막 원소 삭제
del(L2[3]) ; L2      #위치기반 
L1.count(1)          #원소 포함 횟수 

L1.index(4)          #원소 위치
L1.index(3)          #원소 위치(값이 없으면 에러 발생)

L1.sort(reverse=False) ; L1  #정렬된 결과 추출 , 즉시 반영 

len(L1) #리스트 사이즈(원소개수)

# for문 - 들여쓰기에 주의

for i in range(0,6) : # 0:6 -> 0,1,2,3,4,5
    print(i)

for i in range(0,6,2) : # 0:6 -> 0,2,4  +2씩 된 원소만 출력 
    print(i)
    
for i in L1 : # L1원소 출력 
    print(i)
    
for i in L1 : # print의 enter처리 기능을 없애기, 일렬로 출력됨 
    print(i, end='')

#R에서와 마찬가지로 벡터를 생성해야 결과값이 담김 
    
#연습문제) jumin = ['8812111223928','8905042323343','90050612343432'] 에서 각 성별을 나타내는 숫자를 추출(for문 사용)

jumin = ['8812111223928','8905042323343','90050612343432']    


for i in jumin :
     print(i[6])        
    
# 선생님 
L2 = [] 
for i in jumin :
    L2.append(i[6])       

#연습문제) 시작값과 끝값, 증가값까지 사용자 입력 
d1=int(input('시작값을 입력하세요'))
d2=int(input('끝값을 입력하세요'))
d3=int(input('증가값을 입력하세요'))


#선생님 
vsum = 0 #vsum을 지정해줘야 덧셈이 실행됨 

for i in range (d1,d2+1,d3): #d2가 300이 아니라 299니까 +1 해야함 
    vsum = vsum + i 
    
for i in range (d1,d2+1,d3):
    print(i)

print('%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d' % (d1,d2,d3, vsum)) 

# 중첩 for 문 
L1 = [1,2,3]
L2 = [[1,2,3], [4,5,6], [7,8,9]]
 
for i in L1:
    print(i, end= ' ')
    
for i in L1:
    print(i) 

for i in L2:
    print(i)    
    
for i in L2:
    print(i, end= ' ')

#L2의 리스트안에 리스트가 벗겨짐 
for i in L2:
    for j in i:  #리스트안에 리스트가 벗겨지기 위해 중첩 
        print(j, end= ' ')  #1  2  3  4  5  6  7  8  9 이런 형식으로 출력됨  
    print() #중첩 for문과 상관없는 print, 첫째 for문 i의 출력 

#위치기반 중첩 for 문 
for i in range(0,3): #첫번째 리스트 묶음 
    for j in range(0,3): #중첩 리스트 
        print(L2[i][j], end= ' ')
    print()
        
L2[0] #[1,2,3]
L2[0][1] #2 출력

for i in range(0,3):
    print(L2[0][i], end= ' ') #1,2,3

#연습문제-불규칙한 리스트의 2차원 형식 출력  
L3 = [[1,2], [1,2,3], [4,5,6]]
for i in L3:
    for j in i:
        print(j, end= ' ')
    print()

#위치기반 
for i in range(0,len(L3)):
    for j in range(0, len(L3[i])):    
        print(L3[i][j], end=' ')
    print()

#내부 리스트의 len 설정     
len(L3[0])

# while 문 
i=0 
while i < 11 :
    print(i)
    i = i + 1
#i가 11미만인 것 까지 출력 됨 
    
print('\u2605')  #별모양 출력 유니코드 , 2바이트 차지 , 앞에 공백이 몇바이트 차지하는지 생각해야함 
print('\u2605'*3) #문자열*n은 문자열이 n번 반복, 현재는 *3을 했으니 문자열이 3번 반복됨

# if 문 
L1 = [1,2,3,4,5]

for i in L1:
    if i >3:
        print(i)

#연습문제 : 1부터 100까지의 합 출력, 짝수만 

vsum = 0 
for i in range(0,101):
    if i%2 ==0:
        vsum = vsum + i 
print(vsum) 

#선생님-while사용 
vsum = 0 ; i=1 # i선언 
while i < 101:
    if i % 2 == 0 :
        vsum = vsum + i 
    i = i + 1
print(vsum)

#while-continue 사용 
vsum = 0 ; i=0 # i선언 
while i < 101:
    i = i + 1
    if i % 2 != 0 :
         continue  #R에서 next 구문 
    vsum = vsum + i 
print(vsum)

vsum = 0 ; i=0
while i < 101:
    i = i + 1
    if i % 2 != 0:
        continue
    vsum = vsum + i 


#반복제어문 : break, continue 