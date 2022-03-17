# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:23:30 2020

@author: KITCOOP
"""
#파이썬 시각화 
#figure와 subplot 
-figure : 그래프가 그려진 전체 창(도화지 개념)
-subplot : 창 내부에 실제 그래프를 그릴 공간 
-figure 와 subplot에 이름 부여 가능  
1. figure와 subplot의 생성 
import matplotlib.pyplot as plt 

#1-1) 하나씩 출력 
fig1 = plt.figure() #figure 생성 
ax1 = fig1.add_subplot(2,  # figure를 분할할 행의 수 
                       2,  # figure를 분할할 컬럼의 수
                       1)  # 분할된 subplot의 위치

ax2 = fig1.add_subplot(2,  # figure를 분할할 행의 수 
                       2,  # figure를 분할할 컬럼의 수
                       2)  # 분할된 subplot의 위치

#1-2) 동시에 출력 
fig2, ax = plt.subplots(2,2)  #2*2의 subplot 할당 
ax[0,0] #subplot의 색인으로 접근 
ax[0,1]
ax[1,0]
ax[1,1]

# 2. 선그래프 그리기 
#2-1) Series 
s1 = Series([1,3,4,7,8,9])
ax1.plot(s1) #특정 subplot에 직접 전달 

s1.plot() #마지막 호출된 subplot에 그리거나 새창에 그림 

#2-2) Data Frame
# - 컬럼별 서로 다른 선 그래프 출력 
# - index는 x 축 눈금으로 자동 전달 
# - column은 범례로 자동 전달 
 
df_price = DataFrame({2000:[1900,2400,2700], 2001:[1600,1800,2400]})
df_price.index = ['A', 'B', 'C']
df_price.index.name = 'product' #x축 이름 
df_price.columns.name = 'year' #범례 이름 
df_price.plot()

# 연습문제 
#cctv.csv 를 불러오고 각 년도별 검거율 증가추이를 각 구별로 비교할 수 있도록  plot 도표 그리기 
df1 = pd.read_csv('cctv.csv', engine='python')

df2 = df1.pivot_table(index='구', columns='년도', values='검거')
df2.plot()

#선생님 
cctv = pd.read_csv('cctv.csv', engine='python')
cctv['검거율'] =(cctv['검거']/cctv['발생']) * 100 
cctv2 = cctv.pivot_table(index='년도', columns='구', values='검거율')
cctv2.index.name
cctv2.columns.name 
cctv2.plot()

#3. 그래프 옵션 전달 
cctv2.plot(title = '구별 년도별 범죄검거율 현황',   #그래프 제목
           xticks=cctv2.index,                    #x축 눈금 
           ylim = [0,130],                        #y축 범위
           fontsize=8,                            #글자 크기 
           rot=30,                                #x 축 눈금 회전각 
           style = 'k-')                         #라인 스타일        
# 참고 - 라인스타일 전달 방식 
# 참고 - 1) style로 색, 라인형태 동시 전달 방식 
'r--' : 붉은 dash line  
'k-' : 검은색 이은선 
'ko--' : 검은색 dot dash line 
'k.' : 검은색 점선 

cctv.plot?
# 참고 -2) 색과 라인 스타일 각각 전달 방식 
s1.plot(color='r', linestyle='--')

#1) x축 이름, y축 이름 설정 
plt.xlabel ('발생년도') 
plt.ylabel ('검거율') 

#2) 그래프 제목 
plt.title('구별 검거율 변화 추이')
 
#3) x축, y축 눈금 범위 변경 
plt.xlim 
plt.ylim([0,130])

#4) x축, y축 눈금 변경 
plt.xticks(cctv.index)
plt.yticks 

#5) 범례
plt.legend(fontsize = 6, 
           loc = 'best', 
           'title' = '구이름') 
plt.xlabel('aaa')

#4. barplot 그리기 
# - 컬럼별 서로 다른 그룹 
# - 각 컬럼의 데이터들이 서로 다른 막대로 출력 기본 
# - stacked = True 설정시 하나로 쌓인 그래프 출력 
# - column name이 범례로 자동으로 전달 
# - index name 이 x 축 눈금으로 전달 

df_fr = DataFrame({'apple' : [100,110,200], 
                   'banana' :[150,170,210],
                   'mango' : [50,70,100]})

df_fr.plot(kind='bar')
plt.xtikcs(rotation = 0) #x축 눈금 회전 전달 

#[참고 - 그래프 출력 시 한글 깨짐 해결] 
plt.rc('font', family = 'Malgun Gothic')

#[ 참고 - 파이썬 프롬프트에서 그래프 팝업 호출] 
C:\Users\KITCOOP>ipython    #일반 아나콘다 호출 
C:\Users\KITCOOP>ipython --pylab #pylab(시각화)모드 

%matplotlib qt # 일반 아나콘다 실행 후 pylab모드 전환 방법 

#[참고- spyder()]
Tools > prefernces > Ipython console > Graphics > Graphics backend에서 automatic 변경 후 spyder restart(restart 반드시 필요)
#cmd 창 
ipython 하고 실행  

#연습문제 
#kimchi_test.csv 파일을 읽고 
# 각 월별로 김치의 판매량을 비교할 수 있도록 막대그래프로 표현 
df1 = pd.read_csv('kimchi_test.csv', engine = 'python')
df1 = df1.pivot_table(index='판매월', columns='제품', values='수량', aggfunc='sum')

df1.plot(kind='bar')

#선생님 
kim = pd.read_csv('kimchi_test.csv', engine = 'python')
kim2 = kim.pivot_table(index='제품', columns='판매월', values='수량', aggfunc='sum')
plt.rc('font', family = 'Malgun Gothic')
kim2.plot(kind='bar')
plt.xticks(rotation=0)
plt.legend(title='판매월', fontsize=8)
plt.title('월별 김치 판매량')
plt.ylabel('판매량')
