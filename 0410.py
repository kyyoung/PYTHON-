# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:17:42 2020

@author: KITCOOP
"""

#로또 생성 프로그램 
import random 
random.randrange(1,45)

v1=[1,2,3,4,5,6,7]
len(v1) ==7

outlist=[]
inlist=[]
for i in range(1,46):
    inlist=random.randrange(i)
    outlist.append(inlist)    
    if len(outlist)==7:
        break 
#선생님 
print('로또 번호 추첨기')
lotto = [] 
while len(lotto) < 6:
    v1 = random.randrange(1,46)
    if v1 in lotto :
        pass
    else :
        lotto.append(v1)
lotto.sort() 
print('추첨된 로또 번호 === > ' , end= ' ')   #end는 밑의 로또번호 출력을 연속해서 출력할 수 있게 도와줌  

#로또 번호 출력 
for vno in lotto : 
    print(vno, end= ' ')         


#리스트 내포 표현식 
-리스트가 벡터 연산이 안되는 점을 비교적 간단한 문법으로 가능하게 함 
-리스트 내부에 반복문/조건문의 축약형 형태 전달 가능 

#리스트 내포 표현식 문법 1
[리턴값(연산, 함수) for 반복변수 in 대상 ] 
#조건을 포함한 리스트 내포 표현식 문법 
[리턴값 for 반복변수 in 대상 if 조건] #else 생략 가능
#else 선언 문법  
[참리턴값 if 조건 else 거짓리턴값 for 반복변수 in 대상] 

#예제) 아래 리스트에 10% 인상된 값 리턴 
L1=[1,2,3,4,5]

#1) for문 
L2=[]
for i in L1 : 
    L2.append(i*1.1)
L2

#2) map
list(map(lambda x :x*1.1, L1))

#3)리스트 내포 표현식 **딥러닝 자주 사용 
[i * 1.1 for i in L1]  #[리턴값(연산, 함수) for 반복변수 in 대상] 


#예제-조건포함) 아래 리스트에서 3보다 작은 값만 출력 
L1=[1,2,3,4,5]

#1) for 문 
L2=[]
for i in L1 : 
    if i <3 :
        L2.append(i)
L2

#2) map -lambda 축약형 
f1 = lambda x : x  if x > 3 else None 
#lambda에서 조건문이 들어가면 return되는 값을 먼저 써주고 조건을 써줘야함, 그리고 else는 생략불가

list(map(f1,L1))
 
#3) 
[i for i in L1 if i<3 ]
[i for i in L1 if i<3 else i*2]  #else 뒤에 생략 

#예제3) 아래 리스트에서 3보다 작으면 'a' 크거나 같으면 'b' 리턴 
['a' for i in L1 if i <3 else 'b'] #불가 
['a' if i <3 else 'b' for i in L1] #가능 [if 리턴값 if문 else  else리턴값  for 반복변수 in 대상] 


#[연습문제]

sal = ['9,900', '25,000', '13,000']
addr = ['a;b;c', 'aa;bb;cc', 'aaa;bbb;ccc']
comm = [1000,1600, 2000]

#1) sal의 10% 인상값 출력 

#--
f1= lambda x : round(int(x.replace(',','')))*1.1
list(map(f1,sal))

#--
sal_n=[]
for i in sal:
    sal_n.append(round(int(i.replace(',',''))*1.1))
sal_n  

#--
[round(int(i.replace(',',''))*1.1) for i in sal]

#2) addr에서 각 두번째 값(b, bb, bbb) 출력 

#--
f2 = lambda x :x.split(';')[1] 
list(map(f2,addr))

#--
addr_n=[]
for i in addr:
    addr_n.append(i.split(';')[1])

#--
[i.split(';')[1] for i in addr]

#참고 - map에 인자 전달 방식
f1 = lambda x,y : x.split(';')[y]
list(map(f1,addr,1))  #오류, 'int' object is not iterable , addr안에 있는 원소의 개수(원소의 개수는 3개)와 1의 반복횟수가 동일하지 않아서 오류남 
list(map(f1,addr,[1,1,1])) #addr과 반복회수 맞춰서 전달하면 숫자 전달 가능 

#3) comm이 1500보다 큰 경우 'A' 아니면 'B' 출력 

#--
f3= lambda x: 'A'  if x>1500 else 'B'
list(map(f3,comm))

#--
for i in comm:
    if i > 1500 :
        print ('A')
    else:
        print('B')
#--        
['A' if i >1500 else 'B' for i in comm]

#deep copy --메모리 분리하고 데이터 백업 하는 법  
L1=[1,2,3]
L3=L1[:]  #deep copy(메모리 분리, 완벽하게 다른 객체)

L1[0]=10 
L1
L3

#cf)얕은 복사 --메모리 공유, 저장되는 공간은 같고 이름만 다른 것임. alias의 개념 : L1과 L2가 이름만 다른것이고 데이터는 같음, 메모리 절약하기 위해 이렇게 만듦  
L1=[1,2,3]
L2=L1 

L1[0]=10  #L1만 수정했는데 L2도 같이 수정되어 있음, 메모리를 정확하게 공유하고 있기 때문 
L2 
L1


#참고 : 객체의 메모리 주소 확인 
id(L1) #2370196691144
id(L2) #2370196691144 
id(L3) #2370196381960

L1-L2 메모리가 같음, L3는 메모리가 다름 





