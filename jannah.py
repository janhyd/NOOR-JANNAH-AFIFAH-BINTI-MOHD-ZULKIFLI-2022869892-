import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


#  Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jannah"
)

mycursor = mydb.cursor()

def enter_data():
    accepted_value = accept_var.get()

    if accepted_value == "Accepted":
        # Customer Information
        catowner = owner_cat_name_entry.get()
        catname = cat_name_entry.get()

        if catowner and catname:
            age = cat_age_Spinbox.get()
            staffincharge = staff_incharge_entry.get()

            # Inserting data into a table
            sql = "INSERT INTO cat_boarding_registration (catowner, catname, age, staffincharge) VALUES (%s, %s, %s, %s)"
            val = (catowner, catname, age, staffincharge)
            mycursor.execute(sql, val)
            mydb.commit()

            print("Owner Cat Name: ", catowner, "Cat Name: ", catname)
            print("Cat Age: ", age, "Staff Incharge: ", staffincharge)
            print("------------------------------------------")
        else:
            tk.messagebox.showwarning(title="Error", message="Owner Cat Name and Cat Name are required.")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms")



    if accepted_value == "Accepted":
        # ... (rest of your code)
        package_type = package_type_var.get()
        day_count = day_type_menva.get()

        p_prices = {"Gold": 50, "Platinum": 100, "Diamond": 150}
        d_prices = {"Day 1": 20, "Day 2": 40, "Day 3": 60, "Day 4": 80, "Day 5": 100}

        # Inserting data into a table
        sql = "INSERT INTO cat_boarding_registration (package_type, day_count) VALUES (%s, %s)"
        val = (package_type,day_count)
        mycursor.execute(sql,val)
        mydb.commit()

        total_price = p_prices.get(package_type, 0) + d_prices.get(day_count, 0)
        price_label.config(text=f"Price: RM {total_price:.2f}")

        # Inserting data into a table
        sql = "INSERT INTO cat_boarding_registration (total_price) VALUES (%s)"
        val = (total_price,)
        mycursor.execute(sql,val)
        mydb.commit()

        print(f"Total Price: {total_price}")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms")


root=tk.Tk()
root.title("cat boarding registration",)
root.geometry("500x500")
root.configure(bg="#837E7C")

label_name = tk.Label(root,text="CAT BOARDING REGISTRATION",font=('Arial bold',11),bg="#A9A9A9")
label_name.pack(padx=0, pady=0)

frame = tk.Frame(root)
frame.pack()

# entering information
 
customer_frame = tk.LabelFrame(frame, text="CUSTOMER INFORMATION",font=('book mania',9),bg="#87AFC7")
customer_frame.grid(row=0, column=0)

owner_cat_name = tk.Label(customer_frame, text="Owner Name:",font=('capita',9),bg="lightblue")
owner_cat_name.grid(row=0, column=1)
owner_cat_name_entry = tk.Entry(customer_frame,bg="#D5D6EA")
owner_cat_name_entry.grid(row=1, column=1)

cat_name_label = tk.Label(customer_frame, text="Cat Name:",font=('capita',9),bg="lightblue")
cat_name_label.grid(row=0, column=2)
cat_name_entry = tk.Entry(customer_frame,bg="#D5D6EA")
cat_name_entry.grid(row=1, column=2)

cat_age=tk.Label(customer_frame, text="Cat Age",font=('capita',9),bg="lightblue")
cat_age.grid(row=2,column=1)
cat_age_Spinbox=tk.Spinbox(customer_frame,from_=0,to=50,bg="#D5D6EA")
cat_age_Spinbox.grid(row=3,column=1)

staff_incharge_label=tk.Label(customer_frame,text="Staff Incharge:",font=('capita',9),bg="lightblue")
staff_incharge_label.grid(row=2,column=2)
staff_incharge_entry=tk.Entry(customer_frame,bg="#D5D6EA")
staff_incharge_entry.grid(row=3,column=2)

for widget in customer_frame.winfo_children():
    widget.grid_configure(padx=20,pady=5)

#package frame
package_type_label=tk.Label(root,text="Select cat package:",font=('book mania',9),bg="#C2E5D3")
package_type_label.pack(padx=10,pady=5)

package_type_var=tk.StringVar(root)
package_type_var.set("Select Package")
package_type_pac=tk.OptionMenu(root,package_type_var,"Gold","Platinum","Diamond")
package_type_pac.pack(padx=10,pady=5)

day_type_menva=tk.StringVar(root)
day_type_menva.set("Select Days")
day_type_menva_menu=tk.OptionMenu(root,day_type_menva,"Day 1","Day 2","Day 3","Day 4","Day 5")
day_type_menva_menu.pack(padx=10,pady=5)

for widget in package_type_label.winfo_children():
    widget.grid_configure(padx=20,pady=5)

price_label=tk.Label(root,text="Price:RM0.00",font=('book mania',9),bg="#C2E5D3" )
price_label.pack(pady=10)

#Accept terms

terms_frame = tk.LabelFrame(frame, text="Terms & Conditions",font=('book mania',9),bg="#E6E6FA")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.",font=('capita',9),bg="#DBE9FA",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=20,pady=5)

#Button
button = tk.Button(frame, text="Enter data", command= enter_data,font=('capita',9),bg="#C2E5D3")
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)


root.mainloop() 