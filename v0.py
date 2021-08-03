from tkinter import *
import webbrowser as op
import time as tt
import datetime

wi = Tk()
def cs():
    op.open('www.google.com')#<------ Paste class links here
    tt.sleep(3)
    wi.destroy()
    #l1.configure(text = 'aaa')
def en():
    op.open('www.google.com')
    tt.sleep(3)
    wi.destroy()
def ma():
    op.open('www.google.com')
    tt.sleep(3)
    wi.destroy()
def ch():
    op.open('www.google.com')
    tt.sleep(3)
    wi.destroy()
def ph():
    op.open('www.google.com')
    tt.sleep(3)
    wi.destroy()
da = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#Don't change anything here
#Date
c = datetime.datetime.now()
da2 = datetime.date.today()
date = (da2.strftime("%B-%d-%Y")) #B = Month, d = Day, Y = Year
day = datetime.date.today()
day = day.weekday()
day = da[day]
cday = (day,date)

#Time
h = (c.strftime("%H"))
m = (c.strftime("%M"))
h = int(h)
if h > 12:
    h =  h - 12
    z = 'PM'
else:
    z = 'AM'
time = (h, ":", m, z)

# Change colors here
gcol = 'black'  #Background 
tcol = 'white'  #Text
acol = 'purple' #Button
# 'red'/'orange'/'yellow'/'green'/'blue'/'purple'/'white'/'black' or use hex codes


wi.title("Zoom Classes")
wi.config(bg = gcol)
wi.geometry('500x300')
da = Label(wi, text = cday, fg = tcol, bg = gcol, font = 'Lato').place(x=20, y=15)
ti = Label(wi, text = time, fg = tcol, bg = gcol, font = 'Lato').place(x=400, y=15)
i = Label(wi, text = '',fg = 'white', bg = gcol, height = 3).pack()
csBtn = Button(wi, text = 'Computer Science', fg = tcol, bg = acol, command = cs).pack()
Label(wi, text = '', bg = gcol).pack()
phBtn = Button(wi, text = 'Physics', fg = tcol, bg = acol, command = ph).pack()
Label(wi, text = '', bg = gcol).pack()
maBtn = Button(wi, text = 'Maths', fg = tcol, bg = acol, command = ma).pack()
Label(wi, text = '', bg = gcol).pack()
enBtn = Button(wi, text = 'English', fg = tcol, bg = acol, command = en).pack()
Label(wi, text = '', bg = gcol).pack()
chBtn = Button(wi, text = 'Chemistry', fg = tcol, bg = acol, command = ch).pack()
l1 = Label(wi, text = '', bg = gcol).pack()

wi.mainloop()