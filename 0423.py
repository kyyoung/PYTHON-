# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:11:36 2020

@author: KITCOOP
"""
#외부 파일 입출력 함수 
pd.read_csv(
    file, #파일명
    sep=',', #분리구분기호
    header='infer', #첫 번째 행을 컬럼화 할지 여부, None설정시 value로 전달
    names=None, #컬럼이름 변경
    index_col=None, #인덱스 설정 컬럼
    usecols=None, #불러올 컬럼 전달
    dtype=None,   #불러올 데이터 타입 전달, 딕셔너리로 각 컬럼별 전달 가능
    engine=None,  # python 주로 사용 (한글, 맨끝라인 처리 가능), 인코딩으로 해결 안될때 
    skiprows=None,  #제외할 행 전달
    nrows=None,     #불러올 행 개수 전달
    na_values=None, #NA 처리할 문자열
    parse_dates=False,  #날짜 파싱할 컬럼 전달(리스트 형식이기 때문에 [] 사용), R에서는 없었던 기능 
    encoding=None,  #인코딩 옵션 
    )
pd.read_csv('read_test.csv', parse_dates=['date'])
pd.read_csv('read_test.csv', header=None)
pd.read_csv('read_test.csv', header=0)
pd.read_csv('read_test.csv', names=['A', 'B', 'C', 'D', 'E'])
pd.read_csv('read_test.csv', index_col = 'date') 
pd.read_csv('read_test.csv', usecols=['date', 'a']) 
pd.read_csv('read_test.csv', dtype='str') 
pd.read_csv('read_test.csv', dtype={'a':'str', 'c':'float'}) #데이터 타입 따로 컬럼별 설정가능
pd.read_csv('read_test.csv', dtype={'a':'str', 'c':'float'}).dtypes 
pd.read_csv('read_test.csv', na_values=['.' ,'-','?','!'])
pd.read_csv('read_test.csv', na_values={'a':['.' ,'-'],'b':['?','!']}) #na_values도 컬럼별 설정가능

pd.read_csv('read_test.csv', nrows=5)
pd.read_csv('read_test.csv', skiprows=5) #정수 전달시 행 수로 전달 : 본문에서 5개해 스킵, 컬럼이름도 없애버림 
pd.read_csv('read_test.csv', skiprows=[1,5]) #리스트 전달시 행 번호로 전달 : 본문에서의 위치값을 읽어 제외시킴 0행은 컬럼으로, 1행과 5행이 제거됨 

np.loadtxt('test3.txt') #공백, 탭 자동 분리
pd.read_csv('test3.txt', sep='\t') #분리구분기호 탭 전달
pd.read_csv('test3.txt', sep='\s+') #일치하지 않는 공백을 분리할 수 있음 

#적용함수 
#1. map 함수 
-1차원 데이터 셋 (list, array, Series) 적용 가능 
-리스트 출력 필요 
-map(func, *iterables)

#2. map 메서드 
-1차원 데이터 셋(Series, index object) 적용 가능 
-df1.col1.map(arg, na_action=None) : 함수가 필요로하는 추가 인자 전달 불가 

#3. apply 메서드 
-2차원 데이터 셋(DataFrame) 적용가능, 행별 열별 연산 수행 
-적용함수에  Series 형태(그룹)로 데이터를 전달, 그룹함수와 잘 어울림
-df1.apply(func, axis=0, **kwsds) : 함수가 필요로하는 추가 인자 전달 가능 

#4. applymap 메서드
-2차원 데이터셋(DataFrame) 적용가능, 원소별 연산 수행 
-df1.applymap(func) : 함수가 필요로하는 추가 인자 전달 불가 

#예제 다음의데이터 프레임에서 col1 컬럼 천단위 구분기호 제거 
df1 = DataFrame({'col1' : ['1,100', '1,200', '1,300'], 
                 'col2' : ['2,200', '3,300', '4,400']})  
df1 = df1.applymap(lambda x: int(x.replace(',','')))
df1.dtypes

#예제 test3.txt를 불러온 뒤 년도별 총 합 구하기 
np.loadtxt('test3.txt')
pd.read_csv('test3.txt', sep='\t')
df2 = pd.read_csv('test3.txt', sep='\s+', header=None)

f2=lambda x : x + '년' 
np.arange(2000,2014).astype('str').map(f2) #array map 메서드 사용불가 
df2.index = Series(np.arange(2000,2014)).astype('str').map(f2)

df2.apply(sum, axis=1)
df2
df2.columns = ['1월', '2월', '3월', '4월', '5월']
#연습문제 
#top(data, n=5) 함수 생성, 위 데이터에서 각 년도별 값이 큰 2개 월 출력 
#단, 사용자가 n의 값을 전달할 수 있도록 
예시--
       0   1
2000년 1월 2월
2001년 1월 2월

df2.loc['2000년',:].sort_values(ascending=False)[:2].index
df2.loc['2000년',:].sort_values(ascending=False)[:2].index.values
Series(df2.loc['2000년',:].sort_values(ascending=False)[:2].index)
 
def top(data, n=5):
    return data.sort_values(ascending=False)[:n]

top(df2.loc['2000년', :],2)  

df2.apply(top, axis=1, n=3)  

# apply 적용결과를 시리즈로 바꾸고 싶을때 사용많이함~!!! ******

df2.loc['2000년', :].sort_values(ascending=False)[:2].index

