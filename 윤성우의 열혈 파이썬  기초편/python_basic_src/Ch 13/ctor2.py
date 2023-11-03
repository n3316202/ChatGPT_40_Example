# ctor2.py

class Const:
    def __init__(self, n1, n2):
        self.n1 = n1     # self.n1은 인스턴스 변수, n1은 매개변수
        self.n2 = n2     # self.n2는 인스턴스 변수, n2는 매개변수

    def show_data(self):
        print(self.n1, self.n2)

def main():
    o1 = Const(1, 2)
    o2 = Const(3, 4)
    o1.show_data()
    o2.show_data()
   
main()
