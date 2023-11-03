# self_test.py

class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    fa.age = 20

    fa.up_age()
    AgeInfo.up_age(fa)

    print(fa.get_age())
    print(AgeInfo.get_age(fa))

   
main()
