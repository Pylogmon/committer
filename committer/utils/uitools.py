from PySide2.QtWidgets import QLabel


def set_size(label: QLabel):
    size = label.height()
    label.setFixedSize(size, size)
    label.setScaledContents(True)
