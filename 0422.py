# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:15:59 2020

@author: KITCOOP
"""

run profile1 

df1 = DataFrame(np.arange(1,13).reshape(4,3))
df2 = DataFrame(np.arange(13,19).reshape(2,3))
df3 = DataFrame(np.arange(10,90,10).reshape(4,2))


#5. 구조 수정 
#1) row 추가 
df1.append(df2)
df1.append(df2, ignore_index = True) #index 무시 

#2) column 추가 
df1['a'] =[11,21,31,41]

#6. 산술연산
df1.columns = ['a', 'b', 'c']
df3.columns = ['a', 'b']

df1 + df3 #서로 같은 컬럼끼리 연산됨( 키 불일치는 NA 리턴)
df2
df4 = DataFrame(np.array([100,101,102]).reshape(1,3)) 
df2 + df4 #서로 같은 인덱스끼리 연상됨(키 불일치는 NA 리턴)  

#산술연산 메서드(add(+), sub(-), mul(*), div(/)) 
df2.add(df4)  #df2 + df4 결과와 동일 
df2.add(df4, fill_value=0) #NA가 fill_value 값으로 치환된 후 연산

#브로드캐스팅 기능 
#array
arr1 = np.arange(1,9).reshape(4,2)
arr1 + arr1[:, 0:1]   #첫번째 컬럼을 차원 유지 방법으로 추출후 연산! 
df1.iloc[:, 0] #시리즈이기 때문에 행이 key
df1.iloc[:,0:1] #데이터프레임이기 때문에 컬럼이 key 
df1 = DataFrame(arr1)
df1 + df1.iloc[:, 0]  #df1.iloc[:, 0]가 Series 형태이고 키는 [0,1,2,3], df1의 키는 [0,1]이기 때문에 [2,3]은 NA 처리 
df1 + df1.iloc[:,0:1] #df1키는 [0,1] 와 df1.iloc[:,0:1]의 키는 [0]이기에 반복연산되지 않음, 두 개의 키가 일치하지 않으면 반복연산 안됨  

df1.add(df1.iloc[:,0],axis=0)  #컬럼끼리의 반복연산(서로 다른 행을 묶어 전달) 

#연습문제 
#다음의 데이터 프레임에서 2000년 기준 가격 상승률 출력 
df1 = DataFrame({'2000' : [1000,1100,1200], '2001' : [1150, 1200, 1400], '2002' : [1300, 1250, 1410]}, index = ['a', 'b', 'c'])

df2 = df1.sub(df1.iloc[:,0], axis=0)
df2.div(df1.iloc[:,0], axis=0)*100

#선생님 
df1.sub(df1.iloc[:,0], axis=0).div(df1.iloc[:,0], axis=0) * 100


#연습문제 
#1. 3*4 배열 생성 후 a,b,c,d 컬럼을 갖는 df1 데이터 프레임 생성
df1 = DataFrame(np.arange(1,13).reshape(3,4))
df1.columns = ['a', 'b', 'c', 'd']
#2. 2*4 배열 생성 후 a,b,c,d 컬럼을 갖는 df2 데이터 프레임 생성
df2 = DataFrame(np.arange(1,9).reshape(2,4))
df2.columns = ['a', 'b', 'c', 'd']
#3. 위 두 데이터 프레임 union 후 df3 생성 
df3 = df1.append(df2, ignore_index=True)
#4. df3에서 0,2,4 행 선택해서 새로운 데이터 프레임 df4생성 
df4 = df3.iloc[[0,2,4], :]
#5. df3에서 'b', 'd' 컬럼 선택 후 새로운 데이터 프레임 df5 선택 
df5 = df3.loc[:, ['b','d']]
#6. df3-df4 수행(NA리턴 없이)
df3-df4
df3.sub(df4, fill_value=0)

#7. reindex : 인덱스의 재배치 
df1.loc[:,['b','c','a','d']]  #컬럼 재배치 
df1.loc[:,['b','c','d','e']]  #컬럼 reindexing
DataFrame(df1, columns=['b','c','d','e'])  #컬럼 reindexing 
df1.reindex(['b','c','d','e'], axis=1, fill_value=0) #axis=0 행배열, axis=1 컬럼배열, NA를 0으로 치환 옵션 사용 가능 

#예제 - df1의 df2 승수값 출력(df1**df2), 단 df2값이 없는 경우 1로 수정  
df1
df2
df1**df2
df1**df2.reindex(df1.index, fill_value=1)

# 8. 정렬 
df1 = DataFrame({'col1' : [3,2,4,1], 'col2' : ['a', 'c', 'd', 'b']})
df1.sort_values?

df1.sort_values(by,        #정렬대상
                axis=0,    #정렬방향
                ascending = True,   #정렬순서 
                inplace = False,    #정렬후 원본 대체 여부 
                na_position = 'last')  #NA 배치 순서 
# R에서 orderby와 비슷 

df1.sort_values('col1', ascending = False )  #원본 대체 되지 않고 보여주기만함 
df1.sort_values('col1', ascending = False, inplace = True) #inplace옵션 사용으로 원본 대체 됨 
df1.sort_values(['col1', 'col2'], ascending = [False, True]) #컬럼별 정렬순서 전달 


#연습문제 
#1. 'test3.txt' 파일을 읽고 다음과 같은 데이터 프레임 형태로 변경 
df1=np.genfromtxt('test3.txt', dtype =None, delimiter = ' ', encoding ='UTF8' )
df1 = DataFrame ({'20대' : [7.5, 7.4, 6.6, 7.4, 7.5, 7.9], '30대' :[3.6, 3.2, 2.9,3.4,3,3], '40대' :[3.5,3,2,2.1,2.1,1.9], '50대':[3.3, 2.8, 2, 2.1, 2.1, 1.9], '60세이상' :[1.5,1.2,1.1,2.7,2.5,1.9]})
df1.index=['2000년', '2001년', '2002년', '2011년', '2012년', '2013년']

a1 = np.loadtxt('test3.txt', dtype= 'str', delimiter='\t', encoding = 'UTF8') 
df1 = DataFrame(a1)

#선생님 
a1=np.loadtxt('test3.txt')
df1= DataFrame(a1)
df1.columns = ['20대', '30대', '40대', '50대', '60세이상']
df1.index = np.arange(2000, 2014) +'년' #에러 
f1 = lambda x: str(x) + '년'
df1.index = list (map(f1, np.arange(2000,2014)))
df1 = df1.astype('int')
#2. 2010년부터의 20~40대 실업률만 추출하여 새로운 데이터 프레임을 만들어라 
df1.index.name = 'year'
df1
df2=df1.iloc[3:6, :]

#선생님 
df2 = df1.loc['2010년','20대' : '40대']

#3. 30대 실업률 추출하되, 소수점 둘째자리의 표현식으로 출력 
df3 = df1.iloc[:, 2]
df3.astype('float32')
dp.dtypes?
print('%2.f' % int(df3))
pd.options.display.float_format = '{:.2f}'.format
df3

#선생님 
df1.loc[:,'30대']

'%2.f' % 3.6 #스칼라의 형식 변경 
'%2.f' % df1.loc[:'30대'] #벡터연산 불가 

f2 = lambda x: '%2.f' % x
df1.loc[:, '30대'] =list(map(f2,df1.loc[:, '30대']))

#4. 60세 이상 컬럼 제외
df1.iloc[:, 0:4]

#선생님 
df1 = df1.drop('60세이상', axis=1)

#5. 30대 컬럼의 값이 높은 순으로 정렬 
df1.sort_values('30대', ascending = False)

#선생님 
df1.sort_values('30대', ascending = False)
#문자열이기 때문에 정렬이 숫자순서대로 안됨.
1 100 2 200 이런식으로 정렬됨 
#주의 *** 
df1.loc[:, '30대']=df1.loc[:, '30대'].astype('float')
#숫자로 변환후 순서 정렬 
df1.sort_values('30대', ascending = False)


#적용 메서드 : 함수의 반복 처리를 도와주는 메서드  ********
1.map : 1차원 구조에 적용 가능, 원소별 적용 cf) map함수와 기능은 같으나 쓰는 순서는 다름 
df1.loc[:, '30대'].map(f2)

2.apply : 2차원 구조에 적용 가능, 행별 또는 컬럼별 적용(그룹연산에 주로 사용)
df1.apply(sum, axis=0)  #행별연산이지만 컬럼별적용이라고 보면됨
df1.apply(sum, axis=1)  #컬럼별 연산이지만 행별적용이라고 보면됨  
#원소별 적용은 안됨, 그룹연산만 가능

3.applymap : 2차원 구조에 적용 가능, 원소별 적용 
f2 = lambda x: '%2.f' % x
df1.applymap(f2)

#연습문제 - key 값 주의!!!
df1 
1.2000년 기준 증감률 
df2 = df1.iloc[0:1,:]
df1 -df2

#선생님 
(df1 - df1.iloc[0,:])/df1.iloc[0, :]*100

2.20대 기준 증감률 
df1 - df1.iloc[:,0:1]  #안됨, 차원축소해도 key값은 변하지 않음 
df1.sub(df1.iloc[:,0:1], axis=0)  #불가 20대 컬럼이 데이터프레임으로 전달
df1.sub(df1.iloc[:,0], axis=0)    #가능 20대 컬럼이 시리즈로 전달  ******

df1.sub(df1.iloc[:,0], axis=0).div(df1.iloc[:,0], axis=0)*100

#주의 - 데이터프레임의 브로드캐스팅 
#시리즈(1차원)와 데이터프레임(2차원)의 연산시만 브로드캐스팅이 가능 (키 일치시)
#따라서 데이터프레임과 데이터프레임끼리는 산술연산 메서드를 통해서도 브로드캐스팅 전달 불가 


3. 각 년도별 각 연령대가 차지하는 실업률의 비율 리턴 
        20대    30대   40대  50대  총합 
2000년 15.23    10.10  10.08  10.05 이런형식 ~ 

df1
f5 = lambda x: x/x.sum()*100
df1.apply(f5, axis=1)

#참고 - 파일불러올때 오류 안나는법 
pd.read_table('여아신생아.txt', engine = 'python') 