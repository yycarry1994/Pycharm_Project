import tkinter

def func():
    print("aaaaaaaaaaaaaaaa")

win = tkinter.Tk()
win.title('Button_study')
win.geometry("400x400+200+50")

#创建按钮
button1 = tkinter.Button(win, text='按钮1', command=func(), width=10, height=10)
button1.pack() #按钮样式

button2 = tkinter.Button(win, text="按钮", command=lambda: print("bbbbbbbbbbbb"))
button2.pack()#按钮事件

button3 = tkinter.Button(win, text="退出", command=win.quit)
button3.pack()#按钮事件：退出

win.mainloop()