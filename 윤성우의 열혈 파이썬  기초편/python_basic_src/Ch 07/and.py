# and.py

def main():
    num = int(input("2의 배수이면서 3의 배수인 수 입력: "))

    if num % 2 == 0 and num % 3 == 0:
        print("OK!")
    else:
        print("NO!") 

main()
