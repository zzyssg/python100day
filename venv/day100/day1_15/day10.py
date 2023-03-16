"""
day10   图形用户界面GUI：GUI开发模块--tkinter，基于tk工具包，提供了跨平台的GUI控件
        步骤（GUI通常由事件驱动，需要main loop监听鼠标键盘等）：
            1、导入需要的tk模块
            2、创建顶层窗口
            3、添加GUI组件
            4、编写代码，组织功能
            5、进入主事件循环main loop
        游戏开发

"""
import tkinter
import tkinter.messagebox

def main():
    flag = True

    #修改标签上的文字
    def change_label_text():
        nonlocal  flag
        flag = not flag
        color,msg = ('red','hello,world') \
            if flag else ('blue','bye,world')
        label.config(text=msg,fg=color)
    #确认退出

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('找乐子')
    label = tkinter.Label(top,text='Hello World',font='Arial -32',fg = 'red')
    label.pack(expand = 1)
    #创建一个装按钮的容器
    panel = tkinter.Frame(top)
    bt1 = tkinter.Button(panel,text='change',command=change_label_text)
    bt1.pack(side='left')
    panel.pack(side='bottom')
    #主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()