import tkinter

#创建主窗口
win = tkinter.Tk()

#设置标题
win.title('tkinter_study')

#设置大小和位置
win.geometry('400x400+200+50')

'''
Label:标签控件，可以显示文本
win：父窗体
text：显示文本内容
bg:背景色
font：字体
wraplength：指定text文本中多宽之后换行
justify:设置换行后的对齐方式
anchor：位置 n北，e东，w西，s南， center居中；还可以写在一起：ne东北方向
'''
label = tkinter.Label(
    text='我在学习python图形化界面',
    bg="pink", fg='red',
    font=("宋体", 20),
    width=20,
    height=10,
    wraplength=100,
    justify="left",
    anchor="center"
)
label.pack()

#进去循环，可以写控件
win.mainloop()