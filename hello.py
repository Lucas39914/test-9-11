"""hello Lucas 倒计时弹窗程序。

运行后弹出一个对话框，显示 "hello Lucas" 并倒计时 3 秒，
倒计时结束后窗口自动关闭。
仅使用 Python 标准库 tkinter，无需安装任何第三方依赖。
"""

import tkinter as tk

COUNTDOWN_SECONDS = 3
FONT_FAMILY = "Microsoft YaHei"


def main() -> None:
    root = tk.Tk()
    root.title("hello Lucas")
    root.resizable(False, False)
    root.attributes("-topmost", True)  # 置顶，避免被其他窗口挡住

    tk.Label(root, text="hello Lucas", font=(FONT_FAMILY, 20, "bold")).pack(
        padx=48, pady=(28, 10)
    )
    countdown = tk.Label(root, font=(FONT_FAMILY, 11), fg="#888888")
    countdown.pack(pady=(0, 26))

    def tick(remaining: int) -> None:
        if remaining <= 0:
            root.destroy()
            return
        countdown.config(text=f"{remaining} 秒后自动关闭")
        root.after(1000, tick, remaining - 1)

    # 先填好初始文案再计算尺寸，保证窗口居中时大小已经确定
    countdown.config(text=f"{COUNTDOWN_SECONDS} 秒后自动关闭")
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")

    root.after(1000, tick, COUNTDOWN_SECONDS - 1)
    root.mainloop()


if __name__ == "__main__":
    main()
