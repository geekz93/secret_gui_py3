from tkinter import *
import os
import hashlib
import time

master = Tk()
master.title("secret")
#master.resizable(False, False)#不能改变窗口尺寸

#调整文本显示框的大小
Password = Entry(master, font="微软雅黑", bd=10, justify=CENTER)
Password.grid(row=0, column=0, padx=20, pady=5)
Password.delete(0, END)
Password.insert(0, "请输入密码^_^")

#answer 
def crack():
    #弹出顶层窗口
    #设置延时打开exe
    #弹出顶层窗口与sleep冲突，使用 updata()解决
    enter=Password.get()
    ans = hashlib.md5(enter.encode("utf8")).hexdigest()

    # hknudxnt
    if ans == 'f7a6d065216090af5ec48c5c7e1332fb':
        #创建顶层窗口
        top = Toplevel()
        top.title("舟:")
        msg = Label(top, text="素芳,做我女朋友好吗!", font="微软雅黑, 36",
                    fg="red", justify=CENTER, padx=20,pady=5).pack()
        top.update()#提交窗口数据

        hide = "hide.dll"
        rose = "./dll/rose.exe"

        if hide in os.listdir('./dll'):
            os.rename("./dll/hide.dll",rose)

        #窗口居中
        curWidth = top.winfo_reqwidth()    # get current width
        curHeight = top.winfo_height()     # get current height
        scnWidth,scnHeight = top.maxsize() # get screen width and height

        #now generate configuration information
        tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
        (scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
        top.geometry(tmpcnf)
        top.update()                       # update window ,must do

        time.sleep(2)
        os.system("cmd.exe /c start %s"%rose )
        
    else:
        Password.delete(0, END)
        Password.insert(0, "密码不对哦 T_T")


OpenButter = Button(master, text="芝麻开门", command=crack, bd=5, width=10
                    ).grid(row=1, column=0, pady=1)

#窗口居中
master.update()                       # update window ,must do
curWidth = master.winfo_reqwidth()    # get current width
curHeight = master.winfo_height()     # get current height
scnWidth,scnHeight = master.maxsize() # get screen width and height

# now generate configuration information
tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
master.geometry(tmpcnf)


mainloop()
