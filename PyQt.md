# PyQt 6

> https://www.riverbankcomputing.com/static/Docs/PyQt6/

# 安装
```
pip install PyQt6
```

# 开发
```
import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
```