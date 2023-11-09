import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar # pip install PyQt5
from PyQt5.QtCore import QThread, pyqtSignal, Qt                    # pip install PyQt5-tools
import time

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
        self.setWindowTitle("Loading Apps ...")
        self.setGeometry(0, 0, 400, 100)
        self.centerOnScreen()

        self.loading_bar = QProgressBar(self)
        self.loading_bar.setGeometry(20, 40, 350, 30)
        self.loading_bar.setValue(0)

        self.loading_thread = LoadingThread()
        self.loading_thread.update_signal.connect(self.update_loading_bar)
        self.loading_thread.finished.connect(self.cleanup)  # Connect to the cleanup method
        self.loading_thread.start()

        # Make the window topmost
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    #Location on the screen
    def centerOnScreen(self):
        screen = QApplication.desktop().screenGeometry()
        window_size = self.geometry()
        x = (screen.width() - window_size.width()) // 2
        y = (9 * screen.height() - 10 * window_size.height()) // 10
        self.move(x, y)

    def update_loading_bar(self, value):
        self.loading_bar.setValue(value)
        if value == 100:
            self.loading_thread.quit()  # Stop the thread when loading is complete

    def cleanup(self):
        # Perform cleanup tasks here
        print("Cleanup tasks here")
        self.close()

def Loadingbar():
    app = QApplication(sys.argv)
    window = LoadingWindow()
    window.show()
    sys.exit(app.exec_())
