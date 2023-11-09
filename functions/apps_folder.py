import getpass
import os



def apps_folder():
    #favorite()
    user_id = current_user()
    ADUC(user_id)
    #Account_Lockout_Status()
    #GC(user_id)




def current_user():
    username = getpass.getuser()
    print(f"The username of the logged-in user is: {username}")
    return username

def ADUC(user_id):

    file_path = f"C:/users/{user_id}/Downloads/ADUC.ica"
    print(file_path)
    try:
        os.startfile(file_path)
        ADUC = True
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist - Please download an rename it.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def GC(user_id):
    file_path = f"C:/users/{user_id}/Downloads/PHSA.ica"
    print(file_path)
    try:
        os.startfile(file_path)
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist - Please download an rename it.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

