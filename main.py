import pyautogui    #pip install pyautogui
import subprocess   #Launch apps

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
        Loadingbar()
        print(file_name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print("Loading all codes")
    Loading_functions()
    print("Launching Chrome: \n")
    launch_chrome()






#python3 .\main.py
