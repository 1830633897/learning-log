"""week01 day1: 我的第一个 Python 脚本。

目标很简单：证明这台机器的 Python 能跑、我写的代码能执行。
后面每天往这个文件夹里加一点东西，四周后它就是一个真作品。
"""

from datetime import datetime


def main() -> None:
    print("=" * 40)
    print("转型学习计划 · 第 1 天")
    print(f"当前时间：{datetime.now():%Y-%m-%d %H:%M:%S}")
    print("Python 版本：", end="")
    import sys
    print(sys.version.split()[0])
    print("=" * 40)
    print("今天只做一件事：让这行字出现在屏幕上。做到了，就算开张。")


if __name__ == "__main__":
    main()
