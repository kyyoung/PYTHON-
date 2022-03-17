# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:10:41 2020

@author: KITCOOP
"""

1. 문자열, 찾을 문자열, 바꿀 문자열을 입력 받아 변경한 결과를 아래와 같이 출력
변경전 :
변경후 :

v1 =input('문자열을 입력하세요 : ') #abcde 입력 
vold =input('찾을 문자열을 입력하세요 : ')
vnew =input('바꿀 문자열을 입력하세요 : ')
 
v2=v1.replace(vold, vnew)   
print('전 : %s' % v1)
print('후 : %s' % v2)

2. 이메일 주소를 입력받고 다음과 같이 출력
아이디 : a1234
메일엔진 : naver

a1 =input('id를 입력하세요 : ')
a2 =input('메일엔진을 입력하세요 : ')
print('%s@%s' % (a1,a2) )

#선생님 
v1=input('이메일주소를 입력하세요') #'abc1234@naver.com'
vid=v1.split('@')[0]
vaddr = v1.split('@')[1].split('.')[0]


3. 2번을 활용하여 다음과 같은 홈페이지 주소 출력
http://kic.com/a1234

a3=input('홈페이지 엔진을 입력하세요 : ')
print('%s%s' % (a3, a1))
print('http://kic.com/%s' %(a1))

#선생님 
'http://kic.com/' + vid 


4. num1='12,000' 의 값을 생성 후, 33으로 나눈 값을 소숫점 둘째짜리까지 표현
num1 = '12,000'

num1 = int(num1.replace(',' , ''))
round(num1/33,2)

#선생님 
num1='12,000' 
round(int(num1.replace(',',''))/33 ,2)


