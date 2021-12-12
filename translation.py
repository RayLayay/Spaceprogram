

from tkinter import *
from tkinter.messagebox import *
import requests


def translation():
    content = entry.get()
    content = content.strip()
    if content == '':
        showinfo('提示',message='输入要翻译的内容')
    else:
        url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {}

        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'

        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'

        resu = requests.post(url, data = data)
        result = resu.json()
        trans = result['translateResult'][0][0]['tgt']
        res.set(trans)
        return trans



window = Tk()

window.geometry('600x130+300+200')

window.title('中英文翻译')


label = Label(window,text = '输入要翻译的文字：',font=('微软雅黑',20),fg = 'red')

label.grid()

label1 = Label(window, text = '翻译之后的内容：',font=('微软雅黑',20),fg = 'red')
label1.grid(row = 1,column = 0)

res = StringVar()
entry = Entry(window,font=('微软雅黑',20))
entry1 = Entry(window,font=('微软雅黑',20),textvariable = res)

entry.grid(row = 0,column = 1)
entry1.grid(row = 1,column = 1)

button = Button(window,text = '翻译',width = 10,heigh = 2,command = translation)

button.grid(row = 2,column =0,sticky = W)

button1 = Button(window,text = '退出',width = 10,heigh = 2,command = window.quit)
button1.grid(row = 2,column = 1,sticky = E)


window.mainloop()