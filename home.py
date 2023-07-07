import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "bloodbank"
)

def inventory_details():
    
    cursor = db.cursor(buffered = True)

    def search_inventory():
        # Fetch attribute values from the entry fields
        id = id_entry.get()
        date_stored = date_stored_entry.get()
        expiry_date = expiry_date_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        storage_location = storage_location_entry.get()
        status = status_entry.get()
        donor_id = donor_id_entry.get()
        blood_group = blood_group_entry.get()
        component = component_entry.get()

        # Execute the SQL query to search for inventory data based on attribute values
        sql = "SELECT * FROM Inventory_View WHERE "
        values = []

        if donor_id:
            sql += "Donor_ID = %s AND "
            values.append(donor_id)
        if blood_group:
            sql += "Blood_ID = %s AND "
            values.append(blood_group)
        if component:
            sql += "Component = %s AND "
            values.append(component)
        if date_stored:
            sql += "Date_Stored = %s AND "
            values.append(date_stored)
        if expiry_date:
            sql += "Expiry_date = %s AND "
            values.append(expiry_date)
        if id:
            sql += "ID = %s AND "
            values.append(id)
        if price:
            sql += "price = %s AND "
            values.append(price)
        if quantity:
            sql += "quantity = %s AND "
            values.append(quantity)
        if storage_location:
            sql += "Storage_Location = %s AND "
            values.append(storage_location)
        if status:
            sql += "status = %s AND "
            values.append(status)
        # Remove the trailing "AND" from the SQL query
        if sql.endswith("AND "):
            sql = sql[:-4]

        cursor.execute(sql, tuple(values))
        results = cursor.fetchall()

        # Clear the treeview
        tree.delete(*tree.get_children())

        for result in results:
            tree.insert("", "end", values = result)


    # Create a function to view donor details
    def view_inventory():
        # Clear treeview
        tree.delete(*tree.get_children())

        # Fetch donor details from database
        cursor.execute("SELECT * FROM Inventory_View")
        inventory = cursor.fetchall()

        # Insert donor details into treeview
        for unit in inventory:
            tree.insert('', 'end', values=unit)

    # Create a function to update donor details
    def update_inventory():
        # Get selected item from treeview
        selected_item = tree.selection()
        if selected_item:
            # Get donor details from selected item
            unit = tree.item(selected_item)['values']

            # Create a top-level window for updating donor details
            update_window = tk.Toplevel(root)
            update_window.title("Update Inventory")
            update_window.geometry("300x370")

            # Create a frame for update form
            update_frame = ttk.LabelFrame(update_window, text="Update Unit Details")
            update_frame.pack(pady=10, padx=10)

            # Create labels and entry fields for donor details

            date_stored_label = ttk.Label(update_frame, text="Date Stored:")
            date_stored_label.grid(row=0, column=0, padx=5, pady=4)
            date_stored_entry = ttk.Entry(update_frame)
            date_stored_entry.grid(row=0, column=1, padx=5, pady=4)
            date_stored_entry.insert(0, unit[1])  # Pre-fill date stored entry field with current date_stored

            expiry_date_label = ttk.Label(update_frame, text="Expiry Date:")
            expiry_date_label.grid(row=1, column=0, padx=5, pady=4)
            expiry_date_entry = ttk.Entry(update_frame)
            expiry_date_entry.grid(row=1, column=1, padx=5, pady=4)
            expiry_date_entry.insert(0, unit[2])  # Pre-fill expiry date entry field with current expiry_date

            price_label = ttk.Label(update_frame, text="Price:")
            price_label.grid(row=3, column=0, padx=5, pady=4)
            price_entry = ttk.Entry(update_frame)
            price_entry.grid(row=3, column=1, padx=5, pady=4)
            price_entry.insert(0, unit[3])  # Pre-fill price entry field with current price

            quantity_label = ttk.Label(update_frame, text="Quantity:")
            quantity_label.grid(row=4, column=0, padx=5, pady=4)
            quantity_entry = ttk.Entry(update_frame)
            quantity_entry.grid(row=4, column=1, padx=5, pady=4)
            quantity_entry.insert(0, unit[4])  # Pre-fill quantity entry field with current quantity

            storage_location_label = ttk.Label(update_frame, text="Storage Location:")
            storage_location_label.grid(row=5, column=0, padx=5, pady=4)
            storage_location_entry = ttk.Entry(update_frame)
            storage_location_entry.grid(row=5, column=1, padx=5, pady=4)
            storage_location_entry.insert(0, unit[5]) # Pre-fill storage location field with current storage location

            status_label = ttk.Label(update_frame, text="Status:")
            status_label.grid(row=6, column=0, padx=5, pady=4)
            status_entry = ttk.Entry(update_frame)
            status_entry.grid(row=6, column=1, padx=5, pady=4)
            status_entry.insert(0, unit[6])

            donor_ID_label = ttk.Label(update_frame, text="Donor ID:")
            donor_ID_label.grid(row=7, column=0, padx=5, pady=4)
            donor_ID_entry = ttk.Entry(update_frame)
            donor_ID_entry.grid(row=7, column=1, padx=5, pady=4)
            donor_ID_entry.insert(0, unit[7]) # Pre-fill donor ID field with current donor ID

            blood_group_label = ttk.Label(update_frame, text="Blood Group:")
            blood_group_label.grid(row=8, column=0, padx=5, pady=4)
            blood_group_entry = ttk.Entry(update_frame)
            blood_group_entry.grid(row=8, column=1, padx=5, pady=4)
            blood_group_entry.insert(0, unit[8]) # Pre-fill blood group field with current blood group

            component_label = ttk.Label(update_frame, text="Component:")
            component_label.grid(row=9, column=0, padx=5, pady=4)
            component_entry = ttk.Entry(update_frame)
            component_entry.grid(row=9, column=1, padx=5, pady=4)
            component_entry.insert(0, unit[9]) # Pre-fill component field with current component

            # Create a function to update donor details in database
            def save_update():
                # Get updated donor details from entry fields
                updated_date_stored = date_stored_entry.get()
                updated_expiry_date = expiry_date_entry.get()
                updated_price = price_entry.get()
                updated_quantity = quantity_entry.get()
                updated_storage_location = storage_location_entry.get()
                updated_status = status_entry.get()
                updated_donor_ID = donor_ID_entry.get()
                updated_blood_group = blood_group_entry.get()
                updated_component = component_entry.get()

                cursor.execute("SELECT Blood_ID from Blood_Component WHERE blood_group = %s AND component = %s",
                               (updated_blood_group, updated_component)) # get new donor ID from new blood group and component

                blood_ID = cursor.fetchone()
                updated_blood_ID = blood_ID[0]
                
                # Update inventory in database
                cursor.execute("UPDATE Inventory SET date_stored = %s, expiry_date=%s, price = %s, quantity = %s, storage_location = %s, status = %s, donor_ID = %s, blood_ID = %s WHERE ID = %s",
                            (updated_date_stored, updated_expiry_date, updated_price, updated_quantity, updated_storage_location, updated_status, updated_donor_ID, updated_blood_ID, unit[0]))
                db.commit()

                # Close update window and refresh donor details
                update_window.destroy()

            # Create a save button to update donor details
            save_button = ttk.Button(update_frame, text="Save", command=save_update)
            save_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        else:
            # Show error message if no donor is selected
            tk.messagebox.showerror("Error", "Please select a unit to update.")

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Donor Management System")
    root.geometry("800x710")

    search_frame = ttk.LabelFrame(root, text="Search Inventory")
    search_frame.pack(pady=10, padx=10)

    # Create entry fields for search options
    date_stored_label = ttk.Label(search_frame, text="Date Stored:")
    date_stored_label.grid(row=0, column=0, padx=5, pady=5)
    date_stored_entry = ttk.Entry(search_frame)
    date_stored_entry.grid(row=0, column=1, padx=5, pady=5)

    expiry_date_label = ttk.Label(search_frame, text="Expiry Date:")
    expiry_date_label.grid(row=1, column=0, padx=5, pady=5)
    expiry_date_entry = ttk.Entry(search_frame)
    expiry_date_entry.grid(row=1, column=1, padx=5, pady=5)

    id_label = ttk.Label(search_frame, text="ID:")
    id_label.grid(row=2, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(search_frame)
    id_entry.grid(row=2, column=1, padx=5, pady=5)

    price_label = ttk.Label(search_frame, text="Price:")

    price_label.grid(row=3, column=0, padx=5, pady=5)
    price_entry = ttk.Entry(search_frame)
    price_entry.grid(row=3, column=1, padx=5, pady=5)

    quantity_label = ttk.Label(search_frame, text="Quantity:")
    quantity_label.grid(row=4, column=0, padx=5, pady=5)
    quantity_entry = ttk.Entry(search_frame)
    quantity_entry.grid(row=4, column=1, padx=5, pady=5)

    storage_location_label = ttk.Label(search_frame, text="Storage Location:")
    storage_location_label.grid(row=5, column=0, padx=5, pady=5)
    storage_location_entry = ttk.Entry(search_frame)
    storage_location_entry.grid(row=5, column=1, padx=5, pady=5)

    status_label = ttk.Label(search_frame, text="Status:")
    status_label.grid(row=6, column=0, padx=5, pady=5)
    status_entry = ttk.Entry(search_frame)
    status_entry.grid(row=6, column=1, padx=5, pady=5)

    donor_id_label = ttk.Label(search_frame, text="Donor ID:")
    donor_id_label.grid(row=7, column=0, padx=5, pady=5)
    donor_id_entry = ttk.Entry(search_frame)
    donor_id_entry.grid(row=7, column=1, padx=5, pady=5)

    blood_group_label = ttk.Label(search_frame, text="Blood Group:")
    blood_group_label.grid(row=8, column=0, padx=5, pady=5)
    blood_group_entry = ttk.Entry(search_frame)
    blood_group_entry.grid(row=8, column=1, padx=5, pady=5)

    component_label = ttk.Label(search_frame, text="Component:")
    component_label.grid(row=9, column=0, padx=5, pady=5)
    component_entry = ttk.Entry(search_frame)
    component_entry.grid(row=9, column=1, padx=5, pady=5)

    # Create a search button
    search_button = ttk.Button(search_frame, text="Search", command=search_inventory)
    search_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

    # Create a treeview to display donor details
    tree = ttk.Treeview(root, columns=("Date Stored", "Expiry Date", "ID", "Price", "Quantity", "Storage Location", "Status", "Donor ID", "Blood Group", "Component"))
    tree.heading("Date Stored", text="Date Stored")
    tree.heading("Expiry Date", text="Expiry Date")
    tree.heading("ID", text="ID")
    tree.heading("Price", text="Price")
    tree.heading("Quantity", text = "Quantity")
    tree.heading("Storage Location", text = "Storage Location")
    tree.heading("Status", text="Status")
    tree.heading("Donor ID", text="Donor ID")
    tree.heading("Blood Group", text="Blood Group")
    tree.heading("Component", text="Component")
    tree.pack(pady=8, padx=10)

    # Create buttons for view and update options
    view_button = ttk.Button(root, text="View Inventory", command=view_inventory)
    view_button.pack(pady=5)

    update_button = ttk.Button(root, text="Update Inventory", command=update_inventory)
    update_button.pack(pady=5)

    # Create a function to close the database connection and exit the application
    def close_app():
        cursor.close()
        root.destroy()

    # Create an exit button to close the application
    exit_button = ttk.Button(root, text="Exit", command=close_app)
    exit_button.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

def take_blood():

    mycursor = db.cursor()

    # Create the GUI window
    window = Tk()
    window.title("Add New Blood Unit")
    
    # Create the labels and entry fields for the GUI
    donor_id_label = Label(window, text="Donor ID:")
    donor_id_label.grid(row=0, column=0, padx = 5, pady = 5)
    donor_id_entry = Entry(window)
    donor_id_entry.grid(row=0, column=1, padx = 10, pady = 5)

    blood_id_label = Label(window, text="Blood ID:")
    blood_id_label.grid(row=1, column=0, padx = 5, pady = 5)
    blood_id_entry = Entry(window)
    blood_id_entry.grid(row=1, column=1, padx = 10, pady = 5)

    quantity_label = Label(window, text="Quantity:")
    quantity_label.grid(row=2, column=0, padx = 5, pady = 5)
    quantity_entry = Entry(window)
    quantity_entry.grid(row=2, column=1, padx = 10, pady = 5)

    price_label = Label(window, text="Price:")
    price_label.grid(row=3, column=0, padx = 5, pady = 5)
    price_entry = Entry(window)
    price_entry.grid(row=3, column=1, padx = 10, pady = 5)

    storage_location_label = Label(window, text="Storage Location:")
    storage_location_label.grid(row=4, column=0, padx = 5, pady = 5)
    storage_location_entry = Entry(window)
    storage_location_entry.grid(row=4, column=1, padx = 10, pady = 5)

    # Create a function to add the new blood unit to the inventory
    def add_blood_unit():
        donor_id = donor_id_entry.get()
        blood_id = blood_id_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()
        storage_location = storage_location_entry.get()
        
        # Check if the donor exists in the database
        mycursor.execute("SELECT * FROM Donor WHERE Donor_ID = %s", (donor_id,))
        donor = mycursor.fetchone()
        if donor is None:
            messagebox.showerror("Error", "Donor ID not found.")
            return
        
        # Check if the blood component exists in the database
        mycursor.execute("SELECT * FROM Blood_Component WHERE Blood_ID = %s", (blood_id,))
        blood_component = mycursor.fetchone()
        if blood_component is None:
            messagebox.showerror("Error", "Blood ID not found.")
            return
        
        # Automatically generate the next sequential ID
        mycursor.execute("SELECT MAX(ID) FROM Inventory")
        max_id = mycursor.fetchone()[0]
        next_id = 'I001' if max_id is None else 'I{:03d}'.format(int(max_id[1:]) + 1)
        
        # Insert the new blood unit into the inventory
        sql = "INSERT INTO Inventory (Date_Stored, Expiry_date, ID, Price, Quantity, Storage_Location, Status, Donor_ID, Blood_ID) VALUES (CURDATE(), DATE_ADD(CURDATE(), INTERVAL 42 DAY), %s, %s, %s, %s, %s, %s, %s)"
        val = (next_id, price, quantity, storage_location, "Available", donor_id, blood_id)
        mycursor.execute(sql, val)
        db.commit()
        
        messagebox.showinfo("Success", "Blood unit added to inventory.")
        blood_id_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        storage_location_entry.delete(0, END)


    # Create a button to add the new blood unit to the inventory
    add_button = Button(window, text="Add Blood Unit", command=add_blood_unit)
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

    # run the main loop
    window.mainloop()

    mycursor.close()

def add_donor():

    # create cursor object
    mycursor = db.cursor()

    # get the current maximum donor ID and increment it to get the next sequential ID
    mycursor.execute("SELECT MAX(Donor_ID) FROM Donor")
    max_id = mycursor.fetchone()[0]
    next_id = 'D001' if max_id is None else 'D{:03d}'.format(int(max_id[1:]) + 1)

    # function to insert a new donor into the database
    def add():
        # get the values from the input fields
        blood_group = blood_group_input.get()
        name = name_input.get()
        medical_history = medical_history_input.get()
        age = age_input.get()
        address = address_input.get()

        # insert the new donor into the database
        sql = "INSERT INTO Donor (Donor_ID, Blood_Group, Name, Medical_History, Age, Address) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (next_id, blood_group, name, medical_history, age, address)
        mycursor.execute(sql, val)
        db.commit()

        # display the new donor's ID
        message_label.config(text="New donor created with ID: {}".format(next_id))

    # create the GUI
    window = Tk()
    window.title("Blood Bank")
    window.geometry("400x300")

    # create lables and input boxes for each field
    blood_group_label = Label(window, text="Blood Group")
    blood_group_label.grid(column=0, row=0)

    blood_group_input = Entry(window)
    blood_group_input.grid(column=1, row=0, padx = 5, pady = 5)

    name_label = Label(window, text="Name")
    name_label.grid(column=0, row=1)

    name_input = Entry(window)
    name_input.grid(column=1, row=1, padx = 5, pady = 5)

    medical_history_label = Label(window, text="Medical History")
    medical_history_label.grid(column=0, row=2)

    medical_history_input = Entry(window)
    medical_history_input.grid(column=1, row=2, padx = 5, pady = 5)

    age_label = Label(window, text="Age")
    age_label.grid(column=0, row=3)

    age_input = Entry(window)
    age_input.grid(column=1, row=3, padx = 5, pady = 5)

    address_label = Label(window, text="Address")
    address_label.grid(column=0, row=4)

    address_input = Entry(window)
    address_input.grid(column=1, row=4, padx = 5, pady = 5)

    add_button = Button(window, text="Add Donor", command=add)
    add_button.grid(column=0, row=5)

    message_label = Label(window, text="")
    message_label.grid(column=1, row=5)

    window.mainloop()

    #close the cursor object
    mycursor.close()

def donor_details():

    #create a new cursor object
    cursor = db.cursor()

    def search_donor():
        # Fetch attribute values from the entry fields
        name = name_entry.get()
        donor_ID = donor_ID_entry.get()
        address = address_entry.get()
        age = age_entry.get()
        blood_group = blood_group_entry.get()
        medical_history = medical_history_entry.get()

        # Execute the SQL query to search for inventory data based on attribute values
        sql = "SELECT * FROM Donor WHERE "
        values = []
        if name:
            sql += "Name = %s AND "
            values.append(name)
        if donor_ID:
            sql += "Donor_ID = %s AND "
            values.append(donor_ID)
        if address:
            sql += "address = %s AND "
            values.append(address)
        if age:
            sql += "age = %s AND "
            values.append(age)
        if blood_group:
            sql += "Blood_Group = %s AND "
            values.append(blood_group)
        if medical_history:
            sql += "Medical_History = %s AND "
            values.append(medical_history)
        
        # Remove the trailing "AND" from the SQL query
        if sql.endswith("AND "):
            sql = sql[:-4]

        cursor.execute(sql, tuple(values))
        results = cursor.fetchall()

        # Clear the treeview
        tree.delete(*tree.get_children())

        # insert rows in the treeview
        for result in results:
            tree.insert("", "end", values = result)


    # Create a function to view donor details
    def view_donor():
        # Clear treeview
        tree.delete(*tree.get_children())

        # Fetch donor details from database
        cursor.execute("SELECT * FROM Donor")
        inventory = cursor.fetchall()

        # Insert donor details into treeview
        for unit in inventory:
            tree.insert('', 'end', values=unit)

    # Create a function to update donor details
    def update_donor():
        # Get selected item from treeview
        selected_item = tree.selection()
        if selected_item:
            # Get donor details from selected item
            donor = tree.item(selected_item)['values']

            # Create a top-level window for updating donor details
            update_window = tk.Toplevel(root)
            update_window.title("Update Donor")
            update_window.geometry("300x300")

            # Create a frame for update form
            update_frame = ttk.LabelFrame(update_window, text="Update Donor Details")
            update_frame.pack(pady=10, padx=10)

            # Create labels and entry fields for donor details

            blood_group_label = ttk.Label(update_frame, text="Blood Group:")
            blood_group_label.grid(row=1, column=0, padx=5, pady=4)
            blood_group_entry = ttk.Entry(update_frame)
            blood_group_entry.grid(row=1, column=1, padx=5, pady=4)
            blood_group_entry.insert(0, donor[1]) # Pre-fill blood group entry field with current blood group

            name_label = ttk.Label(update_frame, text="Name:")
            name_label.grid(row=2, column=0, padx=5, pady=4)
            name_entry = ttk.Entry(update_frame)
            name_entry.grid(row=2, column=1, padx=5, pady=4)
            name_entry.insert(0, donor[2])  # Pre-fill name entry field with current name

            medical_history_label = ttk.Label(update_frame, text="Medical History:")
            medical_history_label.grid(row=3, column=0, padx=5, pady=4)
            medical_history_entry = ttk.Entry(update_frame)
            medical_history_entry.grid(row=3, column=1, padx=5, pady=4)
            medical_history_entry.insert(0, donor[3]) # Pre-fill medical history entry field with current medical history

            age_label = ttk.Label(update_frame, text="Age:")
            age_label.grid(row=4, column=0, padx=5, pady=4)
            age_entry = ttk.Entry(update_frame)
            age_entry.grid(row=4, column=1, padx=5, pady=4)
            age_entry.insert(0, donor[4]) # Pre-fill age entry field with current age

            address_label = ttk.Label(update_frame, text="Address:")
            address_label.grid(row=5, column=0, padx=5, pady=4)
            address_entry = ttk.Entry(update_frame)
            address_entry.grid(row=5, column=1, padx=5, pady=4)
            address_entry.insert(0, donor[5])  # Pre-fill address entry field with current address


            # Create a function to update donor details in database
            def save_update():
                # Get updated donor details from entry fields
                updated_name = name_entry.get()
                updated_address = address_entry.get()
                updated_age = age_entry.get()
                updated_blood_group = blood_group_entry.get()
                updated_medical_history = medical_history_entry.get()

                # Update donor details in database
                cursor.execute("UPDATE Donor SET name = %s, address = %s, age = %s, blood_group = %s, medical_history = %s WHERE Donor_ID = %s",
                            (updated_name, updated_address, updated_age, updated_blood_group, updated_medical_history, donor[0]))
                db.commit()

                # Close update window and refresh donor details
                update_window.destroy()

            # Create a save button to update donor details
            save_button = ttk.Button(update_frame, text="Save", command=save_update)
            save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        else:
            # Show error message if no donor is selected
            tk.messagebox.showerror("Error", "Please select a unit to update.")

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("IDonor Details")
    root.geometry("800x620")

    search_frame = ttk.LabelFrame(root, text="Search Donor")
    search_frame.pack(pady=10, padx=10)

    # Create entry fields for search options
    name_label = ttk.Label(search_frame, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(search_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    donor_ID_label = ttk.Label(search_frame, text="Donor ID:")
    donor_ID_label.grid(row=1, column=0, padx=5, pady=5)
    donor_ID_entry = ttk.Entry(search_frame)
    donor_ID_entry.grid(row=1, column=1, padx=5, pady=5)

    address_label = ttk.Label(search_frame, text="Address:")
    address_label.grid(row=2, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(search_frame)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    age_label = ttk.Label(search_frame, text="Age:")
    age_label.grid(row=3, column=0, padx=5, pady=5)
    age_entry = ttk.Entry(search_frame)
    age_entry.grid(row=3, column=1, padx=5, pady=5)

    blood_group_label = ttk.Label(search_frame, text="Blood Group:")
    blood_group_label.grid(row=4, column=0, padx=5, pady=5)
    blood_group_entry = ttk.Entry(search_frame)
    blood_group_entry.grid(row=4, column=1, padx=5, pady=5)

    medical_history_label = ttk.Label(search_frame, text="Medical History:")
    medical_history_label.grid(row=5, column=0, padx=5, pady=5)
    medical_history_entry = ttk.Entry(search_frame)
    medical_history_entry.grid(row=5, column=1, padx=5, pady=5)

    # Create a search button
    search_button = ttk.Button(search_frame, text="Search", command=search_donor)
    search_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    # Create a treeview to display donor details
    tree = ttk.Treeview(root, columns=("Donor ID","Blood Group","Name","Medical History", "Age", "Address" ))
    tree.heading("Name", text="Name")
    tree.heading("Donor ID", text="Donor ID")
    tree.heading("Address", text="Address")
    tree.heading("Age", text="Age")
    tree.heading("Blood Group", text = "Blood Group")
    tree.heading("Medical History", text = "Medical History")
    tree.pack(pady=8, padx=10)

    # Create buttons for view and update options
    view_button = ttk.Button(root, text="View All Donors", command=view_donor)
    view_button.pack(pady=5)

    update_button = ttk.Button(root, text="Update Donor Details", command=update_donor)
    update_button.pack(pady=5)

    # Create a function to close the cursor object and exit the application
    def close_app():
        cursor.close()
        root.destroy()

    # Create an exit button to close the application
    exit_button = ttk.Button(root, text="Exit", command=close_app)
    exit_button.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

def patient_details():

    cursor = db.cursor()

    def search_patient():
        # Fetch attribute values from the entry fields
        name = name_entry.get()
        patient_ID = patient_ID_entry.get()
        address = address_entry.get()
        age = age_entry.get()
        blood_group = blood_group_entry.get()

        # Execute the SQL query to search for inventory data based on attribute values
        sql = "SELECT * FROM Patient WHERE "
        values = []
        if name:
            sql += "Name = %s AND "
            values.append(name)
        if patient_ID:
            sql += "Patient_ID = %s AND "
            values.append(patient_ID)
        if address:
            sql += "address = %s AND "
            values.append(address)
        if age:
            sql += "age = %s AND "
            values.append(age)
        if blood_group:
            sql += "Blood_Group = %s AND "
            values.append(blood_group)
        
        # Remove the trailing "AND" from the SQL query
        if sql.endswith("AND "):
            sql = sql[:-4]

        cursor.execute(sql, tuple(values))
        results = cursor.fetchall()

        # Clear the treeview
        tree.delete(*tree.get_children())

        for result in results:
            tree.insert("", "end", values = result)


    # Create a function to view donor details
    def view_patient():
        # Clear treeview
        tree.delete(*tree.get_children())

        # Fetch donor details from database
        cursor.execute("SELECT * FROM Patient")
        inventory = cursor.fetchall()

        # Insert donor details into treeview
        for unit in inventory:
            tree.insert('', 'end', values=unit)

    # Create a function to update donor details
    def update_patient():
        # Get selected item from treeview
        selected_item = tree.selection()
        if selected_item:
            # Get donor details from selected item
            patient = tree.item(selected_item)['values']

            # Create a top-level window for updating donor details
            update_window = tk.Toplevel(root)
            update_window.title("Update Patient")
            update_window.geometry("300x300")

            # Create a frame for update form
            update_frame = ttk.LabelFrame(update_window, text="Update Patient Details")
            update_frame.pack(pady=10, padx=10)

            # Create labels and entry fields for donor details

            name_label = ttk.Label(update_frame, text="Name:")
            name_label.grid(row=0, column=0, padx=5, pady=4)
            name_entry = ttk.Entry(update_frame)
            name_entry.grid(row=0, column=1, padx=5, pady=4)
            name_entry.insert(0, patient[0])  # Pre-fill name entry field with current name

            address_label = ttk.Label(update_frame, text="Address:")
            address_label.grid(row=3, column=0, padx=5, pady=4)
            address_entry = ttk.Entry(update_frame)
            address_entry.grid(row=3, column=1, padx=5, pady=4)
            address_entry.insert(0, patient[2])  # Pre-fill address entry field with current address

            age_label = ttk.Label(update_frame, text="Age:")
            age_label.grid(row=4, column=0, padx=5, pady=4)
            age_entry = ttk.Entry(update_frame)
            age_entry.grid(row=4, column=1, padx=5, pady=4)
            age_entry.insert(0, patient[3])  

            blood_group_label = ttk.Label(update_frame, text="Blood Group:")
            blood_group_label.grid(row=5, column=0, padx=5, pady=4)
            blood_group_entry = ttk.Entry(update_frame)
            blood_group_entry.grid(row=5, column=1, padx=5, pady=4)
            blood_group_entry.insert(0, patient[4])


            # Create a function to update patient details in database
            def save_update():
                # Get updated patient details from entry fields
                updated_name = name_entry.get()
                updated_address = address_entry.get()
                updated_age = age_entry.get()
                updated_blood_group = blood_group_entry.get()

                # Update patient details in database
                cursor.execute("UPDATE Patient SET name = %s, address = %s, age = %s, blood_group = %s WHERE patient_ID = %s",
                            (updated_name, updated_address, updated_age, updated_blood_group, patient[1]))
                db.commit()

                # Close update window and refresh patient details
                update_window.destroy()

            # Create a save button to update patient details
            save_button = ttk.Button(update_frame, text="Save", command=save_update)
            save_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        else:
            # Show error message if no patient is selected
            tk.messagebox.showerror("Error", "Please select a unit to update.")

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Patient Details")
    root.geometry("800x620")

    search_frame = ttk.LabelFrame(root, text="Search Patient")
    search_frame.pack(pady=10, padx=10)

    # Create entry fields for search options
    name_label = ttk.Label(search_frame, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(search_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    patient_ID_label = ttk.Label(search_frame, text="Patient ID:")
    patient_ID_label.grid(row=1, column=0, padx=5, pady=5)
    patient_ID_entry = ttk.Entry(search_frame)
    patient_ID_entry.grid(row=1, column=1, padx=5, pady=5)

    address_label = ttk.Label(search_frame, text="Address:")
    address_label.grid(row=2, column=0, padx=5, pady=5)
    address_entry = ttk.Entry(search_frame)
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    age_label = ttk.Label(search_frame, text="Age:")
    age_label.grid(row=3, column=0, padx=5, pady=5)
    age_entry = ttk.Entry(search_frame)
    age_entry.grid(row=3, column=1, padx=5, pady=5)

    blood_group_label = ttk.Label(search_frame, text="Blood Group:")
    blood_group_label.grid(row=4, column=0, padx=5, pady=5)
    blood_group_entry = ttk.Entry(search_frame)
    blood_group_entry.grid(row=4, column=1, padx=5, pady=5)

    # Create a search button
    search_button = ttk.Button(search_frame, text="Search", command=search_patient)
    search_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)


    # Create a treeview to display patient details
    tree = ttk.Treeview(root, columns=("Name", "Patient ID", "Address", "Age", "Blood Group"))
    tree.heading("Name", text="Name")
    tree.heading("Patient ID", text="Patient ID")
    tree.heading("Address", text="Address")
    tree.heading("Age", text="Age")
    tree.heading("Blood Group", text = "Blood Group")
    tree.pack(pady=8, padx=10)

    # Create buttons for view and update options
    view_button = ttk.Button(root, text="View All Patients", command=view_patient)
    view_button.pack(pady=5)

    update_button = ttk.Button(root, text="Update Patient Details", command=update_patient)
    update_button.pack(pady=5)

    # Create a function to close the cursor object and exit the application
    def close_app():
        root.destroy()
        cursor.close()

    # Create an exit button to close the application
    exit_button = ttk.Button(root, text="Exit", command=close_app)
    exit_button.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

def add_patient():

    # Create a cursor object to interact with the database
    db_cursor = db.cursor()

    # Function to add a new patient to the patient table
    def new_patient():
        # Get the input values from the entry widgets
        patient_name = patient_name_entry.get()
        address = address_entry.get()
        blood_group = blood_group_entry.get()
        age = age_entry.get()

        # Query to get the last patient ID from the patient table
        get_last_patient_id_sql = "SELECT MAX(Patient_ID) FROM Patient"
        db_cursor.execute(get_last_patient_id_sql)
        max_id = db_cursor.fetchone()[0]

        # Generate the next patient ID sequentially
        next_id = 'P001' if max_id is None else 'P{:03d}'.format(int(max_id[1:]) + 1)

        # Construct the SQL query to insert a new patient
        sql = "INSERT INTO Patient (Patient_ID, Name, Address, Blood_Group, Age) VALUES (%s, %s, %s, %s, %s)"
        values = (next_id, patient_name, address, blood_group, age)

        # Execute the query with the provided values
        db_cursor.execute(sql, values)
        db.commit()

        # Display a success message
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Patient added successfully with Patient ID: {next_id}")

    # Create the main window
    root = tk.Tk()
    root.title("Blood Bank Management System")
    root.geometry("600x400")

    # Create patient name label and entry
    patient_name_label = tk.Label(root, text="Patient Name:")
    patient_name_label.pack()
    patient_name_entry = tk.Entry(root)
    patient_name_entry.pack()

     # Create patient address label and entry
    address_label = tk.Label(root, text="Address:")
    address_label.pack()
    address_entry = tk.Entry(root)
    address_entry.pack()

    # Create blood group label and entry
    blood_group_label = tk.Label(root, text="Blood Group:")
    blood_group_label.pack()
    blood_group_entry = tk.Entry(root)
    blood_group_entry.pack()

    # Create age label and entry
    age_label = tk.Label(root, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    # Create add patient button
    add_patient_button = tk.Button(root, text="Add Patient", command=new_patient)
    add_patient_button.pack()

    # Create result text widget
    result_text = tk.Text(root, wrap=tk.WORD)
    result_text.pack(expand=tk.YES, fill=tk.BOTH)

    # Function to clear input fields and results
    def clear_input():
        patient_name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        blood_group_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        result_text.delete("1.0", tk.END)

    # Create clear input button
    clear_input_button = tk.Button(root, text="Clear Input", command=clear_input)
    clear_input_button.pack()

    root.mainloop()

    db_cursor.close()

def transfuse():

    # Create cursor object
    mycursor = db.cursor()

    # Create the GUI window
    window = tk.Tk()
    window.title("Blood Transfusion")

    # Define the GUI elements
    patient_id_label = tk.Label(window, text="Patient ID:")
    patient_id_entry = tk.Entry(window)
    blood_group_label = tk.Label(window, text="Patient Blood Group:")
    blood_group_entry = tk.Entry(window)
    select_unit_label = tk.Label(window, text="Select Blood Unit:")
    select_unit_listbox = tk.Listbox(window, height=10, width = 70)


    # Define the GUI layout
    patient_id_label.grid(row=0, column=0, padx = 5, pady = 2.5)
    patient_id_entry.grid(row=0, column=1, padx = 5, pady = 2.5)
    blood_group_label.grid(row=1, column=0, padx = 5, pady = 2.5)
    blood_group_entry.grid(row=1, column=1, padx = 5, pady = 2.5)
    select_unit_label.grid(row=2, column=0, padx = 5, pady = 2.5)
    select_unit_listbox.grid(row=2, column=1, padx = 5, pady = 2.5)


    # Populate the blood units listbox with available units
    def populate_listbox():
        select_unit_listbox.delete(0, tk.END)
        blood_group = blood_group_entry.get()
        mycursor.execute("SELECT ID, Component, Expiry_date FROM Inventory_View WHERE Blood_Group = %s AND Status = 'Available' ORDER BY Expiry_date", (blood_group,))
        units = mycursor.fetchall()
        for unit in units:
            select_unit_listbox.insert(tk.END, "ID: {} - Component: {} - Expiry Date: {}".format(unit[0], unit[1], unit[2]))

    # Transfuse the selected unit to the patient
    def transfuse_unit():
        patient_id = patient_id_entry.get()
        selected_unit = select_unit_listbox.get(tk.ACTIVE)
        if not selected_unit:
            messagebox.showerror("Error", "Please select a blood unit to transfuse.")
            return
        unit_id = selected_unit.split()[1]
        mycursor.execute("INSERT INTO Transfusion (Unit_Id, Patient_Id, Date_Transfused) VALUES (%s, %s, NOW())", (unit_id, patient_id))
        db.commit()
        messagebox.showinfo("Success", "Blood unit {} has been transfused to patient {}.".format(unit_id, patient_id))
        populate_listbox()

    # Populate the listbox initially and whenever the blood group entry is updated
    populate_listbox()
    blood_group_entry.bind("<KeyRelease>", lambda event: populate_listbox())

    transfuse_button = tk.Button(window, text="Transfuse", command=transfuse_unit)
    transfuse_button.grid(row=3, column=1)



    # Run the GUI loop
    window.mainloop()

    mycursor.close()

def transfusion_history():

    # Function to filter Treeview by patient ID
    def filter_by_patient_id():
        patient_id = filter_entry.get()
        treeview.delete(*treeview.get_children()) # Clear Treeview
        
        # Connect to the database
        cursor = db.cursor()
        
        # Fetch data from the database based on patient ID
        cursor.execute("SELECT t.Patient_ID, i.ID, t.Date_Transfused, i.Donor_ID FROM transfusion t "
                    "JOIN inventory i ON t.Unit_ID = i.ID "
                    "WHERE t.Patient_ID = %s", (patient_id,))
        data = cursor.fetchall()
        
        # Populate Treeview with fetched data
        for row in data:
            treeview.insert('', 'end', values=row)
        
        # Close database connection
        cursor.close()

    # Function to fetch all transfusion history from the database
    def view_all_history():
        treeview.delete(*treeview.get_children()) # Clear Treeview
        
        # Connect to the database
        cursor = db.cursor()
        
        # Fetch all data from the database
        cursor.execute("SELECT t.Patient_ID, i.ID, t.Date_Transfused, i.Donor_ID FROM transfusion t "
                    "JOIN inventory i ON t.Unit_ID = i.ID")
        data = cursor.fetchall()
        
        # Populate Treeview with fetched data
        for row in data:
            treeview.insert('','end', values=row)
        
        # Close database connection
        cursor.close()

    # Create Tkinter window
    root = tk.Tk()
    root.title("Transfusion History")

    # Create Filter Entry widget
    filter_entry = tk.Entry(root)
    filter_entry.pack(pady=10)

    # Create Filter Button
    filter_button = tk.Button(root, text="Filter by Patient ID", command=filter_by_patient_id)
    filter_button.pack(pady=5)

    # Create View All Button
    view_all_button = tk.Button(root, text="View All History", command=view_all_history)
    view_all_button.pack(pady=5)

    # Create Treeview widget
    treeview = ttk.Treeview(root, columns = ('Patient ID', 'Unit ID', 'Transfusion Date', 'Donor ID'))

    treeview.column('Patient ID', anchor=tk.W, width=100)
    treeview.column('Unit ID', anchor = tk.W, width = 80)
    treeview.column('Transfusion Date', anchor=tk.W, width=150)
    treeview.column('Donor ID', anchor=tk.W, width=100)
    treeview.heading('#0', text='', anchor=tk.W)
    treeview.heading('Patient ID', text='Patient ID')
    treeview.heading('Unit ID', text = 'Unit ID')
    treeview.heading('Transfusion Date', text = 'Transfusion Date')
    treeview.heading('Donor ID', text = 'Donor ID')
    treeview.pack(padx = 8, pady = 10)

    def close_app():
        root.destroy()

    # Create an exit button to close the application
    exit_button = ttk.Button(root, text="Exit", command=close_app)
    exit_button.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

def contact_number():

    cursor = db.cursor()

    # Create main window
    root = tk.Tk()
    root.title("Contact Numbers")
    root.geometry("600x450")

    # Create Treeview
    tree = ttk.Treeview(root, columns=("ID", "Contact Number"))
    tree.heading("#0", text="Type")
    tree.heading("ID", text="ID")
    tree.heading("Contact Number", text="Contact Number")
    tree.pack(pady=10)

    def update_tree():
        # Clear existing items in Treeview
        tree.delete(*tree.get_children())

        # Fetch data from donor_contact_no table
        cursor.execute("SELECT donor_id, contact_no FROM donor_contact_no")
        donor_contact_data = cursor.fetchall()
        for data in donor_contact_data:
            tree.insert("", tk.END, text="Donor", values=data)

        # Fetch data from patient_contact_no table
        cursor.execute("SELECT patient_id, contact_no FROM patient_contact_no")
        patient_contact_data = cursor.fetchall()
        for data in patient_contact_data:
            tree.insert("", tk.END, text="Patient", values=data)

    def search_contact():
        search_id = search_entry.get()
        if search_id.startswith("D"):
            cursor.execute("SELECT donor_id, contact_no FROM donor_contact_no WHERE donor_id = %s", (search_id,))
            contact_data = cursor.fetchall()
            tree.delete(*tree.get_children())
            for data in contact_data:
                tree.insert("", tk.END, text="Donor", values=data)
        elif search_id.startswith("P"):
            cursor.execute("SELECT patient_id, contact_no FROM patient_contact_no WHERE patient_id = %s", (search_id,))
            contact_data = cursor.fetchall()
            tree.delete(*tree.get_children())
            for data in contact_data:
                tree.insert("", tk.END, text="Patient", values=data)

    def add_contact():
        def add_contact_submit():
            id_prefix = id_entry.get()[0]
            contact_number = contact_entry.get()
            if id_prefix == "D":
                donor_id = id_entry.get()
                cursor.execute("INSERT INTO donor_contact_no (donor_id, contact_no) VALUES (%s, %s)",
                            (donor_id, contact_number))
            elif id_prefix == "P":
                patient_id = id_entry.get()
                cursor.execute("INSERT INTO patient_contact_no (patient_id, contact_no) VALUES (%s, %s)",
                            (patient_id, contact_number))
            db.commit()
            update_tree()
            add_contact_window.destroy()

        add_contact_window = tk.Toplevel(root)
        add_contact_window.title("Add Contact Number")
        add_contact_window.geometry("300x200")
        id_label = tk.Label(add_contact_window, text="ID:")
        id_label.pack(pady=10)
        id_entry = tk.Entry(add_contact_window)
        id_entry.pack(pady=10)
        contact_label = tk.Label(add_contact_window, text="Contact Number:")
        contact_label.pack(pady=10)
        contact_entry = tk.Entry(add_contact_window)
        contact_entry.pack(pady=10)
        submit_button = tk.Button(add_contact_window, text="Submit", command=add_contact_submit)
        submit_button.pack(pady=10)

    def delete_contact():
        selected_item = tree.focus()
        if selected_item:
            # Get the values of the selected row
            values = tree.item(selected_item)['values']
            contact_id = values[0]
            contact_number = values[1]
            contact_type = contact_id[0]
            ##contact_id = contact_id[1:]

            # Delete the row from respective table based on ID and type
            if contact_type == 'D':
                query = f"DELETE FROM Donor_Contact_No WHERE Donor_ID = '{contact_id}' AND Contact_No = '{contact_number}'"
            elif contact_type == 'P':
                query = f"DELETE FROM Patient_Contact_No WHERE Patient_ID = '{contact_id}' AND Contact_No = '{contact_number}"

            # Execute the delete query
            cursor.execute(query)
            db.commit()

            # Remove the selected row from the Treeview
            tree.delete(selected_item)

    # Add Search and Add buttons
    search_label = tk.Label(root, text="Search by ID:")
    search_label.pack(pady=5)
    search_entry = tk.Entry(root)
    search_entry.pack(pady=5)

    search_button = ttk.Button(root, text="Search", command=search_contact)
    search_button.pack(pady=5)

    add_button = ttk.Button(root, text="Add Number", command=add_contact)
    add_button.pack(pady=5)

    button_delete = ttk.Button(root, text="Delete", command=delete_contact)
    button_delete.pack(pady = 5)

    view_button = ttk.Button(root, text="View All", command=update_tree)
    view_button.pack(pady=5)


    # Start main event loop
    root.mainloop()

    # Close database connection
    cursor.close()


# create a main window
root = tk.Tk()
root.title("Blood Bank Homepage")

# set the size of the window
root.geometry("500x470")

# create a label
lbl = tk.Label(root, text="Select an option from the following:")
lbl.pack(pady=10)

# function to open a new window for each button
def open_window(window_name):
    new_window = tk.Toplevel(root)
    new_window.title(window_name)

# create a button to search inventory
btn1 = tk.Button(root, text="Inventory", width=30, command=lambda: inventory_details())
btn1.pack(pady=10)

# create a button to take blood
btn2 = tk.Button(root, text="Take Blood", width=30, command=lambda: take_blood())
btn2.pack(pady=10)

# create a button to add donor
btn3 = tk.Button(root, text="Add Donor", width=30, command=lambda: add_donor())
btn3.pack(pady=10)

# create a button to view donor information
btn4 = tk.Button(root, text="View Donor Information", width=30, command=lambda: donor_details())
btn4.pack(pady=10)

# create a button to view patient information
btn5 = tk.Button(root, text="View Patient Information", width=30, command=lambda: patient_details())
btn5.pack(pady=10)

# create a button to add patient
btn6 = tk.Button(root, text="Add Patient", width=30, command=lambda: add_patient())
btn6.pack(pady=10)

# create a button to transfuse
btn7 = tk.Button(root, text="Transfuse", width=30, command=lambda: transfuse())
btn7.pack(pady=10)

btn8 = tk.Button(root, text = "View Transfusion History", width = 30, command = lambda: transfusion_history())
btn8.pack(pady = 10)

btn9 = tk.Button(root, text = "View Contact Numbers", width = 30, command = lambda:contact_number())
btn9.pack(pady = 10)

# run the application
root.mainloop()