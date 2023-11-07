import pyautogui    #pip install pyautogui
import subprocess   #Launch apps
import threading
import os
import importlib


def Loading_functions():
    # Create an empty list to store imported file names
    imported_files = []

    # Get a list of all Python files in the "function" folder
    function_files = [f[:-3] for f in os.listdir("functions") if f.endswith(".py")]

    # Import all the Python modules from the "function" folder
    for file in function_files:
        module = importlib.import_module(f'functions.{file}')
        globals().update({name: obj for name, obj in module.__dict__.items() if callable(obj)})
        imported_files.append(file)  # Add the imported file name to the list

    # Print the list of imported file names
    print("Imported files:")
    for file_name in imported_files:
        print(file_name)

def first_thread():
    Loadingbar()

def second_thread():
    # print("Loading all codes")
    #Loadingbar()
    print("Launching Chrome: \n")
    launch_chrome()
    apps()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Loading_functions()

    # Create and start the threads
    Loadin_window = threading.Thread(target=first_thread)
    #Loading_everything = threading.Thread(target=second_thread, args=(port, folder_name_str))
    Loading_everything = threading.Thread(target=second_thread)

    # Start the threads
    Loadin_window.start()
    Loading_everything.start()

    # Join the threads to ensure they finish before exiting
    Loadin_window.join()
    Loading_everything.join()




#python3 .\main.py
