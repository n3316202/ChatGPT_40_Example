from socket import *

#SOCK_STREAM(TCP)통신  SOCK_DGRAN(UDP)통신
serverSock = socket(AF_INET, SOCK_STREAM) #그냥 AF_INET은 IPv4를, AF_INET6는 IPv6를 의미
serverSock.bind(('localhost', 8080)) #묶어준다. 아이피 + 포트번호(프로그램 번호)
serverSock.listen(1)#한명만 기다리겠다

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')
