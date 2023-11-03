#참고 사이트
#https://076923.github.io/posts/Python-tkinter-1/

#tkinter는 GUI에 대한 표준 Python 인터페이스이며 Window 창을 생성할 수 있습니다.

#윈도우이름=tkinter.Tk()를 이용하여 가장 상위 레벨의 윈도우 창을 생성할 수 있습니다.
#윈도우이름.mainloop()를 사용하여 윈도우이름의 윈도우 창을 윈도우가 종료될 때 까지 실행시킵니다.
#생성 구문과 반복 구문 사이에 위젯을 생성하고 적용합니다.


#tkinter.Tk()를 적용할 경우 가장 기본적인 윈도우 창이 생성
import tkinter

window=tkinter.Tk()

window.title("홍길동")
window.geometry("640x400+100+100") #"너비x높이+x좌표+y좌표")
window.resizable(False, False) #윈도우이름.resizeable(상하, 좌우)

label=tkinter.Label(window, text="안녕하세요.")
label.pack()


window.mainloop()

################################
from tkinter import *

root = Tk()
label = Label(root, text='Hello World')
label.pack()

root.mainloop()

################################

from tkinter import *

root = Tk()
listbox = Listbox(root)
listbox.pack()

for i in ['one', 'two', 'three', 'four']:
    listbox.insert(END, i)

root.mainloop()

#####################################

from tkinter import *

root = Tk()
b1 = Button(root, text='테스트')
b1.pack()

def btn_click(event):
    print("버튼이 클릭되었습니다")

b1.bind('<Button-1>', btn_click)

root.mainloop()