from tkinter import *

key=0
root = Tk()

root.title("Cezar")

root.geometry("240x170")

def click_button_en():
    global key
    global fi
    global fo
    fi=open(put_in.get()+'.txt', mode='r')
    fo=open(put_in.get()+'_encrypt.txt', mode='w')
    key=int(message_entry.get())
    encrypt()
    fi.close()
    fo.close()
def click_button_de():
    global key
    global fi
    global fo
    fi=open(put_in.get()+'.txt', mode='r')
    fo=open(put_in.get()+'_decrypt.txt', mode='w')
    key=int(message_entry.get())
    decrypt()
    fi.close()
    fo.close()

label1 = Label(text="set key:")
label1.grid(row=2, column=0, ipadx=10, ipady=6, padx=0, pady=10)

message = StringVar() 
message_entry = Entry(textvariable=message)
message_entry.grid(row=2, column=1, ipadx=0, ipady=6, padx=0, pady=10)

labin = Label(text="file input:")
labin.grid(row=0, column=0, ipadx=10, ipady=6, padx=0, pady=10)
message = StringVar() 
put_in = Entry(textvariable=message)
put_in.grid(row=0, column=1, ipadx=0, ipady=6, padx=0, pady=10)

buten = StringVar()
buten.set("encrypt")

btn_en = Button(textvariable=buten,command=click_button_en)
btn_en.grid(row=3, column=0, ipadx=10, ipady=3, padx=15, pady=10)

butout = StringVar()
butout.set("decrypt")

btn_en = Button(textvariable=butout,command=click_button_de)
btn_en.grid(row=3, column=1, ipadx=10, ipady=3, padx=15, pady=10)
ens='abcdefghijklmnopqrstuvwxyz'
enb='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rub='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
sep='12345 67890-=!@#$%^&*()_+,./<>?""[]|'

def encrypt(): 
    for st in fi.readlines():                
        for i in st:
            if ens.find(i)!=-1:
                index = ens.find(i)
                fo.write(ens[(index+key)%26])
            if enb.find(i)!=-1: 
                index = enb.find(i)
                fo.write(enb[(index+key)%26])
            if rus.find(i)!=-1: 
                index = rus.find(i)
                fo.write(rus[(index+key)%33])
            if rub.find(i)!=-1: 
                index = rub.find(i)
                fo.write(rub[(index+key)%33])
            if sep.find(i)!=-1: 
                index = sep.find(i)
                fo.write(sep[(index+key)%36])
            if ord(i)==10:
                fo.write(chr(10+key-1))
            if ord(i)==13:
                fo.write(chr(13+key))
        st=str(fi.readline())

def decrypt():
   for st in fi.readlines():                
        for i in st:
            if ens.find(i)!=-1:
                index = ens.find(i)
                if index-key<0:index+=26
                fo.write(ens[(index-key)%26])
            if enb.find(i)!=-1: 
                index = enb.find(i)
                if index-key<0:index+=26
                fo.write(enb[(index-key)%26])
            if rus.find(i)!=-1: 
                index = rus.find(i)
                if index-key<0:index+=33
                fo.write(rus[(index-key)%33])
            if rub.find(i)!=-1: 
                index = rub.find(i)
                if index-key<0:index+=33
                fo.write(rub[(index-key)%33])
            if sep.find(i)!=-1: 
                index = sep.find(i)
                if index-key<0:index+=36
                fo.write(sep[(index-key)%36])
            if (ord(i)==10+key-1) :                
                fo.write(chr(ord(i)-key+1))
            if ord(i)==13+key:
                fo.write(chr(ord(i)-key))
        st=str(fi.readline())
root.mainloop()
