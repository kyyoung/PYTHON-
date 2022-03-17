# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:12:44 2020

@author: KITCOOP
"""

#중첩 for문을 사용한 리스트의 입출력 
L1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0, len(L1)) :
    for j in range(0, len(L1[i])) :
        print(L1[i][j], end= ' ')
    print()
    
#입력 
z=1 
for i in range(0,3) : 
    for j in range(0,3) : 
        print(z, end= ' ')
        z = z + 1
    print() 
    
outlist=[]
z=1 
for i in range(0,3) : 
    inlist=[]
    for j in range(0,3) : 
        inlist.append(z)
        z = z + 1
    outlist.append(inlist)
 
outlist 

#2차원리스트 

outlist=[]
z=0
for i in range(0,4) : 
    inlist=[]
    for j in range(0,5) : 
        inlist.append(z)
        z = 3+z
    outlist.append(inlist)
 
outlist 


outlist=[]
z=0
for i in range(0,5) : 
    inlist=[]
    for j in range(0,5) : 
        inlist.append(z)
        z = 3+z
    outlist.append(inlist)
outlist 

list1=[]
list2=[]
value=1
for i in range(0,4) :
    for j in range(0,3) :
        list1.append(value)
        value +=1
    list2.append(list1)
    list1=[] #inlist의 초기화 초기화 안하면 [1,2,3,4,5,6] 이런식으로 한 리스트 안에 넣어짐 
list2

##튜플 
# -리스트와 동일한 자료구조(1차원, 서로다른 데이터 타입 허용)
# -수정불가(읽기전용)
# -수정되면 안되는 참조용 생성시 필요 

#1. 생성
t1 = (1,2,3) ; t1
t2 = 1,2,3 ; t2
t3 = (10,) ; t3  
t4 = (10) ; t4 

type(t3) #tuple
type(t4) #int

#참고 
a1, a2, a3 = 1,2,3 #각 변수에 1,2,3 각각 삽입 

#2. 수정
t1[0] =10 #'tuple' object does not support item assignment
t1.append(11) #'tuple' object ahs no attirbute 'append' 
del(t1[0]) #t1에 있는 원소 삭제 불가 
del(t1)  #object 삭제자체는 가능

#딕셔너리 
-R에서의 리스트와 비슷 (key value 형식)
-key-value형식 (빠르고 쉽게 저장하기 위한 형식)
-4차원으로 확장하면 Series, Dataframe 구조 

#1. 생성 
d1 = {'a':1, 'b':2}
type(d1)
d1
d2={'a':[1,2], 'b':{2,3}}
#2. 색인 (key색인 가능)
d1['a']
d1.get('a') #get 메소드 

#3.수정 
d1['b'] =22
d1['c'] =3
del(d1['c'])

#4. 키출력 
set(d1)

from numpy import nan as NA #파이썬에서 nan이 R에서 NA와 같음 nan을 alias로 이름 NA로 바꿈 
d1['b'] = NA


[참고-dict와 Series, Dataframe의 관계]
-Dataframe  
-dataframe 안에 들어가는 내용을 dictionary 형태로 만들어주고 dataframe으로 묶어야함   
-안그러면 key value가 설정이 안됨 

-Series 
-keyvalue 설정하지 않으면 0,1,2 ... 자동생성 

from pandas import Series
from pandas import DataFrame
Series(d1)
DataFrame(d2)

Series([1,2,3])
DataFrame({'a':[1,2,3], 'b':[4,5,6]})

#연습문제)다음의 리스트와 딕셔너리를 참고하여 전화번호를 완성 : 02)345-4958 
l1=['345-4958', '334-0948', '394-9050', '473-3853']
l2=['서울', '경기', '부산', '제주']
area_no={'서울' : "02", '경기':"031", '부산' : "051", '제주': "064"}
area_no['서울']

area_no[l2[0]] + ')' +l1[0]
area_no[l2[1]] + ')' +l1[1]

tellist1=[]
tellist2=[]
for i in range(0,4):
    tellist1= area_no[l2[i]]+')'+l1[i]
    tellist2.append(tellist1)
tellist2

#선생님 
area_no.get(l2[0]) + ')' + l1[0]
f1 = lambda x, y : area_no.get(y) + ')' + x 
list(map(f1,l1,l2))

#연습문제 
d1 = {'a':['치킨', '라면'], 'b':['치킨무', '김치']}
d1['a'][0]
d1['b'][1]

v1=input("['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']중 좋아하는 음식은?")

for i in range (0,2):
    if d1['a'][i]==v1:
        print(d1['a'][i]+ '의 궁합 음식은'+ d1['b'][i] + '입니다.' )
    else:
         print('그런 음식이 없습니다. 확인해 보세요.')    
         
#선생님 
   d1 = {'치킨':'치킨무', '라면': '김치', '떡볶이':'어묵', '짜장면':'단무지', '피자':'콜라'}
   flist=list(set(d1))
   str(flist) + '중 좋아하는 음식은?'
'치킨' in flist
while 1 :
    ans = input(str(flist) + '중 좋아하는 음식은?')
    if ans in flist :
        print('<%s> 궁합 음식은 <%s>입니다.' % (ans, d1.get(ans)))
    elif ans == '끝' :
        print('프로그램 종료')
        break 
    else : 
        print('그런 음식이 없습니다. 확인해보세요')
    
         
