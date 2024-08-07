import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

win = tk.Tk()
win.geometry("1200x600+0+0")
win.title("Contacts Management System")

#for title style and front
title_label=tk.Label(win,text="Contacts Managements System" ,font=("arial",25,"bold"),border=12,relief=tk.GROOVE,bg="blue",foreground='yellow')
title_label.pack(side=tk.TOP,fill=tk.X)

#for details entry block
detail_frame=tk.LabelFrame(win,text='Enter Details',font=("arial",15),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=400,height=500)

#for contact data show block
data_frame=tk.Frame(win,bd=12,bg='lightgrey',relief=tk.GROOVE)
data_frame.place(x=440,y=90,width=738,height=500)

#================================== Varaibles ================>
Firstname=tk.StringVar()
lastname=tk.StringVar()
email=tk.StringVar()
city=tk.StringVar()
contactno=tk.StringVar()
country=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()

search=tk.StringVar()




#==========entry the details==========>
#=====first name block
firstname_lbl=tk.Label(detail_frame,text='First Name',font=('arial',14),bg='lightgrey')
firstname_lbl.grid(row=0,column=0,padx=2,pady=2)

firstname_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=Firstname)
firstname_ent.grid(row=0,column=1,padx=2,pady=2)

#====== last name block
lastname_lbl=tk.Label(detail_frame,text='Last Name',font=('arial',14),bg='lightgrey')
lastname_lbl.grid(row=1,column=0,padx=2,pady=2)

lastname_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=lastname)
lastname_ent.grid(row=1,column=1,padx=2,pady=2)

#=========email block
email_lbl=tk.Label(detail_frame,text='Email',font=('arial',14),bg='lightgrey')
email_lbl.grid(row=2,column=0,padx=2,pady=2)

email_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=email)
email_ent.grid(row=2,column=1,padx=2,pady=2)

#=========city block
city_lbl=tk.Label(detail_frame,text='City',font=('arial',14),bg='lightgrey')
city_lbl.grid(row=3,column=0,padx=2,pady=2)

city_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=city)
city_ent.grid(row=3,column=1,padx=2,pady=2)

#========contact block
contact_lbl=tk.Label(detail_frame,text='Contact No',font=('arial',14),bg='lightgrey')
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=contactno)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

#=======country name
country_lbl=tk.Label(detail_frame,text='Country',font=('arial',14),bg='lightgrey')
country_lbl.grid(row=5,column=0,padx=2,pady=2)

country_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=country)
country_ent.grid(row=5,column=1,padx=2,pady=2)

#========address block
address_lbl=tk.Label(detail_frame,text='Address',font=('arial',14),bg='lightgrey')
address_lbl.grid(row=6,column=0,padx=2,pady=2)

address_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

#======Gender block
gender_lbl=tk.Label(detail_frame,text='Gender',font=('arial',14),bg='lightgrey')
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_frame,font=('arial',15),state='readonly',textvariable=gender)
gender_ent['values']=('Male','Female','Others')
gender_ent.grid(row=7,column=1,padx=2,pady=2)

#=======dob block
dob_lbl=tk.Label(detail_frame,text='DOB',font=('arial',14),bg='lightgrey')
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_frame,bd=5,font=("arial",14),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)

#============function block============>
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="contact_management")
    curr = conn.cursor()
    curr.execute("select *from contact_table")
    rows=curr.fetchall()
    if len(rows)!=0:
        contact_table.delete(*contact_table.get_children())
        for row in rows:
            contact_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

#===========add buttom function =========>>
def add_func():
    if Firstname.get() == "" or lastname.get() == "" or contactno.get() == "":
        messagebox.showerror("Error!","Please fill all the feild")
    else:
        conn=pymysql.connect(host="localhost",user="root",password="",database="contact_management")
        curr=conn.cursor()
        curr.execute("INSERT INTO contact_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Firstname.get(),lastname.get(),email.get(),city.get(),contactno.get(),country.get(),address.get(),gender.get(),dob.get()))

        conn.commit()
        conn.close()

        fetch_data()  #this will fetch the dada after adding and update
def get_cursor(event):
    cursor_row=contact_table.focus()
    content=contact_table.item(cursor_row)
    row=content['values']
    Firstname.set(row[0])
    lastname.set(row[1])
    email.set(row[2])
    city.set(row[3])
    contactno.set(row[4])
    country.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8]) 
#==================clear function block===========================
def clear():
    '''this is function will clear the entry boxes'''
        
    Firstname.set("")
    lastname.set("")
    email.set("")
    city.set("")
    contactno.set("")
    country.set("")
    address.set("")
    gender.set("")
    dob.set("") 

#===========================update function block===============

def update_func():
    ''' this function update the data '''
    conn=pymysql.connect(host="localhost",user="root",password="",database="contact_management")
    curr=conn.cursor()
    curr.execute("update contact_table set Firstname=%s,lastname=%s,email=%s,city=%s,country=%s,address=%s,gender=%s,dob=%s where contactno=%s",(Firstname.get(),lastname.get(),email.get(),city.get(),country.get(),address.get(),gender.get(),dob.get(),contactno.get()))
    conn.commit()
    fetch_data()
    conn.close()
    clear()

#====================delete function==============>

def delete_func():
    ''' This function deletes a record from the contact_table '''
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="contact_management")
        with conn.cursor() as curr:
            sql = "DELETE FROM contact_table WHERE contactno=%s"
            curr.execute(sql, (contactno.get(),))
            conn.commit()
            if curr.rowcount == 0:
                print("No record found with the given contact number.")
    
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")

    finally:
        conn.close()
    fetch_data()
    clear()

#=================sreaching by name=========>>>
def search_func():
    ''' This function searches for contacts based on user input in the search fields '''
    search_option = search.get()
    search_query = search_entry.get().strip()

    if not search_query:
        messagebox.showerror("Error", "Search field cannot be empty!")
        return

    # Mapping search options to corresponding column names
    column_mapping = {
        "First Name": "Firstname",
        "Last Name": "lastname",
        "Email": "email",
        "City": "city",
        "Contact No": "contactno",
        "Address": "address",
        "DOB": "dob",
        "Gender": "gender"
    }

    search_column = column_mapping.get(search_option)

    if not search_column:
        messagebox.showerror("Error", "Invalid search option!")
        return

    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="contact_management")
        with conn.cursor() as curr:
            # using wildfeild for seraching feilds
            sql = f"SELECT * FROM contact_table WHERE {search_column} LIKE %s"
            curr.execute(sql, ('%' + search_query + '%',))
            results = curr.fetchall()
            
            if results:
                contact_table.delete(*contact_table.get_children())
                for row in results:
                    contact_table.insert('', tk.END, values=row)
            else:
                messagebox.showinfo("Search Result", "No records found matching the query.")
    
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")

    finally:
        conn.close()


#========================show all data======================>
def show_all():
    ''' This function fetches and displays all records from the contact_table '''
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="contact_management")
        with conn.cursor() as curr:
            sql = "SELECT * FROM contact_table"
            curr.execute(sql)
            results = curr.fetchall()
            
            if results:
                contact_table.delete(*contact_table.get_children())
                for row in results:
                    contact_table.insert('', tk.END, values=row)
            else:
                contact_table.delete(*contact_table.get_children())
                messagebox.showinfo("Information", "No records found.")
    
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")

    finally:
        conn.close()




#=========buttoms frame========================>
btn_frame=tk.Frame(detail_frame,bg='lightgrey',bd=10,relief=tk.GROOVE)
btn_frame.place(x=12,y=345,width=352,height=110)

add_btn=tk.Button(btn_frame,bg="lightgrey",text="Add",bd=5,font=('arial',11),width=12,command=add_func)
add_btn.grid(row=0,column=0,padx=20,pady=5)

update_btn=tk.Button(btn_frame,bg="lightgrey",text="Update",bd=5,font=('arial',11),width=12,command=update_func)
update_btn.grid(row=0,column=1,padx=25,pady=5)

delete_btn=tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=5,font=('arial',11),width=12,command=delete_func)
delete_btn.grid(row=1,column=0,padx=20,pady=5)

clear_btn=tk.Button(btn_frame,bg="lightgrey",text="Clear",bd=5,font=('arial',11),width=12,command=clear)
clear_btn.grid(row=1,column=1,padx=25,pady=3)




#=========search buttoms block=======================>

search_frame=tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)
#for searching by text
search_lbl = tk.Label(search_frame, text="Search by", bg="lightgrey", font=('arial',10))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in=ttk.Combobox(search_frame,font=('arial',10),state="readonly",textvariable=search)
search_in['values']=("First Name","Last Name","Email","City","Contact No","Address","DOB","Gender")
search_in.grid(row=0,column=1,padx=10,pady=2)

search_btn = tk.Button(search_frame, text="Search", font=('arial', 10), bd=5, width=9, bg="lightgrey", command=search_func)
search_btn.grid(row=0, column=3, padx=11,pady=2)

search_entry = tk.Entry(search_frame, font=('arial', 13))
search_entry.grid(row=0, column=2, padx=10, pady=2)



#========================================================================================
showall_btn=tk.Button(search_frame,bg="lightgrey",text="Show All",bd=5,font=('arial',10),width=9,command=show_all)
showall_btn.grid(row=0,column=4,padx=0,pady=3)

#======================================================ends frame work

#===============start database work========>>>>>>>>>>>>>>>>>>>
main_frame=tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll= tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

contact_table=ttk.Treeview(main_frame,columns=("First Name","Last Name","Email","City","Contact No","Country","Address","Gender","DOB"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=contact_table.yview)
x_scroll.config(command=contact_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

contact_table.heading("First Name",text="First Name")
contact_table.heading("Last Name",text="Last Name")
contact_table.heading("Email",text="Email")
contact_table.heading("City",text="City")
contact_table.heading("Contact No",text="Contact No")
contact_table.heading("Country",text="Country")
contact_table.heading("Address",text="Address")
contact_table.heading("Gender",text="Gender")
contact_table.heading("DOB",text="DOB")

contact_table['show']='headings'

contact_table.column("First Name",width=100)
contact_table.column("Last Name",width=100)
contact_table.column("Email",width=100)
contact_table.column("City",width=100)
contact_table.column("Contact No",width=100)
contact_table.column("Country",width=100)
contact_table.column("Address",width=100)
contact_table.column("Gender",width=100)
contact_table.column("DOB",width=100)

contact_table.pack(fill=tk.BOTH,expand=True)

fetch_data()
contact_table.bind("<ButtonRelease-1>",get_cursor)
win.mainloop()


