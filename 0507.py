# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:30:48 2020

@author: KITCOOP
"""

# 정규식 패턴 
-약속된 기호를 사용한 패턴 확인 및 추출 
-문자열 함수, 매서드에도 사용가능(일부)
-re모듈 호출 필요 
-findall 매서드로 정규식 패턴에 일치하는 패턴 추출 가능 
-자주쓰는 정규식 패터는 compile하여 변수화 가능 

# 예제 - 다음의 문자열에서 이메일 주소를 정규식 패턴으로 추출 
v_email = 'abc 12 ! abc@naver.com aaa ... 11 Abbb12-1@hanmail.net'
import re 
pat1 = re.compile('[a-z]+@[a-z]+', flags = re.IGNORECASE ) #ignorecase #대소문자 무시 
pat1 = re.compile('[a-z]+@[a-z]+.[a-z]+', flags = re.IGNORECASE )
pat1 = re.compile('[a-z]+@[a-z]+.[a-z]{2,4}', flags = re.IGNORECASE )
pat1 = re.compile('[a-z]+@([a-z]+)\.[a-z]{2,4}.', flags = re.IGNORECASE ) #그룹으로 묶인 () 메일엔진만 출력
pat1 = re.compile('([a-z0-9\.-]+)@([a-z]+)\.[a-z]{2,4}.', flags = re.IGNORECASE )
pat1 = re.compile('([a-z0-9-]+)@([a-z]+)\.[a-z]{2,4}.', flags = re.IGNORECASE ) #그룹으로 묶인 email id와 email 엔진이 출력 
#하이픈 기호는 대괄호 안에서 a-z, 0-9는 a부터z까지 0부터 9까지의 의미임, 나타나는 형태는 아님 
#이 표현식 끝에 하이픈을 쓰게 되면 하이픈이 문자로 해석됨 

#findall
# 패턴.findall(문자열)
pat1.findall(v_email)
Series(pat1.findall(v_email)).str[0] #내부표현으로 벡터연산하여 인덱싱처리 
Series(pat1.findall(v_email)).str[1]

#연습문제 ) 다음의 텍스트에서 '문자열+숫자' 패턴 추출 
txt = '''a a1. +12 
abc+123 ax1 df Ax+000'''
pat2 = re.compile('[a-z]+\+[0-9]+', flags = re.IGNORECASE) #+기호를 문자로 사용하고 싶으면 \+식으로 \를 붙여야함  
pat2.findall(txt)
#정규식패턴 그룹핑 가능 

#연습문제 
#shoppingmall.txt 파일을 읽고 쇼핑몰 웹 주소만 출력(총 25개)
#힌트 : 각 행을 문자열로 불러들인 후 하나의 문자열로 결합 후 진행 
sho = np.loadtxt('shoppingmall.txt', dtype='str', delimiter='\tn')
sho[6].find('h')

f1 = lambda x: x if x.find('h')==0 else 1
L2 = list(map(f1, sho))

vsite = ''
for i in L2:
    if i != 1:
        vsite = vsite + i
        pass


#선생님 
c1 = open('shoppingmall.txt')
list1 = c1.readlines()
c1.close() 

#리스트로 불러온 각 행 데이터 하나의 문자열로 결합 
#1) for 문
vstr = ''
for i in list1 :
    vstr = vstr + i
    
vstr

# 2) 결합메서드 사용
Series(list1).str.cat()  #세로로 붙임 

#패턴 추출 
#http :// ~ 
part1 = re.compile('http://[a-z]+\.[a-z]+\.[a-z.]+', flags = re.IGNORECASE)
part1 = re.compile('http://[a-z0-9./]+', flags = re.IGNORECASE)

part1.findall(vstr)

#참고 -정규식 패턴, 사용시 주의  . 사용 주의~~!!!!
pat2=re.compile('http://.+', flags =re.IGNORECASE) 
vstr2= 'n\nhttp://www.secretlabel.co.kr nnnnn \n\n광고집행기간 ' 
pat2.findall(vstr2)  #공백표시인 nnnn까지 다 추출됨, 그렇기 때문에 너무 축약하면 안됨
part1.findall(vstr2) #올바르게 출력 

#한글 : .사용 적절하게~ 
pat1 = re.complie('[가-힣]+', flags=re.IGNORECASE)

#str.findall
-패턴 추출 매서드
-Series에 적용 가능 
-백터연산 내장 
-series(대상).str.findall(패턴)

s1 = Series(['abc abcd1@naver.com af', 'dfj a12@daum.net xxx'])
pat1 = re.compile('.+@.+')  #.은 공백 숫자 문자 특수문자 다 포함시킴 
s1.str.findall(pat1)

pat2 = re.compile('[a-z0-9]+@[a-z.]+')
s1.str.findall(pat2).str[0] #.str 색인을 통해 리스트 벗김 

#연습문제 - 위 예제에서 이메일 아이디, 엔진 각각 추출 데이터 프레임 생성 
pat3 = re.compile('([a-z0-9]+)@([a-z]+)')
pat4 = re.compile('([a-z0-9]+)@([a-z]+)\.[a-z]+')
s1.str.findall(pat4)
s2 = s1.str.findall(pat3).str[0].str[0]
s3 = s1.str.findall(pat3).str[0].str[1]
df1 = DataFrame({'id' : s2, 'engine' :s3})

#연습문제 
# project_songpa_data.csv 파일을 읽고 동별 LAT와 LON의 평균
df1 = pd.read_csv('project_songpa_data.csv', engine='python')
df1 = df1.set_index('번호')
df1['동'] = df1['name'].str.split('동').str[0].
df1['동'] = df1['동'].str.replace('[0-9]', '') 
df1.groupby('동')['LAT', 'LON'].mean()

pat1 = re.compile('.+[동역]', flags=re.IGNORECASE)

ad1 = df1['name'].str.findall(pat1).str[0]
ad1 = ad1.str.replace('[0-9]' , '')
df1.groupby(ad1)['LAT', 'LON'].mean()

#선생님 
df1.name = df1.name.str.findall('[가-힣]').str.join('')  #가로로 붙임 중요 ***** 
df1.name.unique()
df1.name = df1.name.str.findall('[가-힣]+[동역]').str[0]
df1.groupby('name')['LON', 'LAT'].mean()

#np.random.randint
#- sampling 함수 
#- data에서의 sampling은 불가, sample number 추출 
np.random.randint(low,  #시작값
                  high, #끝값
                  size) #추출사이즈 
#예제) cancer.csv 파일을 읽고 train, test dat set을 7:3 비율로 랜덤 추출
cancer = pd.read_csv('cancer.csv')
cancer

#행과 열의 크기 
rownum = cancer.shape[0]
colnum = cancer.shape[1]
#sample number 획득 , 중복허용 
rn = np.random.randint(0, rownum, size = round(0.7*rownum)) 

#train, test data set 분리 --참고 
cancer_train = cancer.iloc[rn] 
cancer_test = cancer.drop(rn)  #train data set을 제외한 rownum 추출로 test data 
# 참고 - sampling in R
sample(c('a','b','v','r'), size =1) #문자벡터에서 추출가능 
sample(1:150, szie=1)#1~150 숫자벡터에서 추출 

# dummy variable 
# - factor형 변수를 0과 1을 사용하여 구분하는 방법 
# - 주로 class의 개수만큼 혹은 하나 적은 변수로 분할하는 방법 선택 
# - pd.get_dummies 함수 사용 
#- deep learning의 종속변수가 문자형태의 범주형인 경우 더미 변수여야함, 문자값을 넣을 수 없기 때문 
# case1)
v_y1 = ['Y', 'N', 'Y', 'Y']
pd.get_dummies(v_y1)

  Y_y Y_n 
Y  1   0 
N  0   1
Y  1   0
Y  1   0

# case2) 
v_y2 = ['A', 'B', 'C', 'A']
pd.get_dummies(v_y2)

    Y_A  Y_B  Y_C
A   1    0    0
B   0    1    0
C   0    0    1
A   1    0    0

    Y_A  Y_B 
A   1    0   
B   0    1   
C   0    0   
A   1    0   
   
#예제) cancer 데이터의 Y값 더미 변수 
df_dum = pd.get_dummies(cancer['diagnosis'], prefix= 'Y')

cancer.join(df_dum)
