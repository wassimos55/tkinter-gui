from tkinter import *
pro = Tk()
pro.geometry('400x400')
pro.title('ELITE Program')
def us():
    name =Label(pro, text='Your name is ' + inp1.get())
    name.place(x=100,y=240 )
    age =Label(pro, text='Your age is ' + inp2.get())
    age.place(x=100,y=260 )


title=Label(pro, text='First Elite DeskTop Program', bg='red', fg='white', font=('tajawal',17,'bold'))
title.pack(fill=X)
L1 = Label(pro, text='Enter Your Name :', font=('tajawal',14))
L1.pack()
inp1 = Entry(pro, width=30 , font=('tajawal',14), justify='center')
inp1.pack()
L2 = Label(pro, text='Enter Your Age :', font=('tajawal',14))
L2.pack()
inp2 = Entry(pro, width=30 , font=('tajawal',14), justify='center')
inp2.pack()
Btn = Button(pro, text='Add User', font=('tajawal',14),width=20, command=us)
Btn.place(x=100, y=180)
pro.mainloop()



#input()
#Entry()