# -*- coding: utf8 -*-
import tkinter as tk
import pyautogui as pag
import time
import threading


def fun_timer():
    try:
        currentMouseX, currentMouseY = pag.position()
        var1.set(str(currentMouseX) + ',' + str(currentMouseY))
        pag.moveTo(1689, 796, 0.5)
        pag.click()

        global timer
        timer = threading.Timer(0.5, fun_timer)
        timer.start()
    except Exception as e:
        pag.alert(e)


timer = threading.Timer(1, fun_timer)


def srpstart():
    global timer
    timer.start()


# ---------创建界面---------
window = tk.Tk()
window.title('mouse pos')
window.geometry('200x100')
window.wm_attributes('-topmost', 1)  # 顶置窗口

var1 = tk.StringVar()
label1 = tk.Label(
    window,
    textvariable=var1,
    bg='green',
    font=(
        'Arial',
        12),
    width=15,
    height=2)
label1.pack()

btn_start = tk.Button(
    window,
    text='Start',
    width=15,
    height=2,
    command=srpstart)
btn_start.pack()


window.mainloop()
