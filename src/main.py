import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
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
        
        self.file_label = QLabel("No video selected")
        layout.addWidget(self.file_label)

        # Select button
        select_button = QPushButton("Select Video")
        select_button.clicked.connect(self.select_video)
        layout.addWidget(select_button)
    
    def select_video(self):
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Select Video",
                "",
                "Video Files (*.mp4 *.mkv *.avi *.mov *.webm *.flv *.wmv);;All Files (*)",
            )

            if file_path:
                self.file_label.setText(file_path)


app = QApplication(sys.argv)

window = VideoConverter()
window.show()

sys.exit(app.exec())