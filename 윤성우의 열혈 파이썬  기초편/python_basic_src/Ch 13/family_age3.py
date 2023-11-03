# family_age3.py

class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()      # 아빠 나이 객체 생성
    mo = AgeInfo()      # 엄마 나이 객체 생성
    me = AgeInfo()      # 나의 나이 객체 생성

    fa.age = 39       # 아빠 현재 나이
    mo.age = 35       # 엄마 현재 나이
    me.age = 12       # 나의 현재 나이

    sum = fa.get_age() + mo.get_age() + me.get_age()
    print("가족 나이 합:", sum)

    fa.up_age()
    mo.up_age()
    me.up_age()
    sum = fa.get_age() + mo.get_age() + me.get_age()
    print("1년 후의 합:", sum)
    
main()
