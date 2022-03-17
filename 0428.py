# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:19:16 2020

@author: KITCOOP
"""
run profile1 
s1 = Series([10,2,5,1,6])
s2 = Series([10,2,5,1,1,6])

#rank : 큰 순서대로, 작은 순서대로 순위 부여 
s1.rank (axis, method = {'average',  #동순위에 대한 평균값 출력(서로 같은 순위 부여) 
                         'min',      #동순위 중 작은 값 출력(서로 같은 순위 부여)
                         'max',      #동순위 중 가장 큰 값 출력(서로 같은 순위 부여)
                         'first'},   #동순위 중 가장 먼저 배치된 값에 높은 순위(서로 다른)
                       ascending = True) #정렬 순서

s1.rank()  
s2.rank()               #4,5번째 관측치가 1,2순위이므로 그것의 평균 1.5리턴, average가 디폴트
s2.rank(method='min')   #4,5번째 관측치가 1,2순위이므로 그 중 작은 1 리턴, 가장 많이 씀 
s2.rank(method='max')   #4,5번째 관측치가 1,2순위이므로 그 중 큰 2 리턴
s2.rank(method='first') #4,5번째 관측치가 1,2순위이므로 순서대로 1,2 각각 리턴 
s2.rank(method='first', ascending= True)

#in R 
rank(x, na.last = TRUE, ties.method = c('average', 'first', 'last', 'random', 'max', 'min'))

df1 = DataFrame({'col1' : [4,1,3,5], 'col2' :[1,2,3,4]})
df1.rank(axis=0) #col1, col2끼리 비교 
df1.rank(axis=1) #col1과 col2 서로 비교 

# =============================================================================
# #cross-table 
# - 행별, 열별 연산 용이 
# - join 불가 
# - group by 연산 불가 
# - 파이썬 시각화 시 주로 사용
# - multi index를 갖는 구조를 unstack 처리하여 얻거나 pivot을 통해 얻을 수 있음 
# =============================================================================

# 1. pivot 
- 각 컬럼의 값을 교차테이블 구성요소로 전달, 교차테이블 완성 
- index, columns, values 컬럼을 각각 전달 
- 요약 기능 없음 

# 2. pivot_table
- pivot 기능과 유사, 더 많은 옵션 사용 가능 
- index, columns, values 컬럼을 각각 전달 
- aggfunc 옵션 사용하여 요약 기능 전달 가능(기본은 평균)
- fill_value 옵션 사용하여 NA 값 대체 가능 

#예제 : 아래 데이터프레임을 각각 교차 테이블 형태로 정리 
df1 = pd.read_csv('dcast_ex1.csv', engine = 'python')
df2 = pd.read_csv('dcast_ex2.csv', engine = 'python')
df3 = pd.read_csv('dcast_ex3.csv', engine = 'python')

#예시1) 품목별 price, qty 정보를 정리한 교차표 
df1.pivot('name', 'info', 'value') 
df1.pivot('name', 'info') #values 생략시 언급된 컬럼 외 모든 컬럼이 values에 들어가게 됨, 멀티인덱스가 가능하기 때문에 value 컬럼이 여러개일수 있음 

#예시2)- 년도별 음료의 판매현황 정리표 
df2.pivot('year', 'name', 'qty')
df2.pivot('name', 'year', 'qty')
df2.pivot('year', 'name', ['qty', 'price']) #values에 리스트형태로 컬럼 전달 가능 

#예시3) 년도별 음료의 판매현황(수량)의 정리 
df3.pivot('년도', '이름', '수량') #중복값 에러 발생 
df3.pivot_table(index='년도', columns='이름', values='수량') #평균값이 디폴트 
df3.pivot_table(index='년도', 
                columns='이름', 
                values='수량', 
                aggfunc = 'sum', # aggfunc 전달하여 합으로
                fill_value=0)   # fill_value : NA 치환 옵션 
#연습문제 
#movie_ex1.csv 데이터로부터 연령대별 성별 이용비율의 평균을 교차테이블 형식으로 출력 
df1 = pd.read_csv("movie_ex1.csv", encoding='cp949')
df2 = df1.loc[:,('연령대', '성별', '이용_비율(%)')]
df2.pivot_table(index='연령대', columns='성별', values='이용_비율(%)')
df2.pivot_table(index='연령대', columns='성별', values='이용_비율(%)', aggfunc='sum')

#선생님 
movie= pd.read_csv('movie_ex1.csv', engine = 'python')
movie.pivot_table(index='성별', columns='연령대', values='이용_비율(%)', aggfunc='sum')
df2.pivot_table(index='연령대', columns='성별', values='이용_비율(%)', aggfunc='count')
df2.pivot_table(index='연령대', columns='성별', values='이용_비율(%)', aggfunc=len) #count와 비슷

#연습문제
#delivery.csv 파일을 읽고 
df1 = pd.read_csv("delivery.csv", encoding='cp949')
#1) 각 업종별 통화건수가 많은 순서대로 시군구의 순위를 출력 
df1 = df1.set_index(['시군구',  '업종'])
df1.drop(['일자', '시간대', '시도', '읍면동'],  axis='columns').sum(level=[0,1], axis=0).unstack(level=1).rank(method='min', ascending = False)

#선생님 
df1.set_index(['업종', '시군구'])['통화건수'].unstack(level=0) #중복된 값 오류
df2 = df1.set_index(['업종', '시군구'])['통화건수'].sum(level=[0,1]).unstack(level=0) #sum level = 0,1 level 0과 1이 같은 값끼리 그룹 연산 
df2.rank(axis=0, ascending = False)

#2) 각 시군구별 업종 비율 출력 
         족발/보쌈   중국음식   치킨
강남구    31         45         21.5
df1.drop(['일자', '시간대', '시도', '읍면동'],  axis='columns').sum(level=[0,1], axis=0).unstack()
df1.drop(['일자', '시간대', '시도', '읍면동'],  axis='columns').sum(level=[0,1], axis=0).unstack().sum(1)

f1 = lambda x: x/x.sum()*100
df1.drop(['일자', '시간대', '시도', '읍면동'],  axis='columns').sum(level=[0,1], axis=0).unstack().apply(f1, axis=1)

#선생님 
f1 = lambda x : x /x.sum()*100
df2.apply(f1, axis=1)


#3) 시간대별 배달콜수가 가장 많은 업종 1개 출력 
df3 = df1.drop(['일자', '시도', '읍면동', '시군구'],  axis='columns').set_index([ '업종', '시간대'])

df3.sum(level=[0,1],axis=0).unstack().idxmax()

#선생님 
df3 = df1.set_index(['시간대', '업종'])['통화건수'].sum(level=[0,1], axis=0).unstack()
df3.idxmax(axis=1)

#merge 
- join 연산 수행 
- equi join 만 가능 
- 두개의 데이터 프레임만 join 가능 
- outer join 가능
pd.merge(left,                   #첫 번째 데이터 프레임
         right,                  #두 번째 데이터 프레임
         how = {'left',          #조인연산 방법, left outer join
                'right',         #조인연산 방법, right outer join
                'outer',         #조인연산 방법, full outer join
                'inner'},        #조인연산 방법, inner join (조인조건 성립만 출력), 디폴트값 
         on=,                    #조인 컬럼
         left_on=,               #왼쪽 데이터(첫번째)조인 컬럼     in R : by.x by.y
         right_on=,              #오른쪽 데이터(두번째)조인 컬럼   in R : by.x by.y
         left_index=False,       #왼쪽 데이터(첫번째)인덱스 값으로 조인 여부
         right_index=False)      #오른쪽 데이터(두번째)인덱스 값으로 조인 여부 

df1 = DataFrame({'col1':['a', 'b', 'c'], 'col2' : [1,2,3]})
df2 = DataFrame({'col11' : ['a', 'b', 'd'], 'col22' : [10,20,30]})

pd.merge(df1, df2, left_on = 'col1', right_on='col11') #디폴트값인 inner join
pd.merge(df1, df2, left_on = 'col1', right_on='col11', how='outer') #전체 데이터 조인 

#index key를 갖는 경우의 조인 연산 
df11 = df1.set_index('col1')
df22 = df2.set_index('col11')

pd.merge(df11, df22, left_on = 'col1', right_on='col11')  #에러발생
pd.merge(df11, df22, left_index=True, right_index=True)   #조인가능

#연산에 방해되서 reset index로 index를 col으로 만드는 경우가 있음 

# 연습문제 
# emp 데이터를 데이터베이스에서 직접 호출 
import cx_Oracle
import os 
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16MSWIN949')  #커넥션 맺기 전에 해야함
con1 = cx_Oracle.connect("scott/oracle@localhost:1523/orcl")
emp = pd.read_sql('select * from emp', con = con1) 

# 직원의 이름, 연봉, 상위관리자명을 출력하되 상위관리자명이 없을 경우 본인이름을 출력 
df2 = pd.merge(emp.loc[:, ('EMPNO','ENAME','MGR','SAL' )], emp.loc[:, ('ENAME','EMPNO')], how='left', left_on='MGR', right_on= 'EMPNO')

df2.ENAME_y.fillna(df2.ENAME_x)

#선생님 
pd.merge(emp, emp, left_on='MGR', right_on='EMPNO', how = 'left')[['ENAME_x', 'ENAME_y', 'SAL_x']].fillna(axis=1, method='ffill')

# 벡터화 내장된 문자열 메서드  *** 12장 pandas의 벡터화된 문자열 함수 
L1 = ['a;b;c', 'A;B;C']
s1 = Series(L1 )

# 기본적으로 제공되는 문자열 메서드의 벡터 연산 활용 예제 
L1.split(';')[0] #적용불가, 벡터연산 불가  
[i.split(';')[0] for i in L1] #리스트 내포 표현식 처리 
list(map(lambda x: x.split(';')[0], L1)) #mapping 처리 
s1.str.split(';') # 벡터연산가능 , 장점 : 벡터연산이 가능, 단점 : 시리즈에서만 적용 가능  

#1. split 
s1.str.split(';') #벡터 연산 가능 

#2. replace 
s1.str.replace(';' , '|') #패턴 치환 가능, 값 치환 불가 

#3. 대소치환 
s1.str.upper()
s1.str.lower()
s1.str.title()

#4. 패턴여부 
s1.str.startswith('a')  #'a'로 시작 여부 
s1.str.endswith('c')    #'c'로 종료 여부
s1.str.contains('a')    #'a'의 포함 여부 

#5. 계수 
s1.str.count('a')       #'a'의 포함 횟수
s1.str.len()            # 각 문자열의 길이 

#6. 제거함수 
s2 = Series(['  ab  ', '  AB  '])
s2.str.strip().str.len()  #공백제거가 되어있는지 글자수를 세서 판단 
s2.str.strip()

s2.str.rstrip().str.len() #공백제거가 되어있는지 글자수를 세서 판단 
s1.str.lstrip('a')

#7. 색인 
s1.str.split(';')[0]  #a가 나오는 것이 아닌 s1[0] 값이 나옴 
s1.str.split(';').str[0] # 벡터화가 내장 된 색인 : a,A가 출력
s1.str.split(';').str.get(0) # 벡터화가 내장 된 색인 메서드 : a,A가 출력

#8. 위치값 출력 
s1.str.find('b')  #각 원소마다 위치값 출력 (없으면 -1)

#9. 문자열 결합 
s2.str.cat(sep=';')  #시리즈의 원소를 구분기호로 모두 결합 --> '  ab  ;  AB  '
s2.str.join(sep=';') #각 문자열의 글자를 구분기호로 모두 결합 -->
#     ; ;a;b; ; 
#     ; ;A;B; ; 

#10. pad : 글자 삽입 
s1.str.pad(width=10,          #총자리수
           side = 'both',     #삽입 방향
           fillchar='-')      #삽입 문자 
# 연습문제 
#prfessor.csv 파일 읽고 
df1 = pd.read_csv("professor.csv", encoding='cp949')
pro = pd.read_csv("professor.csv", encoding='cp949')

#1) email-id 출력 
df1.EMAIL.str.split('@').str[0]

#선생님 
pro = pd.read_csv("professor.csv", encoding='cp949')
pro['EMAIL'].str.split('@').str.get(0)

#2) 입사년도 출력 
df1.HIREDATE.str[0:4]

#선생님 
pro['HIREDATE'].str[:4]

#3) ID의 두번째 값이 a인 직원 출력 
f1 = lambda x : x.startswith('a',1,2)
vbool = list(map(f1, df1.ID))
df1.loc[vbool , :]

df1.loc[list(df1.ID.str.get(1)=='a'), :]
df1.loc[pro['ID'].str.get(1)=='a', :]

#선생님 
df1.loc[pro['ID'].str[1]=='a', :]

#날짜 파싱 및 포맷 변경
from datetime import datetime 

a1 = '2011/01/11' 

# 1. strptime : 문자 -- > 날짜
- datetime 내 함수 형식으로 사용 
- 벡터 연산 불가 
datetime.strftime 
datetime.strptime
 
L1 = ['2011/01/01', '2012/12/31']

v1 = datetime.strptime(a1, '%Y/%m/%d') #datetime.datetime(2011, 1, 11, 0 , 0 )
datetime.strptime(L1, '%Y/%m/%d') # 에러 발생, 벡터연산 안됨 

v2 = [datetime.strptime(i, '%Y/%m/%d') for i in L1] #내포 표현식으로 벡터연산 가능하게 만듦 

# 2. strftime : 날짜 --> 문자(날짜의 형식 변경)
- 메서드, 함수 형식 모두 가능 
- 벡터연산 불가 

v1.strftime('%A')
datetime.strftime(v1, '%A')
datetime.strftime(v2, '%A') #에러 발생, 벡터연산 불가 
