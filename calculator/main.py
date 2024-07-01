<<<<<<< HEAD
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice (1/2/3/4): ")
        if choice in operations:
            return operations[choice], choice
        else:
            print("Invalid choice! Please select a valid operation.")

def main():
    print("Welcome to the Simple Calculator!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation, op_choice = get_operation()
    
    result = operation(num1, num2)
    
    operation_names = {'1': 'Addition', '2': 'Subtraction', '3': 'Multiplication', '4': 'Division'}
    print(f"{operation_names[op_choice]} of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
=======
import tkinter
from tkinter import *
root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable (False, False)
task_list=[]
def addTask():
    task = task_entry.get()
    task_entry.delete(0,  END)

    if task:
        with open("tasklist.txt","a") as taskfile:
              taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END,task)

def deleteTask():
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(  ANCHOR)
def openTaskFile():


    try:
         global task_list
         with open("tasklist.txt","r") as taskfile:
               tasks=taskfile.readlines()
               
         for task in tasks:
              if task  !='\n':
                 task_list.append(task)
                 listbox.insert(END ,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
    
#icon
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto (False, Image_icon)
#topbar
TopImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="Image/dock.png")
Label (root, image=dockImage, bg="#32405b").place(x=30,y=25)

noteimage=PhotoImage(file="image/task.png")
Label(root,image=noteimage,bg="#32405b").place(x=340,y=25)

heading=Label(root,text="Task",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)
#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)


#listbox
frame1=Frame(root,bd=3,width=700,height=200,bg="#32405b")
frame1.pack(pady=(160,0))


listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


#delete
Delete_icon=PhotoImage(file="image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)










root.mainloop()
>>>>>>> e47e74604e72bdb5c037670264977cd46e215b0c
