from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


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
