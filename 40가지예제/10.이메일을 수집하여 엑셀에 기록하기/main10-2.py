import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = "https://v.daum.net/v/20230303140011566"  # 이메일을 수집할 웹 페이지 주소
response = requests.get(url)  # 웹 페이지 요청

soup = BeautifulSoup(response.text, "html.parser")  # BeautifulSoup 객체 생성
emails = []

# 이메일 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 웹 페이지에서 모든 텍스트 추출
text = soup.get_text()

# 이메일 패턴 매칭 후 리스트에 추가
for match in re.findall(email_pattern, text):
    emails.append(match)

# 중복 제거
emails = list(set(emails))

# 결과 출력
print(emails)

#이걸로
#https://wikidocs.net/160668


#넘파이
#https://datascienceschool.net/01%20python/03.01%20%EB%84%98%ED%8C%8C%EC%9D%B4%20%EB%B0%B0%EC%97%B4.html

#https://laboputer.github.io/machine-learning/2020/04/07/pandas-10minutes/


#판다스(Pandas)는 Python에서 DB처럼 테이블 형식의 데이터를 쉽게 처리할 수 있는 라이브러리 입니다. 데이터가 테이블 형식(DB Table, csv 등)으로 이루어진 경우가 많아 데이터 분석 시 자주 사용하게 될 Python 패키지입니다.
#이 글에서는 아래와 같이 3가지 패키지가 활용됩니다.

#https://wikidocs.net/book/3488

# 이메일을 엑셀 파일로 저장
df = pd.DataFrame(emails, columns=["Email"])
#df.to_excel("10.이메일을 수집하여 엑셀에 기록하기/이메일.xlsx", index=False)
df.to_excel("이메일.xlsx", index=False)
