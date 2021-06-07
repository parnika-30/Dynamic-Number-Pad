from tkinter import * 
import random 
window = Tk()
window.geometry('500x500') 
xcoord=170
ycoord=150 
default_password="0987" 
string=""
v=StringVar() 
v.set(string) 
def change():
    randomlist=generaterandom() 
    btn_0['text']=randomlist[0] 
    btn_1['text']=randomlist[1] 
    btn_2['text']=randomlist[2] 
    btn_3['text']=randomlist[3] 
    btn_4['text']=randomlist[4] 
    btn_5['text']=randomlist[5] 
    btn_6['text']=randomlist[6] 
    btn_7['text']=randomlist[7] 
    btn_8['text']=randomlist[8] 
    btn_9['text']=randomlist[9] 
    global string 
    if(string==default_password):
        print("password matched")
    else:
        print("wrong password") 
    string=""
    v.set(string)

def generaterandom(): 
    list1=[]
    for i in range(100): 
        x=random.randint(0,9) 
        list1.append(str(x))
    list1 = list(dict.fromkeys(list1)) 
    return list1
def get1(): 
    global string
    string+=btn_1["text"] 
    v.set(string)
def get2(): 
    global string
    string+=btn_2["text"]   
    v.set(string)
def get3(): 
    global string
    string+=btn_3["text"] 
    v.set(string)

def get4(): 
    global string
    string+=btn_4["text"] 
    v.set(string)
def get5(): 
    global string
    string+=btn_5["text"] 
    v.set(string)
def get6(): 
    global string
    string+=btn_6["text"] 
    v.set(string)
def get7(): 
    global string
    string+=btn_7["text"] 
    v.set(string)
def get8(): 
    global string
    string+=btn_8["text"] 
    v.set(string)
def get9(): 
    global string
    string+=btn_9["text"] 
    v.set(string)

def get0(): 
    global string
    string+=btn_0["text"]
    v.set(string)   
def backspace(): 
    global string
    string=string[:-1] 
    v.set(string)

text = Entry(window, textvariable=v) 
text.place(x=xcoord+10,y=ycoord-70) 
text.config(state='readonly')

btn_1 = Button(window, text="1", command=get1) 
btn_1.place(x=xcoord, y=ycoord)
btn_1.config(height=3, width=5)
btn_2 = Button(window, text="2", command=get2) 
btn_2.place(x=xcoord+50, y=ycoord) 
btn_2.config(height=3, width=5)
btn_3 = Button(window, text="3", command=get3) 
btn_3.place(x=xcoord+100, y=ycoord) 
btn_3.config(height=3, width=5)
btn_4 = Button(window, text="4", command=get4) 
btn_4.place(x=xcoord, y=ycoord+70) 
btn_4.config(height=3, width=5)
btn_5 = Button(window, text="5", command=get5) 
btn_5.place(x=xcoord+50, y=ycoord+70) 
btn_5.config(height=3, width=5)

btn_6 = Button(window, text="6", command=get6) 
btn_6.place(x=xcoord+100, y=ycoord+70)
btn_6.config(height=3, width=5)

btn_7 = Button(window, text="7", command=get7) 
btn_7.place(x=xcoord, y=ycoord+140) 
btn_7.config(height=3, width=5)
btn_8 = Button(window, text="8", command=get8) 
btn_8.place(x=xcoord+50, y=ycoord+140) 
btn_8.config(height=3, width=5)
btn_9 = Button(window, text="9", command=get9) 
btn_9.place(x=xcoord+100, y=ycoord+140) 
btn_9.config(height=3, width=5)
btn_0 = Button(window, text="0", command=get0) 
btn_0.place(x=xcoord+50, y=ycoord+210) 
btn_0.config(height=3, width=5)
btn_bksp = Button(window, text="<-", command=backspace) 
btn_bksp.place(x=xcoord, y=ycoord+210) 
btn_bksp.config(height=3, width=5)
btn_ok = Button(window, text="->", command=change) 
btn_ok.place(x=xcoord+100, y=ycoord+210) 
btn_ok.config(height=3, width=5)
window.mainloop()