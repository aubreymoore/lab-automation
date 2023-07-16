
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os

DBPATH = 'bioassay.sqlite3'

def enter_data():
    sn = sn_entry.get()
    date_collected = date_collected_entry.get()
    trap_id = trap_id_entry.get()
    sex = sex_entry.get()

    # Create Table
    conn = sqlite3.connect(DBPATH)
    table_create_query = '''
    CREATE TABLE IF NOT EXISTS beetles (
    sn INTEGER PRIMARY KEY,
    date_collected TEXT NOT NULL,
    trap_id INTEGER NOT NULL,
    sex text CHECK(sex IN ('m', 'f')) NOT NULL,
    CONSTRAINT timestamp CHECK (date_collected==strftime('%Y-%m-%d',date_collected)) )
    '''
    conn.execute(table_create_query)

    # Insert Data
    data_insert_query = '''
    INSERT INTO beetles (sn, date_collected, trap_id, sex)
    VALUES (?, ?, ?, ?)
    '''
    data_insert_tuple = (sn, date_collected, trap_id, sex)
    cursor = conn.cursor()
    try:
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
    except sqlite3.Error as er:
        s = f'SQLite error: {" ".join(er.args)}'
        tkinter.messagebox.showwarning(title= "Error", message=s)
    else:
        tkinter.messagebox.showwarning(title= "Ok", message=f'Data entered for beetle {sn}')
    conn.close()

window = tkinter.Tk()
window.title("add_beetles.py   Adds records to beetles table")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
my_frame = tkinter.LabelFrame(frame, text="")
my_frame.grid(row= 0, column=0, padx=20, pady=10)

sn_label = tkinter.Label(my_frame, text='sn (int)')
sn_label.grid(row=0, column=0)
sn_entry = tkinter.Entry(my_frame)
sn_entry.grid(row=1, column=0)

date_collected_label = tkinter.Label(my_frame, text='date_collected' )
date_collected_label.grid(row=0, column=1)
date_collected_entry = tkinter.Entry(my_frame)
date_collected_entry.grid(row=1, column=1)
date_collected_entry.insert(0, '2023-07-16')

trap_id_label = tkinter.Label(my_frame, text='trap_id (int)')
trap_id_label.grid(row=0, column=2)
trap_id_entry = tkinter.Entry(my_frame)
trap_id_entry.grid(row=1, column=2)

sex_label = tkinter.Label(my_frame, text='sex (m or f)')
sex_label.grid(row=0, column=3)
sex_entry = tkinter.Entry(my_frame)
sex_entry.grid(row=1, column=3)

def open_db_browser():
    os.system(f'sqlitebrowser {DBPATH}')

# Button
button = tkinter.Button(frame, text="Add record", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Veiw database using DB Browser
button1 = tkinter.Button(frame, text="View database using DB Browser", command=open_db_browser)
button1.grid(row=4, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
