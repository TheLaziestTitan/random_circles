import random
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setFixedSize(QSize(600, 400))

        self.button = QPushButton("Нарисовать окружности", self)
        self.button.setGeometry(200, 350, 200, 40)
        self.button.clicked.connect(self.update)

        self.circles = []

    def paintEvent(self, event):
        if not self.circles:
            return

        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle["col"])
            painter.drawEllipse(circle["x"], circle["y"], circle["d"], circle["d"])

    def update(self):
        self.circles = [
            {
                "x": random.randint(0, 500),
                "y": random.randint(0, 300),
                "d": random.randint(20, 100),
                "col": QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            }
            for _ in range(random.randint(5, 15))
        ]
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
