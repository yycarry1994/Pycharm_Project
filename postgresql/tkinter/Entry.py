import tkinter


win = tkinter.Tk()

win.title("yudanqu")

win.geometry("400x400+200+50")

'''
Entyr:输入控件，用于显示简单文本内容
'''

#密文显示
entry1 = tkinter.Entry(win, show="*") #show="*" 可以表示输入密码
entry1.pack()

#绑定变量
e = tkinter.Variable()

entry2 = tkinter.Entry(win, textvariable=e)
entry2.pack()
#e代表输入框这个对象
#设置值
e.set("shdahdahdlahdhkjahdkjhakj")
#取值
print(e.get())
print(entry2.get())

win.mainloop()



