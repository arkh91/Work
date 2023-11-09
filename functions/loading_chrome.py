import subprocess   #Launch apps


def launch_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    url="https://apps.phsa.ca/logon/LogonPoint/tmindex.html"
    # Command to run Chrome
    command = [chrome_path, url]

    # Launch Chrome
    subprocess.Popen(command)
