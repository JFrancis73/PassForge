from tkinter import *
from datetime import datetime
import os

# Define function to validate date format
def validate_date(text):
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Create main window
window = Tk()
window.title("User Details")

# Define variables to store user details
first_name = StringVar()
last_name = StringVar()
dob = StringVar()
partner_first_name = StringVar()
partner_last_name = StringVar()
partner_dob = StringVar()
child_first_name = StringVar()
child_last_name = StringVar()
child_dob = StringVar()
father_first_name = StringVar()
father_last_name = StringVar()
father_dob = StringVar()
mother_first_name = StringVar()
mother_last_name = StringVar()
mother_dob = StringVar()
pet_name = StringVar()
keywords = StringVar()

# Create labels and entry fields
Label(window, text="First Name:").grid(row=0, column=0)
Entry(window, textvariable=first_name).grid(row=0, column=1)

Label(window, text="Last Name:").grid(row=1, column=0)
Entry(window, textvariable=last_name).grid(row=1, column=1)

Label(window, text="Date of Birth:").grid(row=2, column=0)
Entry(window, textvariable=dob).grid(row=2, column=1)

# Add similar labels and entries for all remaining fields

# Additional keywords entry
Label(window, text="Additional Keywords:").grid(row=12, column=0)
Entry(window, textvariable=keywords).grid(row=12, column=1)

# Submit button
def submit_details():
    # Access and process user input here
    # For example, print details to console
    print(f"First Name: {first_name.get()}")
    print(f"Last Name: {last_name.get()}")
    # ... and so on for other fields
    base_words = [first_name.get(),last_name.get(),] + keywords.get().split() #continue
    nums = dob.get()
    nums = [nums[:2],nums[:2]+nums[2:4],nums[4:]]
    base_words += nums
    print(base_words)
    with open(".tmp/base.txt","w") as file:
        for i in base_words:
            file.write(i+"\n")
    os.system("python cupp\\cupp.py -q -w .tmp\\base.txt")
    os.system('python .\\Wordlister\\wordlister.py --cap --up --min 4 --max 16 --input .\\cuppout.txt --output .\\.tmp\\templist.txt --perm 1') 


Button(window, text="Submit", command=submit_details).grid(row=13, column=1)

# Run the main event loop
window.mainloop()