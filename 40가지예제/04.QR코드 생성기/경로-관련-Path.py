#1. abspath(path)
#path의 절대경로를 반환한다. 입력받은 path에는 파일 혹은 폴더 이름이 들어온다.

import os.path
print("경로:"+ os.getcwd())

path = "C:\\Users\\toto\PycharmProjects\\ChatGPT_40_Example\\04.QR코드 생성기\\qrdata.txt"

#경로 중 디렉토리명만 얻기
#os.path.dir(path)
print(os.path.dirname("C:\\Users\\toto\PycharmProjects\\ChatGPT_40_Example\\04.QR코드 생성기\\qrdata.txt"))

#경로 중 파일명만 얻기
print(os.path.basename("C:\\Users\\toto\PycharmProjects\\ChatGPT_40_Example\\04.QR코드 생성기\\qrdata.txt"))

#경로 중 디렉토리명과 파일명 나누어 얻기
#os.path.split(path) 디렉토리명, 파일명이 리스트 형태로 나옵니다.

dir, file = os.path.split(path)
print(dir, file, sep="\n")

#디렉토리 안의 파일/서브 디렉토리 리스트
print(os.listdir("C:\\"))

#파일 혹은 디렉토리가 존재하는지 체크
print(os.path.exists(path))