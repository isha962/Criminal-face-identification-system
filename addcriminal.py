import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import trainface

class AddCriminal:

    def addCriminal(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Criminal Detection System")

        # Add padding to the top of the window
        self.root.geometry("+{}+{}".format(100, 50))  # Set padding from the top

        # Create and pack the widgets
        self.add_details_label = tk.Label(self.root, text="ADD CRIMINAL DETAILS", font=("Helvetica", 25))
        self.add_details_label.pack(side="top", padx=5, pady=10)

        self.name_label = tk.Label(self.root, text="NAME:", font=("Helvetica", 15))
        self.name_label.pack(anchor="center", padx=5, pady=15)

        # Increase the height of the name input field using Text widget
        self.name_entry = tk.Text(self.root, height=2, width=40)
        self.name_entry.pack(anchor="center", padx=5, pady=10)

        self.criminal_type_label = tk.Label(self.root, text="TYPE:", font=("Helvetica", 15))
        self.criminal_type_label.pack(anchor="center", padx=5, pady=10)

        self.criminal_type_var = tk.StringVar(self.root)
        self.criminal_type_var.set("")  # Initial value
        self.criminal_type_option_menu = tk.OptionMenu(self.root, self.criminal_type_var, "Criminal", "Non-criminal")
        self.criminal_type_option_menu.pack(anchor="center", padx=5, pady=10)

        self.description_label = tk.Label(self.root, text="DESCRIPTION:", font=("Helvetica", 15))
        self.description_label.pack(anchor="center", padx=5, pady=10)

        self.description_entry = tk.Text(self.root, width=40, height=5)
        self.description_entry.pack(anchor="center", padx=5, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 12), command=self.submit_details, bg="green", fg="white", height=2, width=20)
        self.submit_button.pack(anchor="center", padx=5, pady=5)

        self.root.mainloop()

    def dbconnection(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                  database='criminal',
                                                  user='root',
                                                  password='root')
            return connection
        except Error as e:
            print("Error connecting to database:", e)
            return None

    def submit_details(self):
        con = self.dbconnection()
        if con:
            name = self.name_entry.get("1.0", tk.END).strip()
            criminal_type = self.criminal_type_var.get()
            description = self.description_entry.get("1.0", tk.END).strip()

            if name == "":
                messagebox.showerror("Error", "Please enter a name.")
                return
            elif criminal_type == "":
                messagebox.showerror("Error", "Please select criminal type.")
                return
            elif description == "":
                messagebox.showerror("Error", "Please enter a description.")
                return
            else:
                try:
                    cursor = con.cursor()
                    cursor.execute("INSERT INTO crmdetails(name, type, description) VALUES (%s, %s, %s)", (name, criminal_type, description))
                    con.commit()
                    
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    lastInsertedID = cursor.fetchone()[0]
                    
                    trainface.saveCriminalFace(lastInsertedID, name)
                    
                    messagebox.showinfo("Success", "Criminal details submitted successfully.")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    con.close()
if __name__ == "__main__":
    AddCriminal()


