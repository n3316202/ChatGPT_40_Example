import requests
from bs4 import BeautifulSoup
import re

#url = "https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression"
url = "https://v.daum.net/v/20230303140011566"  # 이메일을 수집할 웹 페이지 주소
response = requests.get(url)  # 웹 페이지 요청

print(response.text)
soup = BeautifulSoup(response.text, "html.parser")  # BeautifulSoup 객체 생성
emails = []

#https://s205203.tistory.com/29
# 이메일 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 웹 페이지에서 모든 텍스트 추출
text = soup.get_text()
print(text)

#파이썬에서 정규 표현식을 사용할 때, 내장 모듈인 re를 사용하고 있습니다. re 모듈에서 제공해주는 함수들을 보면 match(), fullmatch(), findall(), search() 등등이 있는데
# 어떤 함수를 사용하냐에 따라 결과가 달라지게 됩니다.
# 이메일 패턴 매칭 후 리스트에 추가
for match in re.findall(email_pattern, text):
    emails.append(match)

# 중복 제거
emails = list(set(emails))

# 결과 출력
print(emails)
