# -*- coding: utf8 -*-
import tkinter as tk
import pyautogui as pag

import threading


#---------创建界面---------
window=tk.Tk()
window.title('mouse pos')
window.geometry('200x300')
window.wm_attributes('-topmost',1)# 顶置窗口


var1 = tk.StringVar()
label1 = tk.Label(window,textvariable=var1,bg='green', font=('Arial', 12), width=15, height=2)
label1.pack()
var2 = tk.StringVar()
label2 = tk.Label(window,textvariable=var2,bg='blue', font=('Arial', 12), width=15, height=2)
label2.pack()
var3 = tk.StringVar()
label3 = tk.Label(window,textvariable=var3,bg='white', font=('Arial', 12), width=15, height=2)
label3.pack()

def fun_timer():
    try:
        currentMouseX, currentMouseY = pag.position()
        var1.set(str(currentMouseX)+','+str(currentMouseY))

        global timer
        timer = threading.Timer(0.5, fun_timer)
        timer.start()
    except Exception as e:
        pag.alert(e)


timer = threading.Timer(1, fun_timer)
def srpstart():
    global timer
    timer.start()

def srpend():
    global timer
    timer.cancel()

def test():
    pass

btn_start = tk.Button(window,text='Start' , width=15, height=2,command=srpstart)
btn_start.pack()

btn_stop = tk.Button(window,text='Stop', width=15, height=2,command=srpend)
btn_stop.pack()

btn_test = tk.Button(window,text='Test', width=15, height=2,command=test)
btn_test.pack()



window.mainloop()

