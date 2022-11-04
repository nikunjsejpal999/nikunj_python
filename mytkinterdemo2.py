from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_connection():
    return mysql.connector.connect(
            host="localhost", #ip address --> "127.0.0.1"#
            user="root",
            password="",
            database="python_mfw" 
         )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("insert status","all fields are mandatory")
    else:
        connection=create_connection()
        cursor=connection.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("insert status","data inserted successfully")

def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("search status","id is mandatory")
    else:
        connection=create_connection()
        cursor=connection.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("search status","id is invalid")
        connection.close()

def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("update status","all fields are mandatory")
    else:
        connection=create_connection()
        cursor=connection.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("update status","data updated successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("delete status","id is mandatory")
    else:
        connection=create_connection()
        cursor=connection.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        connection.commit()
        connection.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("delete status","data deleted successfully")
        
root=Tk()
root.title("REGISTRATION FORM")
root.geometry("350x400")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)


e_lname=Entry(root)
e_lname.place(x=150,y=150)


e_email=Entry(root)
e_email.place(x=150,y=200)


e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("impact",10),command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("impact",10),command=search_data)
search.place(x=107,y=300)


update=Button(root,text="UPDATE",bg="black",fg="white",font=("impact",10),command=update_data)
update.place(x=170,y=300)


delete=Button(root,text="DELETE",bg="black",fg="white",font=("impact",10),command=delete_data)
delete.place(x=230,y=300)



