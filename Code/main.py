import tkinter as tk
import tkinter.font as tf
import threading

from apscheduler.schedulers.blocking import BlockingScheduler
from os import mkdir, path
from glob import glob
from time import sleep, strftime, localtime, time
from subprocess import run
from datetime import datetime
from random import randint
from pydub import AudioSegment
from pydub.playback import play
from inspect import isclass
from ctypes import pythonapi, c_long, py_object

import mainWindow
from line import AllLine

#######MADEBYDRAGON_TS#######


# 变量存储及声明
m = tk.Tk()
print(AllLine.line())
on_hit = False
textvar1 = tk.StringVar()
textvar1.set('456')
findMusic = tk.StringVar()
warnings = tk.StringVar()
findClock = tk.StringVar()
musicAllList = tk.StringVar()
findClock.set('等待导入闹钟...')
i = 0
j = 0
# 变量存储及声明


# 窗口设置
if True:
    m.title(mainWindow.box.title)
    m.geometry(mainWindow.box.geometry)
    m['background'] = mainWindow.box.background
    mr = mainWindow.box.resizable
    m.resizable(mr, mr)


# 窗口设置

# 指令设置
class cmd():
    def button1cmd():
        try:
            cmd.stopThread.stop_thread(cmd.myThread(cmd.alarms))
        except Exception as e:
            print(e)
        m.quit()

    def text1cmd():
        global on_hit
        if not on_hit:
            on_hit = True
            textvar1.set('123')
        else:
            on_hit = False
            textvar1.set('456')

    def checkmusic():
        global j
        music = ''
        try:
            mkdir('ClockSettings/music')
        except:
            pass
        musiclist = glob(path.join("ClockSettings/music", "*.mp3"))
        while j != len(musiclist):
            musiclist[j] = f'{musiclist[j][20:]}\n'
            music = f'{music}{musiclist[j]}'
            j += 1

        findMusic.set(f'发现{len(musiclist)}个音乐文件\n{music}')
        musicAllList.set(music)

    def Warnings():
        try:
            mkdir('ClockSettings')
            warnings.set("创建配置文件成功")
        except FileExistsError:
            warnings.set("导入配置文件成功")
        m.update()
        try:
            a = open('ClockSettings/Clock.txt', 'r', encoding='UTF-8')
        except FileNotFoundError:
            a = open('ClockSettings/Clock.txt', 'w')
            a.close()
            a = open('ClockSettings/Clock.txt', 'r', encoding='UTF-8')
        aa = a.read()
        a.close()
        sleep(2)
        if aa == '':
            warnings.set("没有发现设置的闹钟,请在出现的文本中输入时间 例:\n22:08\n11:45")
            m.update()
            sleep(2)
            run(r'notepad ClockSettings/Clock.txt')
            warnings.set("导入成功")
            m.update()
            cmd.clocks()
        else:
            warnings.set("请检查/修改您的闹钟是否为想设置的时间,检查结束后保存并关闭")
            m.update()
            sleep(2)
            run(r'notepad ClockSettings/Clock.txt')
            warnings.set("导入成功")
            m.update()
            cmd.clocks()

    def clocks():
        m.update()
        setclock = str(warnings.get())
        m.update()
        findClock.set(setclock)
        count = 0
        a = open('ClockSettings/Clock.txt', 'r', encoding='UTF-8')
        lines = ''
        for line in a.readlines():
            count += 1
            line = line.replace('：', ':')
            lines = f'{lines}{line}'
        send = f'检测到{count}个闹钟\n{lines}'
        findClock.set(send)
        a.close()

    def alarms():
        count = 0
        lines = ''
        a = open('ClockSettings/Clock.txt', 'r', encoding='UTF-8')
        for line in a.readlines():
            count += 1
            line = line.replace('：', ':')
            lines = f'{lines}{line}'
        a.close()
        lines = lines.split('\n')
        while '' in lines:
            lines.remove('')
        print(f'lines:{lines}')
        aread = open('ClockSettings/Clock.txt', 'r', encoding='UTF-8')
        aaa = aread.read()
        int(aaa.replace(':', '').replace("：", '').replace("\n", '').replace(" ", ''))
        musicl = musicAllList.get()
        musiclist = musicl.split('\n')
        print(str(musiclist))

        def job():
            msg = '您设置的 '
            nt = strftime('%H:%M', localtime(int(time())))
            msg = f'{msg}{nt} 闹钟到啦'
            print(msg)
            if len(musiclist) == 1:
                print(f'当前播放:{musiclist[0]}')
                # playsound(f'ClockSettings/music/{musiclist[0]}')
                music = AudioSegment.from_file(f'ClockSettings/music/{musiclist[0]}')
                play(music)
            else:
                rdmMusic = randint(0, len(musiclist) - 1)
                print(f'当前播放:{musiclist[rdmMusic]}')
                music = AudioSegment.from_file(f'ClockSettings/music/{musiclist[rdmMusic]}')
                play(music)

        sc = BlockingScheduler()
        global i
        while i != count:
            clhr = int(lines[i][:2])
            clmt = int(lines[i][3:])
            sc.add_job(job, 'cron', hour=clhr, minute=clmt, id=f'{datetime.now()}', replace_existing=True)
            sleep(0.2)
            i += 1
        sc.start()

    class myThread(threading.Thread):
        def __init__(self, func):
            super().__init__()

            self.func = func
            self.setDaemon(True)
            self.start()

        def run(self):
            self.func()

    class stopThread():
        def _async_raise(tid, exctype):
            """raises the exception, performs cleanup if needed"""
            tid = c_long(tid)
            if not isclass(exctype):
                exctype = type(exctype)
            res = pythonapi.PyThreadState_SetAsyncExc(tid, py_object(exctype))
            if res == 0:
                raise ValueError("invalid thread id")
            elif res != 1:
                # """if it returns a number greater than one, you're in trouble,
                # and you should call it again with exc=NULL to revert the effect"""
                pythonapi.PyThreadState_SetAsyncExc(tid, None)
                raise SystemError("PyThreadState_SetAsyncExc failed")

        def stop_thread(thread):
            cmd.stopThread._async_raise(thread.ident, SystemExit)

# 指令设置

# 指令执行



# 指令执行

# 小部件设置
def settings():
    if mainWindow.window.warn.bold == True:
        bd = tf.BOLD
    else:
        bd = tf.NORMAL
    text1 = tk.Label(m, text=mainWindow.window.title.text,  # 标题
                     bg=mainWindow.window.title.bg,
                     fg=mainWindow.window.title.fg,
                     font=('times', mainWindow.window.title.size))
    text2Font = tf.Font(family=mainWindow.window.warn.font,
                        size=mainWindow.window.warn.size,
                        weight=bd)
    text2 = tk.Label(m, textvariable=warnings,  # 提示
                     bg=mainWindow.window.warn.bg,
                     font=text2Font)
    text3 = tk.Label(m, textvariable=findMusic,  # 查看文件数
                     anchor='center',
                     bg='#FFCDD2')
    text4 = tk.Label(m, textvariable=findClock,
                     bg='#FFCDD2')
    button1 = tk.Button(m, text='Close',  # 我也不知道有啥用
                        command=cmd.button1cmd)
    button2 = tk.Button(m, text='Press',  # 关闭
                        command=cmd.text1cmd, relief='groove')
    button3 = tk.Button(m, text='点击导入闹钟',  # 导入闹钟
                        command=cmd.Warnings,
                        width=10)
    button4 = tk.Button(m, text='开启闹钟'    # 闹钟响铃主进程
                        , command=lambda: cmd.myThread(cmd.alarms),
                        width=5)

    text1.pack()
    text2.pack()
    button1.pack(side='bottom')
    button2.pack(side='bottom')
    text3.pack(side='left')
    text4.pack(side='right')
    button3.pack()
    button4.pack()


# 小部件设置


# 运行
settings()
#fir.quit()
cmd.checkmusic()
m.mainloop()
