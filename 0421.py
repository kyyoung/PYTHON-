# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:15:03 2020

@author: KITCOOP
"""

run profile1 

#Series 색인 
s1=Series([1,2,3,4], index= ['a', 'b', 'c', 'd'])

s1[0] #positional indexing
s1['a'] #label indexing, 팬시 색인
s1[0:2] #slice indexing
s1[[0,2]] #list indexing
s1[s1>2] #boolean indexing 

# pandas 확인함수 

s2 = Series([NA, 2, 3, 4], index=['a', 'b', 'c', 'd'])

s2.isnull() #메서드 형식 
s2.notnull() 

pd.isnull(s2) #함수형식 
pd.notnull(s2)

#Data Frame 
- 행과 열을 갖는 2차원 구조 
- 서로 다른 데이터 타입 허용, 한 컬럼은 같은 데이터 타입만 가능 
- key 값은 column을 사용 

1. 생성
d1 = {'col1' : [1,2,3,4], 'col2' : [5,6,7,8]}  #딕셔너리 허용 : 다른 형태의 데이터 입력 가능 
df1 = DataFrame(d1)
DataFrame(df1, columns = ['COL1', 'COL2']) #df1의 컬럼 인덱스와 다른 값 입력하면 Nan

arr1 = np.arange(1,9).reshape(4,2) # array : 사용가능하나 같은 타입의 데이터만 허용해서 DF 만들기 불편함
df2 = DataFrame(arr1, index=['a','b','c','d'],  columns = ['COL1', 'COL2'] ) #새로운 인덱스와 컬러명 부여 


2. 기본메서드 
df1.index # 추출해서 변경가능
df1.columns #추출해서 변경가능 
df1.dtypes # 각 컬럼의 데이터 타입 확인, oracle의 desc, R의 str과 비슷 
df1.values # key값 제외, 데이터들만 배열형식 출력 

3. index  수정 --> 시각화 할때 데이터 프레임을 수정하고 진행하면 빠름 
df1.index = [1,2,3,4] #전체 덮어쓰는 것 가능 , 일부 수정 불가
df1.index.name  = 'month'  #인덱스에 설명/주석 달기
df1.columns.name = 'columns'  #컬럼 이름에 대한 설명/주석 달기
df1.name = 'DataFrame' #시각화할때 사용 

#4. 색인
df1['col1']  #key indexing 
df1.col1  # key indexing, df1$col1 in R  

# 색인을 직접 전달하는 것은 불가, 색인 메서드 사용  
df1[0:3] #slice 값을 색인으로 전달시 행 우선순위로 바뀜 
df1.iloc[0,0] #positional indexing, 위치값 기반 인덱싱 
df1.iloc[0,:] #슬라이스 색인 가능
df1.iloc[0:3, 0] #슬라이스 + 정수색인 가능 
df1.iloc[[0,1], [0,1]] #정수색인 가능 
df1.iloc[df1.col>3, :] #불리언 색인 불가 

df1.loc[1, 'col1'] # label indexing, 이름값 기반 인덱싱
df1.loc[1,'col1']
df1.loc[df1.col1>3, :] #불리언 색인 가능 

#위치와 이름 인덱싱 둘다 가능한 메서드   
df1.ix[1, 'col1']  # 1이 행 이름으로 해석됨, 색인 가능 하나 없어질 수 있는 메서드  
df1.ix[1,0]        # 1은 행이름, 0은 컬럼 포지션

df3 = DataFrame(np.arange(1,9).reshape(4,2))
df3.ix[0,0] #행이 이름을 갖지 않는 경우 포지션으로 해석됨 

df1.iloc[-1, :] #맨끝행 출력 cf) R은 맨끝행 제외하고 출력됨 
df1.iloc[1:, :] #첫번째 행을 제외하는 대체 슬라이싱 

df1.drop('col1', axis=1) #컬럼제외 
df1.drop(1, axis=0) #행제외 
df1.drop(0, axis=0) #포지션 전달 불가, 오로지 인덱스 이름값만 전달 가능 

#1. 아래와 같은 데이터 프레임 생성후(세 개의 컬럼을 갖는)

from numpy import nan as NA

#name price qty 
#apple 2000 5
#mango 1500 4
#banana 500 10
#cherry 400 NA 

d2= {'name' : ['apple', 'mango', 'banan', 'cherry'], 'price' : [2000,1500,500,400], 'qty' :[5,4,10, NA]} 
df2 = DataFrame(d2)

#1) mango의 price와 qty 선택 
df2.iloc[1:2,: ]

#선생님 
df2.iloc[1,[1,2]]
df2.iloc[1:2, 1:3]
df2.loc[1,['price', 'qty']]

#2) mango와 cherry의 price 선택 
df2.iloc[[1,3], 0:2]

#선생님 
df2.iloc[[1,3],1:2] #차원축소방지, 데이터프레임 출력 
df2.iloc[[1,3],1] #차원 축소됨, 시리즈 출력 

#3) 전체 과일의 price만 선택 
df2.loc[:, 'price'] #차원축소, 시리즈 출력 

#선생님 
df2.loc[:, 'price' : 'price']  #문자 시퀀스배열됨(범위를 정할때는 눈에 보이는대로! 숫자범위와 다름), R은 안됨 
                               #loc 매서드내 이름의 슬라이싱 가능 
                               # 'a' : 'c' -> a~c까지로 해석(마지막 범위 포함)
#4) qty의 평균 
df2.loc[:, 'qty'].mean(axis=0)

#선생님 
df2.qty.mean() #pd.mean 호출, 3개의 값 평균
np.mean(df2.qty) #pd.mean 호출 (numpy mean 무시됨, 이유는 데이터프레임이기 때문에 pandas mean이 자동호출됨)
                 #numpy.mean처럼 사용해주고 싶으면 데이터타입을 어레이로 바꾸거나 skipna = False로 설정
#[참고]
arr1 = np.array([5,4,10,NA])
arr1.mean() #np.mean 호출되면서 NA값 출력 : Null을 포함해서 Na값이 나옴  
Series(arr1).mean() #pd.mean 호출되면서 NA무시하고 평균값 출력, NA 무시하는게 디폴트값  
Series(arr1).mean(skipna = False) #pd.mean 호출, NA무시 못해서 NA값 출력

#5) Price가 1000 이상인 과일 이름 출력
df2.loc[df2.price >=1000, :] 

#선생님 
df2.loc[df2.price >=1000, :] 

#6) cherry, banana, mango, apple 순 출력 

df2.iloc[[3,2,1,0], :]

#7) qty -> QTY 수정*** 버그발생요인, qty 대문자로 변경하면서 원본객체에 반영이 안될 수 있음 인덱스와 데이터를 따로 관리하는 사상때문 

#선생님 
df2.columns[2] = 'QTY' #수정불가
df2.columns.values[2] = 'QTY' # 수정가능 - 비추천, 파이썬이 index를 따로 관리하기 때문에 반영이 안될 수 있음, key에 대한 리턴이 NA일수 있음  

# 버그 발생 안하는 제일 좋은 방법  --> column 새로운 객체 만들어서 덮어써야함 
# 위의 수정방식은 index objext에 반영되지 않아 데이터프레임의 index와 index object 의 값들이 불일치 발생할 수 있음 
aa1 = df2.columns.values 
aa1[2] = 'QTY' 
df2.columns = aa1 

df2.rename({'price' : 'PRICE'}, axis =1) #rename 매서드도 전체 변경 가능, index와 index object 값 전체 변경 


#8) name에 'a'를 포함하는 행 출력 

#선생님 
df1.name in 'a'
'a' in 'apple' #apple에 a 패턴 포함 여부 
'a' in 'cherry' 

f1 = lambda x : 'a' in x
vbool = list(map(f1, df2.name))
df2.loc[vbool, :]

#참고 
'b' in ['bc', 'bd']  # 'b' == 'bc' or 'b' == 'bd' ? 라는 의미, 벡터연산 불가
np.in1d(np.array(['b']), ['bc', 'bd']) # 'b' == 'bc' or 'b' == 'bd' ? 라는 의미, 벡터연산 가능 

#추가 연습문제------------ 
#1)df2의 이름이 apple 또는 cherry인 행을 선택 ( in 연산자 사용, in1d 연산자 사용 )
df2.loc[df2.name=='apple', :]  
df2.loc[df2.name=='cherry', :] 
#기본 in 연산자- 벡터연산 불가, mapping 필요  
'apple' in ['apple', 'cherry']
# mapping 필요 
f1 = lambda x: x in ['apple', 'cherry']
vbool = list(map(f1, df2.name))
df2.loc[vbool, :]

#numpy용 in 연산자 벡터연산 가능
df2.loc[np.in1d(df2.name, ['apple', 'cherry']), :]  #numpy 형식이라 pandas에서는 그렇게 좋은 표현식은 아님 

#pandas용 in 연산자 벡터연산 가능
df2.loc[df2.name.isin(['apple', 'cherry']) , :] 

#2)name에 'o'가 포함된 행 선택 
f2 = lambda x : 'o' in x 
vbool2 = list(map(f2, df2.name))
df2.loc[vbool2, :]

#9) name값을 rowname으로 설정 후 name컬럼 제외 

#선생님 
df2.index = df2.name
df2 = df2.drop('name', axis=1) #axis =1, 열삭제

#10) apple과 cherry행 삭제 
 
#선생님 
df2 = df2.drop(['apple', 'cherry'], axis= 0)

#