# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# ///////////////////////////////////////////////////////////////


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor
from Circle_Loader import CircleLoader



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        layout = QVBoxLayout(self)
        frame = QFrame(self)
        layoutF = QVBoxLayout(frame)
        layout.addWidget(frame)
        loader = CircleLoader(frame, penWidth=7, color=QColor("#159Ac6"))
        layoutF.addWidget(loader)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())