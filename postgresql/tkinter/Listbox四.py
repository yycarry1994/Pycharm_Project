import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# MULTIPLE支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

def myprint(event):
    # print(lb.curselection()) # 返回下标
    print(lb.get(lb.curselection())) # 返回值
lb.bind("<Double-Button-1>", myprint)
win.mainloop()