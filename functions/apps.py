import time
import pyautogui

# Get the screen size
screen_width, screen_height = pyautogui.size()

def apps():
    favorite()
    ADUC()
    Account_Lockout_Status()



def favorite(): # or Categories
    # Ensure mouse events are enabled
    pyautogui.FAILSAFE = True

    # Define the percentage values you want to move
    percentage_x = 0.08  # 20% to the right
    percentage_y = 0.2  # 8% down

    # Calculate the pixel coordinates
    move_x = int(screen_width * percentage_x)
    move_y = int(screen_height * percentage_y)

    # Move the mouse to the calculated coordinates
    pyautogui.moveTo(move_x, move_y)
    # waiting for the page to load
    time.sleep(1)

    pyautogui.click()

def ADUC():
    # Ensure mouse events are enabled
    pyautogui.FAILSAFE = True

    # Define the percentage values you want to move
    percentage_x = 0.08  # 20% to the right
    percentage_y = 0.15  # 8% down

    # Calculate the pixel coordinates
    move_x = int(screen_width * percentage_x)
    move_y = int(screen_height * percentage_y)

    # Move the mouse to the calculated coordinates
    pyautogui.moveTo(move_x, move_y)
    # waiting for the page to load
    time.sleep(1)

    pyautogui.click()
    time.sleep(30)

def Account_Lockout_Status():
    # Ensure mouse events are enabled
    pyautogui.FAILSAFE = True

    # Define the percentage values you want to move
    percentage_x = 0.08  # 20% to the right
    percentage_y = 0.26  # 8% down

    # Calculate the pixel coordinates
    move_x = int(screen_width * percentage_x)
    move_y = int(screen_height * percentage_y)

    # Move the mouse to the calculated coordinates
    pyautogui.moveTo(move_x, move_y)
    # waiting for the page to load
    time.sleep(1)

    pyautogui.click()
    time.sleep(30)
