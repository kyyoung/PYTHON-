# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:28:00 2020

@author: KITCOOP
"""
# 그래프 환경 설정 
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size=10)
plt.rc('figure', figsize = [10,10])

#그래프 옵션 전달 방법 
plt.rcParams.keys() 

#히스토그램 - 도수분포표에서 얻어지는 막대그래프 
df1 = pd.read_csv('cctv.csv', engine= 'python')
df1['CCTV수'].hist(bins=10)  #bins --> 막대의 개수 조정
df1['CCTV수'].hist(bins=[0,100,200,500,1000]) #리스트 전달 시 막대의 범위 
df1['CCTV수'].plot(kind= 'kde') #히스토그램을 연속형 분포의 형태로 ~ 커널밀도함수 


# os 종류 
1. 윈도우 
2. 유닉스 : HP-UX(HP), AIX(IBM), solaris(SUN)...
3. 리눅스(유닉스 무료판) : cens-OS, redhat, ubuntu**, pedora ...
redhat --> 오라클 편리 

-가상머신(virtual machine) : 한 os에 다른 os를 가상으로 설치하는 툴 
1) VMWare**
2) virtual PC 
3) virtual Box

윈도우에서 오렌지툴만 접속기능이 있어서 유닉스와 통신이 가능함, 나머지 r스튜디오나 아나콘다는 그런 기능이 없음 

#기타툴 
1) putty : 접속툴 
2) winscp : 파일전송 