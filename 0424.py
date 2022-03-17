# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:25:38 2020

@author: KITCOOP
"""

# multi index -- 색인이 어려움!
- index가 계층(level)적 구조를 갖는 경우
- 상위레벨 (level = 0), 하위레벨(level =1...)
- index, column 모두 설정 가능 

#1. muti index 생성 --인덱스 설정후 리스트로 전달!  
      col1   col2
A   a   1      2 
    b   3      4
B   a   5      6
    b   7      8
    
df1 = DataFrame(np.arange(1,9).reshape(4,2))
df1.index =[ ['A', 'A', 'B', 'B'], ['a','b','a','b']] #인덱스는 로우의 개수대로 써주기 
df1.index
df1.columns = ['col1', 'col2']
df1.index.names = ['상위인덱스', '하위인덱스']

#2) 
df2 = DataFrame(np.arange(1,17).reshape(4,4))
df2.index = [['A','A', 'B', 'B'], ['a', 'b', 'a', 'b']]
df2.columns = [['col_a','col_a', 'col_b','col_b', ], ['col1', 'col2','col1', 'col2']]
df2

#연습문제 : multi_index.csv 파일을 읽고 멀티 인덱스 설정 
df1 = pd.read_csv('multi_index.csv', encoding='cp949')
df1.index
df1.columns




df1.iloc[:,0]=df1.iloc[:,0].fillna(method='ffill')
df1.index = [df1.iloc[:,0] , df1.iloc[:,1]]
df1.drop(['Unnamed: 0'], axis='columns', inplace=True)
df1.drop(['Unnamed: 1'], axis='columns', inplace=True)
df1.index.names = ['도시', '하위인덱스']

df1.columns = [df1.columns, df1.iloc[0, :]]




Series(df1.iloc[0,:].values)

#선생님 

#step1) 지역컬럼 NA 치환 
df1.iloc[:,0]=df1.iloc[:,0].fillna(method='ffill')
#step2) 첫번재 두번째 컬럼 멀티인덱스 설정 
df1 = df1.set_index(['Unnamed: 0', 'Unnamed: 1'])
#step3) 컬럼값 변경 - > 냉장고 냉장고 TV TV *** 컬럼의 개수랑 맞아야함 
a1 = df1.columns.map(lambda x: np.where( 'Unnamed' in x, NA, x)) 
#np.where의 결과가 array이기 때문에 하나의 데이터 타입만 허용, NA가 문자열로 묶여서 나옴 Nan으로 안나옴 

a2 = df1.columns.map(lambda x: NA if 'Unnamed' in x else x)
#리스트 안에 묶임
df1.columns = Series(a2).fillna(method='ffill') 

#step4) 멀티컬럼 설정 
df1.columns = [df1.columns, df1.iloc[0, :]]

#step5) 첫번째 행 제거 
drop메서드 이름 전달을 받음, 멀티인덱스에서는 이름이 여러개이기 때문에 
어느 이름이 전달되는지를 정확하게 명시해줘야함 

df1 = df1.drop(NA, axis=0, level=0)  #멀티인덱스에서 level(인덱스의 위치)을 정확하게 명시    

#step6) index, column 이름 설정 
df1.index.names = ['지역', '지점']
df1.columns.names = ['품목', '구분']
df1

#2. multi-index 색인 
- ix, loc, iloc : 기본은 상위 레벨의 값만 색인 가능 
- ix, loc, iloc : 튜플 전달 시 하위 레벨의 값 색인 가능 
- xs : 하위 레벨 직접 색인 가능한 색인 메서드(함수 처럼 쓰임) 
#df1.xs('이름', 색인방향(index=0, column=1, 0이 디폴트), 인덱스 level(상위:0, 하위:1, 0이 디폴트))

df1['냉장고']  # 상위 레벨의 컬럼은 키 색인으로 추출 가능 
df1['price']  # 하위 레벨의 컬럼은 키 색인으로 추출 불가 

df1.loc[:, '냉장고'] #가능
df1.loc[:, 'price'] #불가

df1.loc['seoul', :] #가능
df1.loc['A', :] #불가 

#예) 모든 품목의 price 선택
df1.xs('price', axis=1 , level =1) 
df1.xs( , axis=[0,1])  #서로다른 레벨 전달 불가, 한가지만 전달 가능함 

#예) A 지점의 price 선택 
df1.xs('price', axis=1, level=1).xs('A', axis=0, level='지점')
df1.xs('price', axis=1, level=1).xs('A', axis=0, level=1)

#예) Seoul의 B 지점 선택, 서로 다른 레벨 전달(인덱스)
df1.loc['seoul', 'B', :]
df1.loc[('seoul', 'B'), :] 
df1.iloc[1,:] #위치기반 
#예) 냉장고의 price 선택, 서로 다른 레벨 전달(컬럼)
df1.loc[:, '냉장고', 'price']  #전달 불가 
df1.loc[:, ('냉장고', 'price')] #전달 
df1.iloc[:,0] #위치기반 

#예) 냉장고의 price, TV의 qty 선택 
df1.iloc[:,[0,3]]
df1.loc[:,[('냉장고', 'price'),('TV', 'qty')]]

#1.multi_index_ex1.csv 파일을 읽고 다음을 수행 
df1 = pd.read_csv('multi_index_ex1.csv', encoding = 'cp949')
df1.columns
df1.index

#1) 각 인덱스와 컬럼을 multi-index를 갖도록 설정 
df1 = df1.set_index(['지역', '지역.1'])

a1 = df1.columns.map(lambda x: x[0:2])
df1.columns = [a1, df1.iloc[0,:]]

df1.drop('지점', axis=0, level=0, inplace = True)

df1.index.names= ['상위품목', '하위품목']
df1.columns.names=['지역', '지점']

#t선생님 
#1) 각 인덱스와 컬럼을 멀티 인덱스를 갖도록 설정 
df1.columns = [df1.columns.map(lambda x: x[:2]), df1.iloc[0,:]]
#1-1) 첫번째 행 제외 
df1 = df1.iloc[1:,]  #혹은
df1 = df1.drop(0, axis=0)
#1-2) 멀티 인덱스 설정 
df1.index = [df1.iloc[:,0], df1.iloc[:,1]]
df1 = df1.iloc[:,2:]
#1-3) 인덱스 이름 설정 
df1.index.names = ['구분', '상세']
df1.columns.names=['지역', '지점']

#2) 컴퓨터의 서울지역 판매량 출력 
df1.loc['컴퓨터', '서울']

#선생님 
df1 = df1.astype('int')
df1.loc['컴퓨터', '서울']

#3) 서울지역의 컴퓨터의 각 세부항목별 판매량의 합계 출력 
df1 = df1.applymap(lambda x: int(x))

df1.loc['컴퓨터','서울'].apply(sum, axis=1)

#선생님 
df1.loc['컴퓨터', '서울'].sum(1) #axis 생략 가능 

#4) 각 지역의 A지점의 TV 판매량 출력 
df1
df1.xs('A', axis=1, level=1).xs('TV', axis=0, level=1)
df1.iloc[2,[0,3,6]]

df1.xs('A', axis=1, level=1) #컬럼은 컬럼방향에 맞게 axis=1, 하위레벨은 레벨대로 level=1
df1.xs('노트북', axis=0,level=1) #인덱스는 인덱스방향에 맞게 axis=0, 하위레벨은 레벨대로 level=1

#선생님 
df1.xs('A', axis=1, level=1).xs('TV', axis=0, level=1)

#5) 각 지역의 C지점의 모바일의 각 세부항목별 판매량 평균 출력 
df1.iloc[4:6, [2,5,8]].apply(sum, axis=1)/3

#선생님 
df1.xs('A', axis=1, level=1).loc['모바일', :].sum(1)

#6) 서울지역의 A지점의 노트북 판매량 출력 
df1.loc[:,('서울', 'A')].xs('노트북', axis=0, level=1)
df1.iloc[0,0]

#선생님 
df1.loc[:, ('서울', 'A')]
df1.iloc[:,0]

#산술연산 **** 매우 중요 
df1
axis=0, 행
axis=1, 컬럼 

#1) multi - index의 axis만 전달시 : multi-index와 상관없이 각 행별, 열별 연산 
df1.sum(0)
df1.sum(1)

#2) multi- index에 axis, level 전달시 : multi-index의 각 레벨이 같은 값 끼리 묶여 그룹연산(행별, 열별 전달 가능)
#지역 판매량 총 합 
df1.sum(axis=1, level=0) #상위 컬럼 서로 다른 행끼리 sum
#지점 판매량 총합 
df1.sum(axis=1, level=1) #상위 컬럼 서로 다른 컬럼끼리 sum
#구분(컴퓨터/가전/모바일)별 판매량 총합 
df1.sum(axis=0, level=0) # 상위 인덱스 서로다른 행끼리  sum
df1.sum(axis=0, level=1)  # 상위 인덱스 서로다른 컬럼끼리 sum이니깐 데이터 그대로 출력

#예) 구분(컴퓨터, 가전, 모바일)별 판매량 총합
df1.sum(axis=0, level=0)

#4. multi-index의 축 치환 및 정렬 
df1.swaplevel(0,1,axis=1) #지역이 같은 값끼리 묶이지 않음 
swaplevel(i,j, axis) i와 j는 교환하고자 하는 컬럼 혹은 인덱스 레벨, axis=0 행(인덱스), 1 컬럼 
지점           A     B     C     A     B     C     A     B     C
지역          서울    서울    서울    경기    경기    경기    강원    강원    강원

df1.swaplevel(0,1,axis=0)

#바꾸고 싶은 모양 
#서울 경기 강원 서울 경기 강원 서울 경기 강원 
#A   A     A   B    B   B     C   C   C
--> 다음과 같은 형식으로 먼저 인덱스를 정렬한 후 swaplevel을 수행해야함 

df1.sort_index(axis=1, level=[1,0]).swaplevel(0,1, axis=1)
지점           A                 B                 C            
지역          강원    경기    서울    강원    경기    서울    강원    경기    서울

df1.sort_index(axis=1, level=0) #상위레벨 순서대로 정렬
df1.sort_index(axis=1, level=1) #하위레벨 순서대로 정렬 
df1.sort_index(axis=1, level=[1,0]) 
