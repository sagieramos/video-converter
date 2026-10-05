import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VideoConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Converter")
        self.resize(900, 600)

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title
        title = QLabel("Video Converter")
        title.setStyleSheet("font-size: 32px; font-weight: bold;")
        layout.addWidget(title)

        # Select button
        select_button = QPushButton("Select Video")
        layout.addWidget(select_button)


app = QApplication(sys.argv)

window = VideoConverter()
window.show()

sys.exit(app.exec())