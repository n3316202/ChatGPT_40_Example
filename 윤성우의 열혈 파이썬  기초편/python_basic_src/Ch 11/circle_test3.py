# circle_test3.py

import circle as cc

def main():
    r = float(input("반지름 입력: "))
    ar = cc.ar_circle(r)
    print("넓이:", ar)
    ci = cc.ci_circle(r)
    print("둘레:", ci)

main()
