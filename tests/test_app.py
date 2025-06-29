import pytest
from PyQt5.QtWidgets import QApplication, QLabel
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import MainWindow  # Đảm bảo tên file chính xác


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app
    # Không gọi app.quit() hoặc sys.exit() để tránh lỗi


@pytest.fixture
def app(qtbot, qapp):
    window = MainWindow()
    qtbot.addWidget(window)
    yield window
    window.close()


def test_window_title(app):
    assert app.windowTitle() == "PyQt5 App"


def test_label_text(app):
    label = app.findChild(QLabel)
    assert label is not None
    assert label.text() == "Hello, PyQt5!"


def test_label_position(app):
    label = app.findChild(QLabel)
    assert label is not None
    assert label.pos().x() == 50
    assert label.pos().y() == 50
