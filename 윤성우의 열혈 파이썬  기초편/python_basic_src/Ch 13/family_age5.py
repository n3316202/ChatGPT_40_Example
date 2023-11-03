# family_age5.py

class AgeInfo:
    def __init__(self, age):
        self.age = age
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo(39)      # 아빠 나이 객체, 그리고 초기화 
    fa.up_age()
    print("1년 후 아빠 나이:", fa.get_age())
    
main()
