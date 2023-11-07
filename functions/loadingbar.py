from tqdm import tqdm   #pip install tqdm
import tkinter as tk
from tkinter import ttk
import time



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar #pip install PyQt5
from PyQt5.QtCore import QThread, pyqtSignal
import time


def Loadingbar():
    '''
    # Define the total number of iterations or tasks
    total_iterations = 100

    # Create a tqdm object with the total number of iterations
    with tqdm(total=total_iterations, desc="Loading") as pbar:
        for i in range(total_iterations):
            # Simulate some work
            time.sleep(0.01)

            # Update the loading bar
            pbar.update(1)

    print("Loading complete!")
    '''
    app = QApplication(sys.argv)
    window = LoadingWindow()
    window.show()
    sys.exit(app.exec_())

class LoadingThread(QThread):
    update_signal = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # Simulate some work
            self.update_signal.emit(i)

class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Loading Bar")
        self.setGeometry(0, 0, 400, 100)
        self.centerOnScreen()

        self.loading_bar = QProgressBar(self)
        self.loading_bar.setGeometry(10, 10, 380, 30)
        self.loading_bar.setValue(0)

        self.loading_thread = LoadingThread()
        self.loading_thread.update_signal.connect(self.update_loading_bar)
        self.loading_thread.start()

    def centerOnScreen(self):
        screen = QApplication.desktop().screenGeometry()
        window_size = self.geometry()
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        self.move(x, y)

    def update_loading_bar(self, value):
        self.loading_bar.setValue(value)
        if value == 100:
            self.close()
