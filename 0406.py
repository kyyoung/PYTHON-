# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:14:29 2020

@author: KITCOOP
"""

#데이터 분석에 필요한 모듈(패키지)활용 
import numpy #array 
import pandas #DataFrame 

#print 함수 
print(1)
print('%d' %1)   #정수 형식 출력 
print('%2f' %10) #실수 형식 출력 
print('%s' %'abcde') #문자열 형식 출력 

print('%d + %d = %d' % (1,1,2))
print('%d 더하기 %d는 %d 입니다.' % (1,1,2))

#5,6,12, 13 --> 05, 06, 12, 13 
to_char(대상, '09')  #오라클
sprintf(대상, '%02d') #R 
print('%02d' % 1) #출력값: 01, 파이썬 -- 문자형식인 숫자 

print('%5.2f' %10) # 앞의 5는 총 자리수 '10.00'
print('%7.2f' %10) # '  10.00' 자리수가 남기 때문에 공백이 생김 
print('%.2f' %10) # '10.00'

#escape 문자 
print('\') #출력에러 
print('\\') # '\'를 일반기호화 하기 위해 '\' 사용 
print('a\nb')

# .format 매서드 
print("{0:d} {1:5d} {2:05d}".format(123, 123,123))
    # 첫번째 위치부터 123 값 전달, 전달, 두번째 위치부터 123 값 전달, 세번째위치부터 123값 전달 빈칸은 0으로 채워라 

print("{0:d} {1:.2f} {2:s}".format(10, 100,1000))
#형식 에러 s 는 문자 형식 1000은 숫자 형식 

#형식을 맞춰줘야함 - 순서는 상관 없음 
print("{0:d} {1:.2f} {2:s}".format(10, 100,'1000'))
print("{0:d} {0:.2f} {1:s}".format(10, '100',1000))

#cf) 위의 .format 매서드 함수 사용 
print("%d %5d %05d" % (123,123,123))

#색인 
v1 = 'abcdef' 
v1[0] #시작위치가 0이기 때문에 출력값이 a, 문자열 색인 가능(R에서는 불가, R에서 색인은 벡터부터)
v1[1] #출력값 b 
v1[2] 
v1[1:2] #위치가 1~1까지 추출 b만출력  
v1[1:3] #위치가 1~2까지 추출 bc 출력 

# 산술연산 함수 
round(1.23)
round(1.23, 1)

import math
dir(math) #리스트 출력 
math.trunc(1.23)

5**2 # 제곱연산자(**)
math.pow(5,2) #제곱연산 함수 

# 문자열 사용 
v1 ='select ename 
       from emp'
v1= '''select ename 
       from emp '''
#엔터를 누르면 '''로 묶어서 전달 

'a' + 'b' # 'a' || 'b' 
          # paste( 'a', 'b', sep='')
          # stringr :: str_c('a', 'b')

s = 'Good Morning' 
s[0:4] 
s[0:1]

'a' in 'abcde' #문자열 포함 여부 : True
'abcde' in 'a' # False , in 뒤에 있는 것이 더 커야함 

##메서드 
#1)startswith , R에서는 str_detect로 문자열 찾음 
a1.startswith(prefix, #시작값 확인 문자열
              start,  # 검사 시작 위치(생략가능)
              end)    # 검사 시작 끝 위치 (생략가능)
a1= 'abcde'
a2= ' abc ' 
a3= 'a;b;c'
 
a1.startswith('a')
a1.startswith('a', 1)

#2)endswith 
a1.endswith(suffix,  #끝값 확인 문자열 
            start,   #검사 시작 위치(생략가능)
            end)     #검사 끝 위치(생략가능)

 a1.endswith('e')
 a1.endswith('e', 1,3) #a1[1:3]이 'e'로 끝나는지 여부
 a1.endswith('c',1,3)  #a1[1:3]이 'c'로 끝나는지 여부

#3) 공백 제거 함수   
 a2.lstrip() #a2의 왼쪽 공백제거- R에서는 ltrim
 a1.lstrip('a')  #a1의 왼쪽의 a 제거 
 a2.rstrip() #a2의 오른쪽 공백 제거 -R에서는 rtrim 
 a2.strip() #a2의 양쪽에서 공백 제거 -R에서 str_remove_all 로 지우기? 
 
#4) replace 
 a1.replace('a', 'A') # a1에서 'a'를 'A'로 변경 R에서 str_replace 
 a1.replace('a', '') # a1에서 'a'를 삭제 
 
#5) split 
 a3. split(';') #a3을 ';'로 분리
 a3. split(';')[1]
 
#cf) 파이썬에서 리스트는 R에서의 벡터처럼 묶기 위한 용도 R에서의 리스트는 층을 분리 

#6) 대소치환 
a1.upper() #대문자
a1.lower() #소문자
a1.title() #camel 표기법 -앞에만 대문자  

#7) find -R에서 str_locate  
a1.find('a') #'a'의 위치
a1.find('A') #'A'의 위치, 없으면 -1 리턴

#8) count
a1.count('a') #a1에 'a'의 포함횟수 리턴 

#9) format 
'{0:d}+{1:d} = {2:.2f}'.format(1,2,3) 

#연습문제 
ename = 'smith' 
tel ='02)345-7839' 
jumin = '901223-2223928' 
vid = 'abc1234!' 

#1)ename의 두번째 글자가 m으로 시작하는 지 여부 
ename.startswith('m',1)

#2) tel에서 국번(345) 출력 
tel.replace('-', ')').split(')')[1]

#3) jumin에서 여자인지 여부 출력 
jumin.split('-')[1].startswith('2',0)

#4) id에서 '!'가 포함되어 있는지 여부 출력
vid.find('!') 

#선생님 
#1) 
ename[1] == 'm'
ename.startswith('m',1)
#2) 
v1=tel.find(')')
v2=tel.find('-')
tel[v1+1 : v2]
tel.split(')')[1].split('-')[0]
#3) 
jumin[7]=='2'
jumin.startswith('2', 7)

#4) 
'!' in vid
vid.find('!') !='-1'

L1=['abc', 'bcd', 'cds']
L1.startswith('a') # 리스트에서 쓸 수 없음


#input : 사용자가 입력한 값 가져오기(readline in R) 숫자를 넣어도 문자형으로 전달 
a1 = input() #cmd창에 a1 값 입력하면 a1값 출력 
a1 

a1 =input('값을 입력하세요 : ')

#형 변환 함수 
1+'1' # 형 불일치 연산 불가 
1+int('1') #정수형으로 바꾼 후 연산 가능 
1+float('1') #숫자형으로 변환 후 연산 가능 

str(1)  #문자형이기 때문에 날짜형으로 변환 불가 

# 연습문제 
# 사용자로부터 두 수를 전달 받아 다음과 같은 형식으로 출력 
"4+10 = 14입니다." 

a1=int(input())
a2=int(input())

'{0:d}+{1:d} = {2:.2f} 입니다'.format(a1,a2,a1+a2) 


#선생님 
v1= int(input('첫번째 수를 입력하세요 : '))
v2= int(input('두번째 수를 입력하세요 : '))

print('%d + %d = %d입니다.' % (v1, v2, v1+v2))

#참고 
#주석처리 단촉키 ctrl + 1, ctrl + 4
# #주석해제 단축키 ctrl + 5
