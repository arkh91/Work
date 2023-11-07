import subprocess   #Launch apps


def launch_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # Command to run Chrome
    command = [chrome_path]

    # Launch Chrome
    subprocess.Popen(command)