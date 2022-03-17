# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#데이터 분석에 필요한 모듈 호출 

import numpy  #array와 관련된 모듈
import pandas #dataframe과 관련된 모듈 

#모듈안에 있는 함수 목록 확인 
#파이썬에서는 변수던 뭐든 이름을 설정할때 . 을 사용할 수 없음 이유는 모듈을 호출할때 . 을 사용하기 때문, 그리고 명령어 앞에 꼭 모듈을 설정해야함 
dir(pandas)
pandas.read_csv('emp.csv')

#세부 호출 방법 
import pandas
pandas.read_csv('emp.csv')

# pandas에 대한 alias 지정  
import pandas as pd 
pd.read_csv('emp.csv')

#모듈 내 함수 직접 호출 --> 모듈.함수 이렇게 입력할 필요 없음  *** 중요 
from pandas import Series #pandas 안에 있는 Series 함수 호출  
from pandas import * #pandas안에 있는 모든 함수들을 호출! 

Series([1,2,3])

from pandas import read_csv
read_csv('emp.csv')

# 함수와 메서드의 차이 
메서드 - 함수의 또 다른 형태 
#함수 - 함수가 앞에 오고 뒤에 데이터 
function(data, ...) 
function(data= , a=, b=, ...)
#메서드 -  함수의 형태가 데이터 뒤에 와서 처리하는 형식, passing의 에러처리 빠르게 하기 위해서 사용   
data.function(a= , b=, ...)
'a'.isupper()
'a'.

# 리스트 : 데이터 표현을 위한 기본 자료구조(1차원), (cf: R에서는 벡터)
L1 =  [1,2,3]
type(L1)
L1 + 1 # 파이썬에서는 리스트(R, 벡터) 연산 수행 불가

  
