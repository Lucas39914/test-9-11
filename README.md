# hello Lucas 倒计时弹窗

一个最小的 Python 项目：运行时弹出窗口显示 `hello Lucas`，并倒计时 3 秒，倒计时结束后自动关闭。

## 环境要求

- Python 3（需要包含 tkinter，Windows 官方安装包默认自带）

## 运行

```bash
python hello.py
```

运行后弹出窗口，显示 `hello Lucas` 和倒计时文字，3 秒后窗口自动关闭、程序退出。

## 配置

倒计时时长由 `hello.py` 顶部的常量控制：

```python
COUNTDOWN_SECONDS = 3
```

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `hello.py` | 主程序，使用标准库 `tkinter` 创建窗口，通过 `after()` 驱动倒计时 |
