import json5
from os import mkdir

def jsonMain():
    try:
        with open('ClockSettings/Settings.json5','r',encoding='UTF-8') as ff:
            ckjson = ff.read()
        print('检测到配置文件')

    except:
        try:
            mkdir('ClockSettings')
        except FileExistsError:
            pass
        with open('ClockSettings/Settings.json5','w',encoding='UTF-8') as ff:
            wjson = \
    '{\n\
  "windowBox": {    //窗口框设置\n\
    "title": "Clock v0.2.0 (DRAGON_TS未响应)",    //窗口框标题\n\
    "color": "#E1D4F9",    //窗口背景色\n\
    "width": 960,    //窗口宽度\n\
    "height": 540,    //窗口高度\n\
    "allowChangeSize": false    //是否允许改变大小\n\
  },\n\
  "window": {    //窗口内部设置\n\
    "title": {    //窗口标题设置\n\
      "text": "Clock v0.2.0",  //文字\n\
      "bg": "#E1D4F9",  //背景色\n\
      "fg": "#00ACC1",  //颜色\n\
      "fontSize": 30  //大小\n\
    },\n\
    "warn": {\n\
      "bg": "#E1D4F9",\n\
      "font": "方正喵呜简体",\n\
      "fontSize": 20,\n\
      "bold": true\n\
    }\n\
  }\n\
}'
            ff.write(wjson)
        with open('ClockSettings/Settings.json5', 'r', encoding='UTF-8') as ff:
            ckjson = ff.read()
    return ckjson