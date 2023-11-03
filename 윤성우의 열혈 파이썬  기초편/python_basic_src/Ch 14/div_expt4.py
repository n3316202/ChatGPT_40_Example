# div_expt4.py

def main():
    bread = 10     # 열 개의 빵

    try:
        people = int(input("몇 명? "))
        print("1인당 빵의 수: ", bread / people)
        print("맛있게 드세요.")
    except ValueError:
        print("입력이 잘못되었습니다.")
    finally:
        print("어쨌든 프로그램은 종료합니다.")
    
main()
