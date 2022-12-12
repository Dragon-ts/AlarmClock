import json5
import WriteJson as wj
#MADEBYDRAGON_TS#

readJson = wj.jsonMain()
js = json5.loads(readJson)


class box:
    global js
    title = js['windowBox']['title']
    geometry = f"{js['windowBox']['width']}x{js['windowBox']['height']}"
    background = js['windowBox']['color']
    resizable = js['windowBox']['allowChangeSize']


class window:
    class title:
        text = js['window']['title']['text']
        bg = js['window']['title']['bg']
        fg = js['window']['title']['fg']
        size = js['window']['title']['fontSize']
    class warn:
        bg = js['window']['warn']['bg']
        font = js['window']['warn']['font']
        size = js['window']['warn']['fontSize']
        bold = js['window']['warn']['bold']