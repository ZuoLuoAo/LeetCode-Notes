# AGENTS.md

## 项目概览

- 项目类型：LeetCode 刷题笔记仓库（Obsidian Vault + GitHub 公开作品集）
- 主要语言：Python、C++（代码以内嵌代码块形式保存在 Markdown 笔记中，不单独建文件）
- 关键目录：
  - `问题库/`：做题提问收录与次数统计（ask_count / appear_count）
  - `模板/`：题解、问题、专题总结三类模板
  - 主题目录（如 `01-数组/`）：按需创建，每题一个 `README.md`
  - `学习日志.md`：每次练习的追加式记录
- 不要修改的目录：无；所有内容按本文件规范维护

## 常用命令

- 安装依赖：无（纯 Markdown 仓库）
- 本地查看：用 Obsidian 打开仓库根目录
- 运行测试：无（代码在 LeetCode 在线验证）
- 类型检查 / 格式化：无

## 代码规范

- 遵循现有笔记风格；不做无关重构。
- 详细规范（commit、命名、结构、质量、安全、语言）使用 `coding-standards` skill，按任务类型按需读取。
- 笔记、目录、注释、提交描述一律使用中文；首页 README 保留英文简介段落（公开仓库例外）。

## Commit 规范

- Conventional Commits：英文 type + 中文描述，如 `feat: 新增 LC0001 两数之和`。
- 分支命名：`feature/刷题-YYYYMMDD`；初始化骨架使用 `feature/init-笔记体系`。
- push 仅在用户明确要求时执行。

## 安全边界

- 不读取或提交 `.env`、密钥、Cookie 等私有凭据。
- 不提交 `.obsidian/` 本地配置。
- 私有仓库 `LeetCode-Raw`（LeetHub 原始代码存档）不混入公开仓库。

## 交付要求

- 说明改动文件。
- 说明验证命令与结果。
- 说明未验证项与剩余风险。
