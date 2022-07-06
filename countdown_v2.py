from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
# import sys
# sys.setrecursionlimit(10000)

def countdown(client_date, msg, name):
    
    cntdown = client_date - datetime.now().replace(microsecond=0)
    lbl = Label(root, text=f"{name} Countdown: {cntdown}", fg='red', font=('arial', 15))
    lbl.grid(row=8, column=0)

    if cntdown == timedelta(0):
        messagebox.showinfo('countdown', msg)
        root.after(5000, root.destroy)
    else:
        root.after(1000, lambda: countdown(client_date, msg, name))


root = Tk()
root.title('countdown')


lbl_name = Label(root, text='enter the name for countdown: ')
entry_name = Entry(root)

lbl_year = Label(root, text='enter the year: ')
entry_year = Entry(root)

lbl_month = Label(root, text='enter the month: ')
entry_month = Entry(root)

lbl_day = Label(root, text='enter the day:  ')
entry_day = Entry(root)

lbl_hour = Label(root, text='enter the hour: ')
entry_hour = Entry(root)

lbl_min = Label(root, text='enter the minute: ')
entry_min = Entry(root)

lbl_msg = Label(root, text='enter the msg to display: ')
entry_msg = Entry(root)


lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)

lbl_year.grid(row=1, column=0)
entry_year.grid(row=1, column=1)

lbl_month.grid(row=2, column=0)
entry_month.grid(row=2, column=1)

lbl_day.grid(row=3, column=0)
entry_day.grid(row=3, column=1)

lbl_hour.grid(row=4, column=0)
entry_hour.grid(row=4, column=1)

lbl_min.grid(row=5, column=0)
entry_min.grid(row=5, column=1)

lbl_msg.grid(row=6, column=0)
entry_msg.grid(row=6, column=1)


def btn_click():
    year = int(entry_year.get())
    month = int(entry_month.get())
    day = int(entry_day.get())
    hour = int(entry_hour.get())
    minute = int(entry_min.get())
    msg = entry_msg.get()
    name = entry_name.get()

    client_date = datetime(year=year, month=month, day=day, hour=hour, minute=minute)

    countdown(client_date, msg, name)



btn = Button(root, text='submit', command=btn_click)
btn.grid(row=7, column=1)

root.mainloop()

# todo
# better gui
# control variables