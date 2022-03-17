# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:23:19 2020

@author: KITCOOP
"""

#데이터 언어 
part1 :
    2 : numpy + pandas 

#전역변수(global, in R : v1 <<-1) 
def f1(x) : 
    v1 = 1
    print(v1)

def f2( ) : 
    print(v1)

v1=10 
f1(v1) # 1리턴(함수 내부 선언값이 더 우선순위)
f2( ) #10리턴(v1이 전역변수 선언되어 있으므로)

#-- 
def f1() :
    v2 = 1
    print(v2)
    
def f2() :
    print(v2)

f1() #1
f2() #name 'v2' is not defined

#-- 
def f1() :
    global v2   #전역변수 선언
    v2 = 1
    print(v2)

def f2() :
    print(v2)
    
f1() #1
f2() #1

#매개변수 전달방식 
# 1) * : 가변형 인자 전달 방식, 내부 반복문 필요 
def f1(*para) :
    for i in para :
        print(i)
f1(1,2,3,4) #1,2,3,4 출력 
f1(1*2)
f1(2*2)
# 예제) 함수에 입력된 모든값의 곱을 출력하는 함수 생성 

def f2(*para) :
    for i in para :
        for j in para :
              print(i*j)
f2(2,3)

#선생님
def f2(*para):
    vprod=1 
    for i in para:
        vprod = vprod*i 
    return vprod 
f2(2,3,5)

#2) ** : key-value 인자 전달 방식, 내부 반복문 필요 
d1 = {'a':1, 'b':2, 'c':3} 
d1.get('a')
d1['a']
d1.keys()

def f3 (**para) :
    for i in para.keys():
        print('%s의 값은 %s입니다.' % (i, para[i]))
f3(a=1, b=2, c=3)

#3) zip : 동시에 변수를 묶어서 전달 시 필요 
fsum(v1,v2)

def fsum(v1,v2):
    result=[]
    for i, j in zip(v1,v2):
        result.append(i+j)
    return result
fsum([1,2,3],[10,20,30])


#모듈의 생성 
# -모듈 : 함수의 묶음 
# 정의된 여러개의 함수를 하나의 파이썬파이(.py)에 저장하면 하나의 모듈이 생성됨 

# [연습문제]
# 두 수를 전달받아 두 수의 곱을 구하여 리스트에 저장, 저장된 값은 숫자가 큰 순서대로 정렬하여 출력하도록 하는 사용자 정의함수 생성. 
# 단, 사용자 정의함수에 두 수 이외의 reverse라는 키워드 인자를 입력 받도록 하자 
fprod(L1, L2, reverse=True)

L1=[]
L2=[]
def fprod(L1, L2, reverse= True):
    result = []
    for i, j in zip(L1,L2):
        result.append(i*j)
    return result

fprod([3], [2])

#선생님 
def fprod(x, y, **para):
    result = []
    for i, j in zip (x,y):
        result.append(i*j)
    result.sort(reverse=para['reverse'])
    return result

fprod(L1,L2, reverse=True)
    
#외부파일 불러오기 
1.open : 파일을 열어서 메모리상으로 불러오는 작업(cursor 선언) 
2.fetch : 선언된 cursor(임시 메모리 공간)에 저장된 data를 한 건씩 불러오기 
3.close : 객체 선언 완료 후 cursor에 할당된 메모리 영역 close 
          cursor를 닫지 않으면 메모리 누수 현상이 발생할 수 있으므로 주의 
          
c1 = open('read_text1.txt') #커서 선언 , txt 파일 디폴트 디렉토리에 저장 
v1=c1.readline() #fetch
print(v1)
v2=c1.readline() #fetch
print(v2)
c1.close() #close

#-- 반복문으로 열기 

c1 = open('read_text1.txt')
while 1 : 
    v1 = c1.readline()
    if v1 == '' :
        break 
    print(v1)   #1234와 5678 사이에 한줄이 삽입됨 메모장에 엔터로 내려써서 그럼,, 이미 디폴트값이 한 칸 내려쓰는거인데 엔터로 내려써서..
c1.close()


#--
c1 = open('read_text1.txt')
while 1 : 
    v1 = c1.readline()
    if v1 == '' :
        break 
    print(v1)   
c1.close()

#--저장
c1 = open('read_text1.txt')
outlist=[]
while 1 : 
    v1 = c1.readline()
    if v1 == '' :
        break 
    outlist.append(v1)
c1.close()

outlist

#--readlines() 
c1 = open('read_text1.txt')
v1 = c1.readlines()

#실습과제: 아래와 같은 함수 생성 (리스트 안에 리스트 삽입하고 형식 변경 ~) 
 f_read_txt(file, sep = ';', fmt = 'int')
 [[1,2,3,4],[5,6,7,8]]  
 f_read_txt(file, sep = ';', fmt = 'str')
 [['1','2','3','4'],['5','6','7','8']]  
 
 
#