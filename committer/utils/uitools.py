from PySide2.QtWidgets import QLabel


# 设置label大小
def set_size(label: QLabel):
    size = label.height()
    label.setFixedSize(size, size)
    label.setScaledContents(True)
