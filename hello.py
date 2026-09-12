"""Hello World 弹窗程序。

运行后弹出一个对话框，显示 "Hello World"，点击确定后退出。
仅使用 Python 标准库 tkinter，无需安装任何第三方依赖。
"""

import tkinter as tk
from tkinter import messagebox


def main() -> None:
    root = tk.Tk()
    root.withdraw()  # 隐藏 tkinter 主窗口，只显示弹窗
    root.title("Hello World")

    messagebox.showinfo("Hello World", "Hello World")

    root.destroy()


if __name__ == "__main__":
    main()
