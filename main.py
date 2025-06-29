from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import os
from loguru import logger

# Xác định working dir
if getattr(sys, "frozen", False) or hasattr(sys, "_MEIPASS") or "__compiled__" in globals():
    os.chdir(os.path.dirname(sys.executable))
    logger.info(f"Running from executable: {os.getcwd()}")
    print(f"Running from executable: {os.getcwd()}")
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    logger.info(f"Running from source code: {os.getcwd()}")
    print(f"Running from executable: {os.getcwd()}")


curdir = os.getcwd()

logger.success(f"Current working directory: {curdir}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 App")
        label = QLabel("Hello, PyQt5!", self)
        label.move(50, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Starting PyQt5 application...")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
