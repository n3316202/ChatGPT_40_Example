import requests

response = requests.get('https://ipinfo.io/ip')
external_ip = response.text.strip() #좌우열 문자공백제거

print("외부 IP: " + external_ip)