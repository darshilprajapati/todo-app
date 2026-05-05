import tkinter as TK
from tkinter import messagebox as tb
import random

root=TK.Tk()

root.configure(bg="white")
root.title("To-Do-List using ui")
root.geometry("250x220")

tasks=[]

def update_task():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)
    pass

def update():
    task=lb_tasks.get("active")
    newtask=txt_input.get()
    if task in tasks:
        i=tasks.index(task)
        tasks[i]=newtask
    update_task()

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
     task= txt_input.get()
     if task !="":
        tasks.append(task)
        update_task()
     else:
        tb.showwarning("Warning","You need to enter a task")

def delete_task():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_task()
    
def deleteall_task():
    confirmed=tb.askyesno("Please confirm","Do you really want to delete all")
    if confirmed==True:
        global tasks
        tasks=[]
        update_task()

def number_of_task():
    number_of_task=len(tasks)
    msg="Number of tasks:%s"%number_of_task
    lbl_display["text"]=msg

lbl_display=TK.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

def fade():
    colors = ["red", "orange", "green", "blue", "purple"]
    current_color = lbl_title.cget("fg")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    lbl_title.config(fg=next_color)
    root.after(500, fade)

lbl_title=TK.Label(root,text="To-Do-List",fg="red",background="white",relief="groove",font=("calibri",14,"bold"))
lbl_title.grid(row=0,column=0)

fade()

txt_input=TK.Entry(root,width=20)
txt_input.grid(row=1,column=1)

btn_add=TK.Button(root,text="ADD TASK",relief="raised",fg="black",bg="light blue",command=add_task,width=14)
btn_add.grid(row=1,column=0)

btn_update=TK.Button(root,text="UPDATE",fg="black",bg="light blue",command=update,width=14)
btn_update.grid(row=2,column=0)

btn_delete=TK.Button(root,text="DELETE",fg="black",bg="light blue",command=delete_task,width=14)
btn_delete.grid(row=3,column=0)

btn_deleteall=TK.Button(root,text="DELETE ALL",fg="black",bg="light blue",command=deleteall_task,width=14)
btn_deleteall.grid(row=4,column=0)

btn_number_of=TK.Button(root,text="NUMBER OF TASKS",fg="black",bg="light blue",command=number_of_task,width=14)
btn_number_of.grid(row=5,column=0)

btn_exit=TK.Button(root,text="EXIT",fg="black",bg="light blue",command=exit,width=14)
btn_exit.grid(row=6,column=0)

lb_tasks=TK.Listbox()
lb_tasks.grid(row=2,column=1,rowspan=5)

root.mainloop()