# circle_test1.py

import circle

def main():
    r = float(input("반지름 입력: "))
    ar = circle.ar_circle(r)
    print("넓이:", ar)
    ci = circle.ci_circle(r)
    print("둘레:", ci)

main()
