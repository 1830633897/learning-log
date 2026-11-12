# NAS 侦察笔记（2026-11-12）

> 第 1 周 · SSH 登录 NAS。这份笔记就是第 4 周巡检脚本的"需求文档"。

## 环境速查

- 主机：群晖 DS918+（DSM 7.2.2，系统名 MYDS，Apollolake 平台）
- SSH：`ssh WQQ@100.107.171.101`
- 坑：NAS 上非交互 SSH 的 docker 不在 PATH，命令前要 `export PATH=$PATH:/usr/local/bin`

## 巡检对象：正在跑的 3 个容器

| 容器 | 状态 | 镜像 | 用途 |
|------|------|------|------|
| kitchen | Up 24 hours | kitchen-kitchen | 自部署应用 |
| litellm | Up 43 hours | ghcr.nju.edu.cn/berriai/litellm | AI 网关 |
| openclaw | Up 47 hours (healthy) | ghcr.nju.edu.cn/openclaw/openclaw | AI 巡检/自动化助手 |

## 资源水位（本次采样）

- 磁盘：/volume1 共 881G，已用 772G，剩 109G —— **使用率 88%** ⚠️
- 内存：总计约 3.9GB
- 温度：/host/sys/class/hwmon/hwmon0/temp2_input（÷1000 = ℃）

## 第 4 周巡检脚本的雏形（需求清单）

1. 检查 3 个容器是否都在运行（`docker ps`）
2. 检查磁盘使用率，超过 85% 报警（现在 88%，已经超线！）
3. 检查内存使用率
4. 检查 CPU/主板温度，超过 65℃ 报警
5. 输出一段人能直接看的摘要，异常项标出

> 顺带发现一个真问题：磁盘 88% 快满了。学习的同时顺手解决真实问题——这就是运维开发的日常。
