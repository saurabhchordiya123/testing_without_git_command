import requests
import json
from tkinter import *
from tkinter.messagebox import  showinfo,showerror

def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params={
        'authorization':'zcQ4Kxvmglj6RGfokaZ5bPECTp3UO2Y0INHre7u8itnWVydBwLk9LJu0XBicHb73GKwUTSM26gFroOyl',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number

    }
    response=requests.get(url,params=params)
    dic=response.json()
    print(dic)
    return dic.get('return')


def btn_click():
        num=textNumber.get()
        msg=textMsg.get("1.0",END)
        r=send_sms(num,msg)
        if r==True:
            showinfo("send success","successfully sent")
        else:
            showerror("error","something went wrong..")

#creating GUI
root=Tk()
root.title('message sender')
root.geometry('400x550')
font=("Helvetica",22,"bold")

textNumber = Entry(root,font=font)
textNumber.pack(fill=X,pady=20)

textMsg=Text(root)
textMsg.pack(fill=X)

sendBtn=Button(root,text="send sms",command=btn_click)
sendBtn.pack()

root.mainloop()