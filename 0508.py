# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:40:46 2020

@author: KITCOOP
"""

#파이썬 날짜 표현 
from datetime import datetime

# 1. 현재 날짜 및 시간 
d1 = datetime.now()  # in R : Sys.Date(), in oracle : sysdate

d1.year  #datetime 객체의 년 추출 
d1.month #datetime 객체의 월 추출
d1.day   #datetime 객체의 일 추출
d1.hour  #datetime 객체의 시 추출
d1.minute #datetime 객체의 분 추출
d1.second #datetime 객체의 초 추출

# 2. 날자 파싱(문자열 -> 날짜 인식)
# 2-1) datetime.strptime 
#-두번째 인자(날짜 포맷) 생략 불가 
#-벡터연산불가 

d2 = datetime.strptime('2020-05-31', '%Y-%m-%d')

#2-2) pd.to_datetime
#-날짜 포맷 생략 가능 
#-벡터 연산 가능 
pd.to_datetime(['2020/01/01', '2020/01/02'])
pd.to_datetime(['01/12/20', '01/13/20'], format = '%m/%d/%y') #이런 형태는 포맷 살려야함 

#2-3)datetime.datetime 
datetime(2012,1,2)


# 3. 날짜 포맷 변경 
d2.strftime('%Y')

# 4. 날짜 연산 
d2 - d1 #timedelta object로 출력 
(d2 - d1).days #timedelta object의 일수 출력 
(d2 - d1).seconds #timedelta object의 초수 출력 

# d1 날짜로부터 7일뒤 날짜 계산 
d1 + 7 #연산 불가 

# 5. timedelta를 사용한 날짜 연산 
from datetime import timedelta 
d1 + timedelta(7) #7일뒤 
d1 + timedelta(1/24) #1시간뒤

# 6. offset 사용한 날짜 연산 
import pandas.tseries.offsets
dir(pandas.tseries.offsets)

from pandas.tseries.offsets import Day, Hour, Second,  Week

d1 + Day(5)
d1 + Hour(12)
pandas.tseries.offsets.Week
#emp.csv 파일을 읽고 
emp = pd.read_csv('emp.csv', engine='python')
#1) 년, 월, 일 각각 추출 
emp.HIREDATE = emp.HIREDATE.str.replace('0:00', '').str.strip()
f1 = lambda x :datetime.strptime(x, '%Y-%m-%d')
emp.HIREDATE = emp.HIREDATE.apply(f1)

#2) 급여 검토일의 요일 출력(단, 급여 검토일은 입사날짜의 100일 후 날짜) 
emp.HIREDATE + timedelta(100)

#3) 입사일로부터의 근무일수 출력 
d1 = datetime.now()
f2 = lambda x: (d1 - x).days
emp.HIREDATE.apply(f2)


#선생님 
datetime.strptime(emp.HIREDATE, '%Y-%m-%d %H:%M')  #벡터연산 불가 
emp.HIREDATE.map(lambda x : datetime.strptime(x, '%Y-%m-%d %H:%M'))
emp['HD'] = emp.HIREDATE.map(lambda x : datetime.strptime(x, '%Y-%m-%d %H:%M'))

#1) 년 월 일 각각 추출 
v_year = emp['HD'].map(lambda x: x.year)
v_month = emp['HD'].map(lambda x: x.month)
v_day = emp['HD'].map(lambda x: x.day)

#2) 
emp.HD.map(lambda x: x+DAY(100).strftime('%A'))

#3) 
(d1-emp.HD).map(lambda x: x.days)

# 7. 날짜 INDEX 생성 및 색인 
pd.date_range(start,   #시작날짜
              end,     #끝날짜
              periods, #기간(개수)
              freq)    #날짜빈도 

pd.date_range(start ='2020/01/01', end='2020/01/31')
pd.date_range(start ='2020/01/01', end='2020/01/31', freq='7D')
pd.date_range(start ='2020/01/01', end='2020/01/31', freq = 'W') #매주 일요일 
pd.date_range(start ='2020/01/01', end='2020/01/31', freq = 'W-MON') #매주 월요일

# 연습문제
#1부터 연속적인 값을 갖는 Series 생성,
#2020년 매주 일요일 날짜를 인덱스를 갖도록 생성 
s1 = Series(np.arange(1,53))
d1 = pd.date_range(start='2020/01/01', end='2020/12/31', freq = 'W')
s1.index=d1
s1

#선생님 
d1 = pd.date_range(start='2020/01/01', end='2020/12/31', freq = 'W')
s1 = Series(np.arange(1,len(d1)+1), index=d1)

#datetime 객체를 인덱스로 생성 시 날짜값 색인 가능 
s1['2020']
s1['2020-12']

# truncate : 날짜 인덱스를 갖는 경우 날짜 선택 특정 개체에 대한 날짜의 선택 
s1.truncate(after='2020-11-01')
s1.truncate(before='2020-11-01')

#그런데 이 방법 안쓰고 
s1[:'2020-11-01'] #이렇게 해도 됨, 날짜를 슬라이스 색인 값으로 사용가능(단, 끝범위 포함)

# 8. resample : 날짜의 빈도수 변경 
-upsampling : 더 많은 날짜수로 변경(주별 -> 일별)
-downsampling : 더 적은 날짜수로 변경(일별 - > 월별)

s1.resample('D', fill_method='ffill') #upsampling시 fill_method 필요 : 주별에서 일별이니깐 인덱스의 빈공간을 채워야하기 때문에 fill_method 사용 
s1.resample('D').asfreq() #upsampling시 새로 생긴 날짜의 value가 NA로 출력
s1.resample('M').sum() #downsampling시 그룹함수 전달 필요 일에서 월별로 묶어야 되기 때문에 

#예제) s1을 일별데이터로 정리,  value는 0으로 표현 
s2 = s1.resample('D').sum() #upsamling시 생긴 값이 0으로 표현됨 

#연 습 문 제
# 부동산 매매지수.csv 파일을 읽고 
df1 = pd.read_csv('부동산_매매지수.csv', engine= 'python', skiprows=1)
df1 = df1.iloc[1:514, :]
#1) 2008년 4월 7일부터 관찰된 매 주 각 구별 매매지수라고 할 때 날짜 컬럼추가
day1 = datetime.strptime('2008-04-07', '%Y-%m-%d')
day2 = day1 + Week(512)

d1=pd.date_range(start=day1, end =day2, freq='7D' )

df1['날짜'] = d1

#2) 2017년 기준 작년 대비 상승률 상위 10개 구를 상승률과 함께 출력 
df1 = df1.set_index('날짜')
df1 = df1.astype('float')
df1['년도'] = df1.index.astype('str').str[0:4]
d2 = df1['2017']
d3 = df1['2016']
df2 = pd.concat([d3,d2])
df3 = df2.groupby('년도').sum()
df3.sub(df3)
s1 = (df3.iloc[1,:]-df3.iloc[0,:] )/ df3.iloc[0,:] *100
s1.sort_values(ascending = False).iloc[0:10]

run profile1
#선생님 
df1 = pd.read_csv('부동산_매매지수.csv', engine= 'python', skiprows=[0,2])

#데이터프레임 NA 삭제 
df1.iloc[0,0] = NA  #NA가 하나라도 들어가 있음 삭제되나?  
df1.dropna(axis=0, how ='all')  #전체가 NA인 경우만 삭제됨 

df1.iloc[0].isnull().any()  #NA가 하나라도 포함되어 있는가?
df1.iloc[0].isnull().all()  #w전체가 NA인가?
df1.iloc[0].isnull().sum()  #NA의 개수 
df1.apply(lambda x: x.isnull().all(), axis=1)
df1 = df1.loc[df1.apply(lambda x: x.notnull().all(), axis=1), :]

#1) 
df1.index = pd.date_range('2008/04/07', periods=df1.shape[0], freq = '7D')

#2) 
df11 = df1.resample('Y').mean()

df11['2017']
- df11['2016']

(df11['2017'].values - df11['2016'].values) / df11['2016'].values * 100

#shift : 날짜의 이동 함수 

df11.shift(periods=1,   #이동범위
           freq=None,   #기간(년단위, 월단위)
           axis=0,      # 디폴트는 이전 행
           fill_value=None)  #이전값 가져올 수 없는 경우 NA리턴 대신 

df22 = (df11 - df11.shift(1)) / df11.shift(1)*100 
df22['2017'].T.sort_values('2017-12-31', ascending=False)[:10]
