"""第 2 周 · Day 1 练习：用 requests 抓取一个真实的 API。

任务：把下面的 TODO 补全，让脚本打印出 JSON 里的字段。
做完后自己提交：git add week02/day01_api.py && git commit -m "week02 day1: 第一次用 requests 调 API" && git push

运行方式（在仓库根目录）：
    python week02/day01_api.py
"""

import json

import requests

URL = "https://httpbin.org/json"


def main() -> None:
    # TODO 1：用 requests.get() 请求 URL，把响应对象存到变量 resp
    # 提示：resp = requests.get(URL, timeout=10)
    resp = requests.get(URL, timeout=10)

    # TODO 2：resp 里有三个常用属性，各打印一次看它们是什么
    #   resp.status_code  —— HTTP 状态码（200 表示成功）
    #   resp.text         —— 原始文本（JSON 也是文本！）
    #   resp.headers      —— 响应头（一个字典）
    # 提示：print(resp.status_code)
    print(resp.status_code)
    print(resp.text)
    print(resp.headers)

    # TODO 3：把 JSON 文本变成 Python 字典
    # 两种写法等价，都试一遍：
    #   data = json.loads(resp.text)     # 手动解析
    #   data = resp.json()               # requests 自带的便捷方法
    data = resp.json()
    print(data)

    # TODO 4：看一眼 data 的结构，然后取出 slideshow 的标题打印出来
    # 提示：字典套字典，一层一层往下取：data["slideshow"]["title"]
    # 打印形如：标题：xxx
    print("标题：" + data["slideshow"]["slides"][0]["title"])


if __name__ == "__main__":
    main()
