# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:20:07 2020

@author: KITCOOP
"""
#cut 
# 연속현 변수의 구간분할, 범주형 변수 생성시 사용 
run profile1 
pd.cut(
       x, #연속형 변수를 갖는 객체 
       bins, #나눌 구간을 갖는 리스트
       right=True, #오른쪽 닫힘 여부(닫힘이 포함되는것임)
       labels=None, #각 구간의 이름 부여
       include_lowest = False #최소값 포함여부 
       )

s1=Series([1,2,3,5,7,10]) 
pd.cut(s1,bins=[1,5,10])  #1초과 5이하, 5초과 10이하 
pd.cut(s1,bins=[1,5,10],right=False) #1이상 5미만 5이상 10미만 
pd.cut(s1,bins=[1,5,10], include_lowest = True)  #첫 번째 값의 그룹 할당 : 최소값인 1이 포함되기 위해 0.999초과 부터 시작함 
pd.cut(s1,bins=[1,5,10], include_lowest = True, labels=['A','B'])  #그룹의 이름 부여 

#[연습 문제]
#subway2.csv 파일을 읽고 각 역별 승하차의 오전/오후별 인원수를 출력 
sub = pd.read_csv("subway2.csv", engine='python', skiprows=1)
sub
sub=sub.set_index(['전체','구분'])

f1=lambda x : int(x.split('~')[0])
s1 = Series(list(map(f1, sub.columns)))
sub.columns=pd.cut(s1,bins=[0,12,24], include_lowest=True, labels=['오전','오후'])
sub.columns.names=['시간']

f2=lambda x: int(x.replace(',',''))
sub = sub.applymap(f2)
sub.stack().sum(level=[0,2], axis=0)

#선생님 
sub['전체'] = sub['전체'].fillna(method='ffill')
#멀티인덱스
sub = sub.set_index(['전체', '구분'])
#천단위 구분기호 삭제
sub = sub.applymap(lambda x: int(x.replace(',' ,'')))
#컬럼이름 숫자형 시간 정보로 변경 
sub.columns = sub.columns.str[:2].astype('int')

#시간정보(컬럼)stack처리 컬럼을 인덱싱 
sub2 = sub.stack()

#참고 인덱스를 컬럼으로 변환
sub3 = sub2.reset_index()
sub3.columns = ['역', '구분', '시간', '인원수']
sub3

#시간컬럼 오전, 오후 변경 
sub3['시간대'] =pd.cut(sub3['시간'], bins=[0,12,24], include_lowest=True, labels=['오전', '오후'])
#pivot
sub3.pivot_table(index=['역','구분'], columns='시간대', values='인원수', aggfunc='sum')

#multi index에서 특정 level 선택  --위치값 기반 
sub2.index.get_level_values(0)
sub2.index.get_level_values(1)
sub2.index.get_level_values(2)


#groupby 메서드 
#-분리-적용-결합 
#특정 컬럼의 값 혹은 인덱스를 group화 
#groupby만 수행시 분리만 수행, 적용함수 따로 전달 
#[] 시리즈 [[]] 데이터 프레임 주의***** 
emp = pd.read_csv('emp.csv')
emp.groupby('DEPTNO') #아무것도 출력 안됨, 분리데이터 셋 저장만 한 상태 
emp.groupby('DEPTNO').sum() #groupby 컬럼은 인덱스로 출력 
emp.groupby('DEPTNO')['SAL'].sum() #연산 컬럼 선택 -시리즈형태로 출력 
emp.groupby('DEPTNO')[['SAL']].sum() #연산 컬럼 선택 - 데이터프레임 형식으로 출력  
emp.groupby('DEPTNO')['SAL', 'COMM'].sum()  #여러개 컬럼 연산시 사용 : 데이터 전체를 불러오는 것이기 때문에 메모리 차지 많이함 
emp.groupby(['DEPTNO', 'JOB'])['SAL', 'COMM'].sum()  #여러개의 컬럼 group by 시 
emp['SAL'].groupby(emp['DEPTNO']).sum() #연산 컬럼이 많이 없는 경우 연산 컬럼 먼저 호출: 계산하고 싶은 데이터만 불러오기 때문에 메모리 차지를 많이하지 않음 

emp2 = emp.groupby(['DEPTNO', 'JOB'])[['SAL']].sum()  #멀티인덱스 
emp2.index
emp2.groupby(level=0).mean() #멀티인덱스의 경우 특정 레벨 groupby 가능 

#참고- 오라클 성능 
select sum(sal)
  from emp 
 group by deptno;

# 참고 : index화 된 groupby 컬럼을 다시 컬럼으로 배치 
emp.groupby('DEPTNO')[['SAL']].sum().reset_index()
emp.groupby('DEPTNO', as_index=False)[['SAL']].sum()

#groupby 수행 시 여러 연산 함수 전달 
emp.groupby('DEPTNO')[['SAL']].agg(['sum', 'mean']) #mean과 max가 동시 전달 
emp.groupby('DEPTNO')[['SAL', 'COMM']].agg(['sum', 'mean']) #sal과 comm에 mean과 max가 동시 전달 
emp.groupby('DEPTNO')[['SAL', 'COMM']].agg({'SAL':'sum', 'COMM':'mean'}) #딕셔너리 형태로 sal에는 sum만 comm에는 mean만 전달 

in R) groupby 연산 수행 
ddply(emp,.(DETPNO), [summarise, SAL=sum(SAL), COMM=mean(COMM)])

#연습문제 
#1. sales 데이터를 불러와서 
sal = pd.read_csv('sales3.csv', engine='python')
#1) 각 날짜별 판매량의 합계를 구하여라 
sal.groupby('date')['qty'].sum()
#2) 각 code별 판매량의 합계를 구하여라 
sal.groupby('code')['qty'].sum()

#3) prodcut 데이터를 이용하여 각 날짜 별 상품별 매출의 합계를 구하여라 
pro = pd.read_csv("product.csv", engine = 'python')
 
sales2=pd.merge(sal, pro)

#선생님 
sales2['sum'] = sales2['qty']*sales2['price']
sales2.groupby(['date', 'code', 'product'])[['sum']].sum()

#사용자 정의 그룹핑 중요 ******
df1 = DataFrame(np.arange(1,26).reshape(5,5), columns= ['a','b','c','d','e'])
#1) 각 행, 컬럼마다 그룹이름 리스트로 순차적으로 전달, 같은 그룹이름끼리 묶임 
df1.groupby(['g1', 'g1', 'g2', 'g2', 'g2']).sum() #1행과 2행은 g1 3행~5행 g2
df1.groupby(['g1', 'g1', 'g2', 'g2', 'g2'], axis=1).sum() #1열2열은 g1 3열~5열 g2

#2) 각 행, 컬럼이름에 매칭되는 그룹이름을 딕셔너리 형식으로 전달 
df1.groupby({'a':'g1','b': 'g1', 'c':'g2','d': 'g2','e': 'g2'},axis=1).sum() 

#3) cutting object 
#예제) emp 데이터에서 각 연봉의 등급별 연봉의 평균을 출력 
# 단, 연봉의 등급은 3000이상 A, 1500dltkd 3000미만 B, 1500미만 c
c1 = pd.cut(emp['SAL'], [0,1500,3000,10000], right = False, labels =['C', 'B', 'A'])
emp.groupby(c1)['SAL'].mean()

#연습문제 
#2. delivery.csv 파일을 읽고 
df1 = pd.read_csv('delivery.csv', engine='python')

#1) 요일별로 각 업종별 통화건수 총 합 확인 
df1.dtypes
df1.일자 = df1.일자.astype('str')
v1 = [datetime.strptime(i, '%Y%m%d') for i in df1.일자]
v2 = [datetime.strftime(i, '%A') for i in v1]
df1['요일'] = v2

df1.groupby('요일')['통화건수'].sum()

#선생님 
deli =pd.read_csv('delivery.csv', engine='python', parse_dates=['일자'])
deli['요일'] = deli['일자'].map(lambda x :x.strftime('%A')).str.upper()
deli['통화건수'].groupby(deli[['요일', '업종']]).sum() #불가
deli.groupby(['요일', '업종'])[['통화건수']].sum() #가능 

#2) 평일과 주말(금,토,일) 각 그룹별 시군구별 통화건수 총 합 출력
df2 = df1.pivot_table(index=[ '시군구'], columns='요일', values='통화건수', aggfunc='sum')
df2.groupby({'Friday' : '주말', 'Saturday' : '주말', 'Sunday' : '주말', 'Monday' : '평일', 'Tuesday':'평일', 'Wednesday' : '평일', 'Thursday' : '평일', axis=1}).sum()

#선생님 
deli2 = deli.groupby(['요일', '시군구'])['통화건수'].sum().unstack()  #추천 
deli3 = deli.groupby(['요일', '시군구'])[['통화건수']].sum().unstack() #추천하지 않음 
deli3.columns #멀티컬럼이 됨 비추천함 
 
deli2.groupby(['주말','평일','주말','주말','평일','평일','평일']).sum()  #순서대로 전달하면됨 

#참고 - 딕셔너리 생성 시 하나씩 매핑 모두 전달 
{'Friday' : '주말', 'Saturday' : '주말', 'Sunday' : '주말', 'Monday' : '평일', 'Tuesday':'평일', 'Wednesday' : '평일', 'Thursday' : '평일'} #가능 

{['MONDAY', 'TUESDAY'] : '평일', ..., 'SUNDAY':'주말'}  #불가

#3. student.csv와 exam_01.csv 파일을 읽고 
#1) 각 성별 A,B,C 그룹에 해당되는 학생수(count) 출력 
# 단, A 그룹은 시험성적이 90이상, B그룹은 70 이상, C그룹은 나머지 
std = pd.read_csv('student.csv', engine='python')
exam = pd.read_csv('exam_01.csv', engine ='python')

df1 =pd.merge(std, exam, left_on ='STUDNO', right_on='STUDNO' )
c1 = pd.cut(df1['TOTAL'], [0,70,90,1000], right = False, labels =['C', 'B', 'A'])

#선생님 
std = pd.read_csv('student.csv', engine='python')
ex = pd.read_csv('exam_01.csv', engine ='python')
std2 = pd.merge(std,ex, on ='STUDNO')
std2['JUMIN'].str[6] #에러발생 , 문자열이 아니기 때문  
str(std2['JUMIN'][0])[6] 

std2['JUMIN'].astype('str').str[6] #문자타입으로 형 변환 후 수행 
v1 = std2['JUMIN'].astype('str').str[6].replace({'1': '남자', '2':'여자'}) #replace에 딕셔너리로 전달하면 여러개 동시 전달 가능
c1 = pd.cut(std2['TOTAL'],[0,70,90,101], right = False, labels = ['C', 'B', 'A'])

std2.groupby([v1,c1])['STUDNO'].count()

#groupby의 transform 메서드 
#R의 ddply 내부함수 transform과 유사

emp.groupby('DEPTNO')['SAL'].mean() #deptno 별 그룹핑
emp_1 = emp.groupby('DEPTNO')['SAL'].transform('mean') #전체 행 기준 그룹핑 

emp.join(emp_1, lsuffix='_x',rsuffix='_y' ) #조인메서드 : 중복된 컬럼이름 존재 시 접미어 전달 필수 
pd.merge(emp, emp_1, left_index = True , right_index = True)

#groupby의 apply 메서드로 사용자 정의함수 전달 
f1 = lambda x : x.sum()
emp.groupby('DEPTNO')['SAL'].apply(f1) #apply 적용 가능 

# 예제 
# 데이터프레임을 전달 받아 SAL 컬럼 역순 정렬, 가장 큰 2개 행 추출 함수 생성 
f_sort = lambda x: x.sort_values('SAL', ascending = False)

# 1) SAL이 큰 순서대로 전체에서 두 명 출력 
emp.sort_values('SAL', ascending = False)[:2] 
emp.sort_values('SAL', ascending = False).iloc[:2, :]

# 2) 부서별로 SAL이 큰 순서대로 두 명 출력 
emp.groupby('DEPTNO').apply(f_sort)
emp.groupby('DEPTNO', group_keys = False).apply(f_sort) 
#그룹바이 수행하면 그룹화 된 컬럼이 인덱스로 가지만 인덱스로 가지 않음, 
#이유는 종종 그룹바이 연산 결과와 그룹바이 컬럼이 중복되는 경우 종종 key 중복으로 groupby 연산 자체가 에러 발생 할 수 있음 
#이럴 경우 groupby 연산 컬럼의 index로 출력을 방지하여 출력하게 할 수 있음 

#[참고 - groupby 수행시 데이터 저장 형태] --DEPTNO 그룹별로 묶여 있음 
6    7782   CLARK    MANAGER  7839.0  1981-06-09 0:00  2450     NaN      10
8    7839    KING  PRESIDENT     NaN  1981-11-17 0:00  5000     NaN      10
13   7934  MILLER      CLERK  7782.0  1982-01-23 0:00  1300     NaN      10
7    7788   SCOTT    ANALYST  7566.0  1987-04-17 0:00  3000     NaN      20
10   7876   ADAMS      CLERK  7788.0  1987-05-23 0:00  1100     NaN      20
12   7902    FORD    ANALYST  7566.0  1981-12-03 0:00  3000     NaN      20
