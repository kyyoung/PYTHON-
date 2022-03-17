# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:13:34 2020

@author: KITCOOP
"""
run profile1
#stack, unstack 
- long <-> wide 형태의 변화
- multi index 컬럼화, 컬럼의 multi index 화

s1 = Series([1,2,3,4], index=[['A','A','B','B'],['a','b','a','b']])

#멀티인덱스주의 ***

s1.unstack() #index의 하위 레벨의 컬럼화 
s1.unstack(level=0) #index의 특정 레벨의 컬럼화  level=0  상위레벨 

s2= s1.unstack(level=0)
s2.stack() #column의 index화
s2.stack(level=0) #특정 레벨의 column의 index화

s2.loc['b', 'B'] = NA
s2.stack() #stack  처리시 NA는 생략 
s2.stack(dropna =False) #dropna=False 옵션, NA 생략불가 

# [ 연습 문제 ]
#sales2.csv 파일을 읽고
df1 = pd.read_csv('sales2.csv', engine = 'python') 
sales = pd.read_csv('sales2.csv', engine = 'python') 
# 1) 다음과 같은 형태로 만들어라
#                 냉장고          tv             세탁기         에어컨
#                 출고 판매 반품  출고 판매 반품  출고 판매 반품  출고 판매 반품
# 2018-01-01  c1  
df1 = df1.set_index(['날짜', '지점', '품목'])
df2 = df1.unstack()
df2 = df2.sort_index(axis=1, level=[1,0],ascending=[True,False]).swaplevel(0,1, axis=1)

#선생님 
sales=sales.set_index(['날짜', '지점', '품목'])
sales.unstack().sort_index(axis=1, level=1).swaplevel(0,1,axis=1)

sales2= sales.stack().unstack(level=[2,3]) #stack 처리해서 모두 다 인덱스로 만든 후 필요한 항목을 컬럼화하기 

sales.stack().index #날짜. 지점, 품목, 컬럼(출고, 판매, 반품)까지 인덱싱 
sales.index #날짜, 지점, 품목이 인덱싱 

# 2) 위의 데이터 프레임에서 아래와 같은 현황표로 출력(총합)
# 출고  ---
# 판매  ---
# 반품  ---
df3 = df2.stack()

#선생님 
sales2.sum(axis=1, level=1).sum() #하위컬럼을 기준으로 sum 하고 컬럼별로 sum 

# 3) 날짜별 품목별 출고량의 총합을 아래와 같이 출력
#                     냉장고   TV    세탁기      에어컨
# 2018-01-01

df3.xs('출고', axis=0, level=2).unstack()
df4 = df1['출고'].unstack(level=0).unstack().sum(0)
df4.unstack()

#선생님 
sales2.sum(axis=0, level=0).sum(axis=1, level=0)
sales.sum(axis=0, level=[0,2]).sum(1).unstack()
# 4) 지점별 각 판매 현황을(총 합) 아래와 같이 출력
#         출고  판매   반품  
# c1
# c2
# c3

df1.unstack().sum(1)
df2.unstack()

#선생님 
sales2.sum(axis=0, level=1).sum(axis=1, level=1)
sales.sum(level=[0,1], axis=0).sum(axis=0)


#참고 -  multi index에서의 산술연산 시 동시 여러 level 전달 가능 
sales.sum(level=[0,1], axis=0)



#[ 연습문제]
#movie_ex1.csv 파일을 읽고 
movie = pd.read_csv('movie_ex1.csv', engine='python')
#1) 지역 시도별 성별 이용비율의 평균을 정리한 교차테이블 생성 
movie1 = movie.iloc[:,[3,6,8]]
movie1 = movie1.set_index(['지역-시도', '성별'])
movie1 = movie1.sort_index(axis=0, level=[1,0])
movie1.sum(level=[0,1], axis=0).unstack()

movie.unstack()

len(movie1.index) 

#선생님
movie2 = movie.set_index(['지역-시도', '성별'])['이용_비율(%)']
movie2.unstack() #남여 정렬이 안되어있어 값을 묶을 수 없음 
movie2.sum(level=[0,1]).unstack() #남여레벨을 정렬한 후 unstack!

#2) 일별 연령대별 이용비율의 평균을 정리한 교차테이블 생성
movie2 = movie.iloc[:,[2,7,8]]
movie2 = movie2.set_index(['일', '연령대'])
movie2 = movie2.sort_index(axis=0, level=[1,0])
movie2.sum(level=[0,1], axis=0).unstack()

#선생님 
movie3 = movie.set_index(['일', '연령대'])['이용_비율(%)']
movie3.unstack()  #연령대의 정렬이 믹스되어 있어 값이 레벨별로 묶일수 없음
movie3.sum(level=[0,1]).unstack()

# python - 오라클 연동 
f_sql('select * from emp', ip='192.168.0.115', port='1523', id='scott', passwd='oracle', sid='orcl')

#1.module 설치(os에서 설치해야함)
#cx_Oracle : 파이썬과 오라클을 연결시켜주는 외부 패키지 
cmd창을 켜서 명령어 입력 pip cx_Oracle 설치함 
C:\Users\KITCOOP>pip install cx_Oracle

#2. module 호출
import cx_Oracle

#3. connection 생성 
#cx_Oracle.connet("id/passwd@ip:port/sid")
#cx_Oracle.connect("scott/oracle@192.168.0.115:1521/testdb")
con1 = cx_Oracle.connect("scott/oracle@localhost:1523/orcl")

#[참고 - oracle sid 및 서비스 포트 확인 방법] 
cmd 창에서 
C:\Users\KITCOOP > lsnrctl status  입력 후 확인 

#[참고 - orcle 연동시 한글 깨짐 현상]
import os 
os.putenv('LNS_LANG', 'KOREAN_KOREA.KO16MSWIN949')  #커넥션 맺기 전에 해야함
#4. sql 실행 
pd.read_sql('select * from emp', con = con1) 
pd.read_sql('select * from student', con = con1) 

#연습 
import cx_Oracle
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16MSWIN949')  #커넥션 맺기 전에 해야함
con1 = cx_Oracle.connect("scott/oracle@localhost:1523/orcl")
pd.read_sql('select * from student', con = con1) 




#연습문제 : 다음의 함수를 생성 
f_sql('select * from emp', ip ='192.168.0.115', 
      port='1521', id='scott', passwd='oracle', sid='orcl')

