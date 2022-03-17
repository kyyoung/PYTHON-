# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:58:24 2020

@author: KITCOOP
"""
run profile1
import re 
# =============================================================================
# bank 데이터 불러온 후
# 1) 결혼 여부(marital)에 따른 housing과 loan의 각 현황별 고객 수를 다음과 같이 정리
#                        housing         loan
#                     yes      no       yes    no
# married
# divorced
# single

bank = pd.read_csv('bank-full.csv',  engine='python')

pat1 = re.compile('.+;', flags=re.IGNORECASE)
bank1 = bank.iloc[:,0].str.findall(pat1).str[0]
v1 = bank1.str.split(';').str[0]
v2 = bank1.str.split(';').str[1].str.replace("\"", "")
v3 = bank1.str.split(';').str[2].str.replace("\"", "")
v4 = bank1.str.split(';').str[3].str.replace("\"", "")
v5 = bank1.str.split(';').str[4].str.replace("\"", "")
v6 = bank1.str.split(';').str[5]
v7 = bank1.str.split(';').str[6].str.replace("\"", "")
v8 = bank1.str.split(';').str[7].str.replace("\"", "")
v9 = bank1.str.split(';').str[8].str.replace("\"", "")
v10 = bank1.str.split(';').str[9]
v11 = bank1.str.split(';').str[10].str.replace("\"", "")
v12 = bank1.str.split(';').str[11]
v13 = bank1.str.split(';').str[12]
v14 = bank1.str.split(';').str[13]
v15 = bank1.str.split(';').str[14]
v16 = bank1.str.split(';').str[15].str.replace("\"", "")

pat2 = re.compile('"[a-z]+"', flags=re.IGNORECASE)
v17 = bank.iloc[:,0].str.findall(pat2).str[9].str.replace("\"", "")

bank3 = {'age' : v1, 'job' : v2, 'marital' : v3, 'education' : v4, 'default' : v5,
        'balance' : v6, 'housing' : v7, 'loan' : v8, 'contact' : v9, 'day' : v10, 
        'month' : v11, 'duration' : v12, 'campaign' : v13, 'pdays' :v14, 'previous' : v15, 
        'poutcome' : v16, 'y' : v17}

df1 = DataFrame(bank3)
df2 = df1.loc[: ,['marital','housing','loan']]
d1 = df2.pivot_table(index = 'marital', columns='housing', aggfunc='count')
d2 = df2.pivot_table(index = 'marital', columns='loan', aggfunc='count')
d3 = pd.concat([d1, d2], axis=1)

# 2) hosing 또는 loan의 대출 여부에 따른 각 결혼여부 별 소득수준의 평균(balance)을 막대그래프로 출력
# hosing 또는 loan의 대출 여부는 둘다  yes인 경우, 둘 중 하나라도 yes인 그룹, 둘다 no인 그룹으로 표현
# (단, 아래 처럼 막대그래프 출력)
# 
# married  divorced  single   married  divorced  single     married  divorced  single
# 둘다 YES,                둘 중 하나 YES,                     둘다  no
 
df3 = df1.loc[: ,['marital','housing','loan', 'balance']]
df3.balance = df3.balance.astype('float')

df4 = df3.set_index(['marital', 'housing', 'loan']).sum(level=[0,1,2])
df5 = df4.reset_index()

df5.loc[( df5.housing=='no') & (df5.loan=='yes'), ['housing','loan']] ='y/no'
df5.loc[( df5.housing=='yes') & (df5.loan=='no'), ['housing','loan']] ='y/no'

df6 = df5.set_index(['marital', 'housing', 'loan']).sum(level=[0,1,2])
df6 = df6.sort_index(axis=0, level=[0,1,2]).swaplevel(0,1, axis=0)
df6.unstack().plot(kind='bar')

# =============================================================================

# =============================================================================
# 문제2	twitter.csv 파일을 읽고
twi = pd.read_csv('twitter.csv', engine='python')
twi = twi.loc[twi.apply(lambda x: x.notnull().all(), axis=1), :]
# 1) name과 username 패턴이 일치하는 사람 출력
twi.columns
twi.Name = twi.Name.str.lower()
twi.Username
twi.Username = twi.Username.str.lower()

pat1 = re.compile('[a-z]+', flags = re.IGNORECASE)
twi.Name = twi.Name.str.findall(pat1).str.join('')
twi.v2 = twi.Username.str.findall(pat1).str[0]

v2_n = v2.str[1:4]

f2 = lambda x, y: x in y
vbool = list(map(f2, twi.v2, twi.Name))
twi.loc[vbool, (['Name', 'Username'])]


v1.str.contains('Animal')
# 2) 유저별 게시물 포스트 현황을 살핀 후
# 유저별 최초 게시물 날짜가 가입 날짜로부터 1년 이후인 사람의 유저별 포스팅 수와 Likes Received 수를 출력
#  (가입한 날짜로부터 1년 동안 포스팅이 없었던 사람)
day1 = twi['Tweet Posted Time (UTC)'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M'))
day2 = twi['User Account Creation Date'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M'))
(day2 - day1).days 

f1 = lambda x, y: (x-y).days
day3 = list(map(f1, day1, day2))
twi['1년'] = day3
twi2 = twi.loc[twi['1년']>365, ('Username', 'Tweet Content', 'Likes Received', )]
twi3 = twi2.groupby(['Username'])[['Tweet Content', 'Likes Received']].agg({'Tweet Content' : 'count', 'Likes Received' : 'sum'})
# =============================================================================
