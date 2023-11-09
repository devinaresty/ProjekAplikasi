from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('www.kiertytafood.com')
root.geometry('340x440')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    Username=user.get()
    Password=code.get()

    if Username=='devina' and Password=='123':
        screen=Toplevel(root)
        screen.title("www,kiertyta.com/menu")
        screen.geometry('340x440')
        screen.config(bg="white")

        Text(screen,text='Hello Everyone!',bg='black',font=('Calibiri(Boddy)',2,'bold')).pack(expand=True)

        screen.mainloop()

    elif Username=='nunez' and Password=='111':
        screen = Toplevel(root)
        screen.title("www,kiertyta.com/menu")
        screen.geometry('340x440')
        screen.config(bg="white")

    elif Username=='defari' and Password=='666':
        screen = Toplevel(root)
        screen.title("www,kiertyta.com/menu")
        screen.geometry('340x440')
        screen.config(bg="white")

    elif Username == 'anugrah' and Password == '333':
        screen = Toplevel(root)
        screen.title("www,kiertyta.com/menu")
        screen.geometry('340x440')
        screen.config(bg="white")

    else:
        screen = Toplevel(root)
        screen.title("www,kiertyta.com/menu")
        screen.geometry('340x440')
        screen.config(bg="red")


img = PhotoImage(file='logo1.png')
Label(root,image=img,bg='grey').place(x=115,y=55)

frame=Frame(root,width=210,height=210,bg="grey")
frame.place(x=68,y=195)

heading=Label(frame,text='Sign in',bg='grey',font=('Helvetica',18))
heading.place(x=66,y=2)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(1,'Username')



user = Entry(frame,width=25,fg='black',border=2,bg="white",font=('Microsoft Yamei UI Light',10))
user.place(x=16,y=44)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(1,'Password')


code = Entry(frame,width=25,fg='black',border=2,bg="white",font=('Microsoft Yamei UI Light',10))
code.place(x=16,y=88)
code.insert(0,'Password')
code.bind(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Button(frame,width=10,pady=7,text='Sign in',bg="white",border=2,command=signin).place(x=60,y=150)
Label=Label(frame,text="Don't have a account?",fg='black',bg='grey')
Label.place(x=15,y=120)

sign_up=Button(frame,width=6,text='sign up',border=0,fg='blue',bg='grey',cursor='hand2')
sign_up.place(x=140,y=120)

root.mainloop()