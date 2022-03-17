# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:29:27 2020

@author: KITCOOP
"""

#리스트 
R에서 벡터처럼 여러개의 값을 하나로 묶기 위한 최소 단위 자료구조 
1차원 형식 --> R (벡터)과 공통점 
중첩구조 가능(리스트 안에 리스트 삽입이 가능) --> R과 차이점 
서로 다른 데이터 타입 입력 가능 

#1.생성 
L1=[1,2,3]
L2=[1,'2',3] ; L2  #문자와 숫자와 같이 들어가도 문자는 문자로 숫자는 숫자로 입력됨 
type(L2)
L3=[1,2,[3,4]] ; L3 #묶음안에 묶음이 유지됨 
L4=[1,2,3,4,5,6] 

#2. 색인 
L1[0] #정수(position) 색인 가능 
L1[0:2] #슬라이스 색인 가능 (연속범위 색인 가능)
L1[1:] # 1포지션부터 ~끝까지 색인 --> 2,3 출력 
L1[ : 2] # 처음부터 1 포지션까지 색인 -->1,2 출력 

L1[[0,2]] # 리스트를 전달한 색인 불가(동시에 여러개 전달 불가)
L3[2][0] # 중첩된 리스트 색인은 밖에다 한 번 더 색인 해줘야함
L1[-1] #reverse indexing '3' 이 출력됨, In R은 3제외한 나머지 1,2 출력 
L4[::2] # start:end:by   -- > 예시에서는 2스텝 넘어가면서 출력 [1,3,5]가 출력됨 
#3. 수정 
L1[0] =10   
L1[1]=[20,30] ; L1 #[10, [20, 30], 3] - 왼쪽과 오른쪽의 수정 범위가 같아야 수정이 됨  
L1[1:3]=[20,30] ; L1 #[10, 20, 30] -범위 설정 한 후 수정 

#4. 확장 
# =============================================================================
# 참고 In R 
# v1 <-c(1,2,3)
# c(v1,4)  
# append(v1, 4)
# v1[4]<- 4 #범위에 벗어나도 4라는 값 전달 가능 
# =============================================================================

In Python
L1.append(40)
L1[4]  #범위에 벗어나는 것 자체가 에러, 위치값으로 확장 전달 불가 

L1 = [1,2,3]
L2 =[4,5,6]

#확장 
L1+ L2 # 리스트 확장 
L1*3 #리스트 확장 -- L1이 세번 반복됨 [1, 2, 3, 1, 2, 3, 1, 2, 3]
L1 = L1 + [4] #리스트 원소 추가 
L1.extend([5]) ; L1 #리스트 원소 추가 

#삭제 - 위치 기반 
del(L1[0]) ; L1 #원소의 삭제 
del(L1[3]) ; L1 #중간 위치 원소 삭제 가능 cf) R에서는 불가 
del(L1) ; L1 # L1  자체를 삭제 in R : rm(list= 'L1')
L2 = [] #객체 원소 삭제 L2의 형태는 남겨놓음 



#연습문제
d1=input('지폐로 교환할 돈을 얼마?')
d_m =int(d1)
d2=input('50000원짜리 ==>')  
d_m2 = d_m//int(d2)
d3=input('10000원짜리 ==>') 
d_m3 = (d_m%int(d2))//int(d3)
d4=input('5000원짜리 ==>')  
d_m4 =  (d_m%int(d2))%int(d3)//int(d4)
d5=input('1000원짜리 ==>')  
d_m5=(d_m%int(d2))%int(d3)%int(d4)//int(d5)
d_m6=(d_m%int(d2))%int(d3)%int(d4)%int(d5)

d6=input('지폐로 바꾸지 못한 돈 ==> ')

#선생님
money = int(input('지폐로 교환할 돈을 얼마?'))
q50 = money // 50000 #몫 (%/% in R)
money = money % 50000 #나머지 (%% in R)
q10 = money // 10000 
money = money % 10000
q5 = money // 5000
money = money % 5000
q1 = money // 1000 
money = money % 1000 

print('50000원짜리 ==>%2d 장' % q50)
print('10000원짜리 ==>%2d 장' % q10)
print('5000원짜리 ==>%2d 장' % q5)
print('1000원짜리 ==>%2d 장' % q1)
print('지폐로 바꾸지 못한 돈 ==>%2d 장' % money)

# 논리 연산자
v1 = 10 
(v1 > 5) &(v1<15)
(v1 > 5) and (v1<15)
(v1 > 5) | (v1<15)
(v1 > 5) or (v1<15)
!(v1 > 5) #R에서의 부정 연산자 
not(v1 > 5) #파이썬 부정 연산자 

#lamda **** 꼭 기억 , 자주 사용함 
-사용자 정의 함수(축약형)
1) 기존 함수 선언 방식 
def 함수명 :  
2) lambda #if, for문 사용 불가, 입력된 인자를 리턴하는 것만 가능함  
lambda input : output 
예제) 입력된 값의 10% 증가값을 리턴하는 함수 생성 
f1 = lambda x : x *1.1
f1(10)

예제) 두 수를 입력받아 두 수의 합을 리턴 
f2 = lambda x, y= 0 : x+ y #인자의 기본값 선언 가능, 일부 인자만 기본값 선언하려면 뒤에다가 써 줘야함  
f2 = lambda x=0, y  : x + y #앞에 있는 인자의 기본값 선언시 뒤에 있는 y도 기본값 선언해야함 
f2(1,10) 
f2(1)

#리스트의 백터연산(적용함수)
L1 + 1 #리스트 연산 불가(반복연산 불가하기 때문) 
L1 * 1.1 #리스트 연산 불가(반복연산 불가하기 때문) 
f1(L1)  #함수에 전달해도 반복연산이 불가능하기 때문에 오류
#-----------------------------------------------------------------------------
list(map(f1, L1)) #리스트의 백터연산 방법 -----> map 사용 : 원소별 연산이 반복 적용됨 , 특성상 리스트로 담아야지만 출력이 가능
#예제 ) L1 + L11의 결과 리턴 
L11 = [1,2,3,4] 
L1 + L11 # 불가, 사칙연산이 아닌 리스트의 결합(확장)으로 리턴됨 [10, 20, 30, 40, 1, 2, 3, 4]
list(map(f2,L1,L11))  #가능 : map의 기능이 R에서 mapply와 같음 
map?
map(func, *iterables) --> map object *의 의미는 여러개 인자 전달 가능 // cf) **는 여러개 인자 전달시 key value 형태만 전달 
# =============================================================================
# [참고- in R]
# sapply(L1, f1)
# mapply(f1, L1)

# sapply(L1, f1, L2)
# mappy(f1, L1, L2)
# =============================================================================
#연습문제 
#다음의 리스트를 생성 
L1 = [1,2,3,4]
L2 = [10,20,30,40]
L3 = [100, 200, 300]
L4 = ['서울', '부산', '대전', '전주']
L5 = ['abc@naver.com', 'a123@hanmail.net']
    
    
# 1. L2의 L1승 출력, 10^1, 20^2, 30^3, 40^4 
f_1 = lambda x, y : x**y 
list(map(f_1, L2, L1))

# 2. L4의 값에 "시"를 붙여 출력
f_2 = lambda x, y : x+y
list(map(f_2, L4, '시')) 

# 3. L5에서 이메일 아이디만 출력 
f_3= lambda x : x. split('@')[0]
list(map(f_3, L5))

#선생님 
#1) 
f1 = lambda x, y : x**y 
list(map(f1,L2,L1))

#2) 
f2= lambda x : x + '시'  
list(map(f2, L4))

#3) 
f3 = lambda x : x.split('@')[0]
list(map(f3, L5))

#2차원 형식 리스트 
L1 = [[1,2,3], [4,5,6], [7,8,9]] #1차원 , L1의 객체는 3개 [] 형식 
len(L1)

L1[1][0]