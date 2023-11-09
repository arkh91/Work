from pykeepass import PyKeePass # pip install pykeepass


# Specify the path to your KeePass database (KDBX file)
kdbx_file = 'path/to/your/database.kdbx'

# Specify the master password for the database
master_password = 'your_master_password'

# Open the KeePass database
kp = PyKeePass(kdbx_file, password=master_password)

# Access entries in the database
for entry in kp.entries:
    print(f"Title: {entry.title}")
    print(f"Username: {entry.username}")
    print(f"Password: {entry.password}")
    # You can access other attributes like URLs, notes, etc. as well

# Close the database
kp.close()
