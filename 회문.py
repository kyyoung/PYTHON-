Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
vword=input('회문판별 문자를 입력하세요 : ')
vcnt = math.trunc(len(vword) /2 )  #len: 글자수 세는 것 
for i in range(0,vcnt):
    if vword[i] == v[-(i+1)]
       continue 
   else : 
       exit (0)  
   
print('회문입니다.')
