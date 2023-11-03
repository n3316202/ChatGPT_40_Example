# circle_test2.py

from circle import ar_circle
from circle import ci_circle

# from circle import ar_circle, ci_circle

def main():
    r = float(input("반지름 입력: "))
    ar = ar_circle(r)
    print("넓이:", ar)
    ci = ci_circle(r)
    print("둘레:", ci)

main()
