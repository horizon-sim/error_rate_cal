from importlib import import_module
from tkinter import *
import tkinter.messagebox as msgbox
import clipboard

root = Tk()
root.title("오차율 계산기")
root.geometry("640x480+500+200") 
root.resizable(False, False) 

def btn_cal():
    theory_result = float(theory_input.get())
    exper_result = float(exper_input.get())
    ocha = round((abs(exper_result - theory_result) / theory_result) * 100, 2)
    clipboard.copy(f"{ocha}")
    ocha_result = ocha,"%"
    number1.config(text=ocha_result)
    
def enter_cal(event):
    theory_result = float(theory_input.get())
    exper_result = float(exper_input.get())
    ocha = round((abs(exper_result - theory_result) / theory_result) * 100, 2)
    clipboard.copy(f"{ocha}")
    ocha_result = ocha,"%"
    number1.config(text=ocha_result)
    
root.bind('<Return>', enter_cal)
    
# 계산 프레임
number_frame = Frame(root)
number1 = Label(number_frame, text="(오차율)", font=("", 15, "bold"), height=6)
number_frame.pack()
number1.pack()

# 세트당 횟수
theory = Frame(root)
theory_title = Label(theory, text="[이론값]")
theory_input = Entry(root, width=30)
theory.pack(side="top")
theory_title.pack(pady=3)
theory_input.pack(pady=3)

# 세트 쉬는시간
exper = Frame(root)
exper_title = Label(exper, text="[실험값]")
exper_input = Entry(root, width=30)
exper.pack(side="top")
exper_title.pack(pady=3)
exper_input.pack(pady=3)

# 계산 실행 버튼
cal_frame = Frame(root)
cal = Button(cal_frame, text="계산", font=("", 15, "bold"), height=2, width=7, command=btn_cal)
cal.pack()
cal_frame.pack(side="bottom", ipady=25)

# my name
my_name_frame = Frame(root)
my_name_frame1 = Label(my_name_frame, text="제작 : 물리학과 코딩동아리\nversion : 2.0.0")
my_name_frame.place(relx=0.70, rely=0.90)
my_name_frame1.pack()


root.mainloop()