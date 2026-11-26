# 写作与研究 Skill 工具包

这套工具包包含 11 个 Agent Skills。把所需 Skill 的完整目录复制到目标 Harness 的技能目录即可安装。项目级安装会随当前项目使用，用户级安装供本机多个项目共用。路径里的 `~` 指用户目录，Windows 上通常是 `C:\Users\你的用户名`。各工具的发现规则见 [Agent Skills 规范](https://agentskills.io/specification) 和下表的官方文档。

| Harness | 项目级目录 | 用户级目录 | 官方文档 |
|---|---|---|---|
| Claude Code | `.claude/skills` | `~/.claude/skills` | [Skills](https://code.claude.com/docs/en/skills) |
| Cursor | `.cursor/skills` | `~/.cursor/skills` | [Skills](https://cursor.com/docs/skills) |
| Gemini CLI | `.gemini/skills` 或 `.agents/skills` | `~/.gemini/skills` 或 `~/.agents/skills` | [Agent Skills](https://geminicli.com/docs/cli/skills/) |
| OpenCode | `.opencode/skills` 或 `.agents/skills` | `~/.config/opencode/skills` 或 `~/.agents/skills` | [Skills](https://opencode.ai/docs/skills/) |
| VS Code / GitHub Copilot | `.github/skills` | `~/.copilot/skills` | [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Codex | `.agents/skills` | `~/.agents/skills` | [Codex 技能目录](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) |

## 安装与验证

1. 从 GitHub 仓库页面选择 **Code → Download ZIP** 并解压，也可以复制仓库的 HTTPS 地址运行 `git clone <地址>`。私有仓库需要先登录有访问权的 GitHub 账号。
2. 将 `skills/` 下的同名目录完整复制到上表对应位置。例如 Claude Code 的项目级路径是 `<项目>/.claude/skills/humanizer-zh/SKILL.md`。如果要用 `survey` 或 `paper-details`，同时复制 `documenting-with-sources` 和 `writing-quotation`。
3. 从目标项目重新开启一个会话，输入“请用 `humanizer-zh` 润色下面这句话，保留原意：该方案可以进行数据导出。”检查工具显示的 Skill 调用或读取记录。若找不到 Skill，先核对目录层级、产品版本和项目是否受信任。

也可以用 Python 批量安装。在工具包目录打开终端后运行下面的命令。安装器会自动加入依赖，并在发现同名目录时停止，既有 Skill 仍可单独备份后再替换。

```powershell
# 列出清单
python install.py --list

# 安装全部到 Claude Code 用户目录（macOS / Linux 可用 python3）
python install.py --dest "$HOME/.claude/skills"

# 只安装指定 Skill。将路径换成你实际项目的目录
python install.py --dest "C:/path/to/project/.agents/skills" humanizer-zh survey

# 先预览将复制哪些 Skill
python install.py --dry-run --dest "$HOME/.cursor/skills" paper-details
```

## 随包提供的 Skill

| Skill | 用途 | 使用条件 |
|---|---|---|
| `humanizer-zh` | 中文润色，保留事实和语气 | 纯文本即可使用 |
| `anti-defensive-writing` | 论文叙事、摘要、引言和审稿回复 | 用已有证据支撑论点 |
| `chinese-academic-writing` | 中文论文、摘要、逐章修订与交付核查 | 按[写作规则 9.0 社会科学适用版](skills/chinese-academic-writing/references/writing-rules-9.md)执行。项目专用要求由作者提供 |
| `literature-synthesis-guide` | 从已有资料提炼证据表和叙述性综述 | 点名调用并提供文献材料 |
| `master-thesis-studio-skill` | 中文硕士论文组织、写作与 Word 输出 | 点名调用。生成 Word 需要 Python 和 `lxml`。可使用随包的上游示例模板，或用 `--template` 传入自己的 `.docx` 或 `.dotx` 模板 |
| `explain` | 写概念或系统说明 | Mermaid 图取决于目标 Harness 或阅读器 |
| `documenting-with-sources` | 给文稿标注出处 | 同时安装 `writing-quotation` |
| `writing-quotation` | 组织引文、原文和译文 | 提供引文原文和出处 |
| `survey` | 综合不同来源，写专题报告 | 需要资料或检索能力；同时安装两个引用 Skill |
| `paper-details` | 从论文写分节解读 | 需要可读论文；提取图片视 Python/PyMuPDF 或宿主工具而定；同时安装两个引用 Skill |
| `html` | 把概念、机制或报告做成 HTML 说明页 | 点名调用；写文件、预览和导出 PDF 取决于本机工具 |

## 平台插件与替代方法

| 条目 | 跨 Harness 使用方法 | 原生恢复 |
|---|---|---|
| `write-like-me:write-like-me` | 给目标 Harness 提供自己有权使用的写作样本，请它参考句式、用词和节奏；可使用 [写作风格提示词](writing-style-prompt.md) | 在 ChatGPT/Codex 的插件目录安装 **Writing Style**，按提示连接来源 |
| `documents:documents` | 使用目标 Harness 提供的 Word 或文档工具 | 安装 **Documents** |
| `google-drive:google-docs` | 安装目标 Harness 支持的 Google Drive/Docs 连接器，再登录 Google | 安装 **Google Drive** 并连接账号 |
| `pages:write-page` | 让目标 Harness 创建 Markdown，有需要时再导入自己的文档平台 | 在 ChatGPT/Codex 安装 **Pages** |
| `zotero:Zotero` | 用目标 Harness 支持的 Zotero 连接器，或从 Zotero 导出 `.bib` 提供给它 | 安装 **Zotero**，连接本机文献库 |

平台插件的连接器、私有样本访问和授权需要在目标工具中单独设置。[ChatGPT/Codex 插件文档](https://learn.chatgpt.com/docs/plugins#use-and-install-plugins)

## 来源与改动

- `humanizer-zh` 取自安装快照，保留 MIT 许可。为符合 Agent Skills 通用格式，去掉了 Claude 专用的工具预授权列表。[Humanizer-zh 上游](https://github.com/op7418/Humanizer-zh)
- `anti-defensive-writing` 取自已安装的中文目录，附上 MIT 许可。[Anti-Defensive Writing 上游](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)
- 六个 AI Review Skills 取自已安装插件快照 `0.3.2+codex.20260909134907`。把三项 Skill 需要的运行环境说明放入各自的 `references/`，以便独立安装；保留上游许可。[AI Review Skills 上游](https://github.com/hoku-ya/ai-review-skills)
- `master-thesis-studio-skill` 是本机工作台版本，保留其中的 MIT 许可、说明、脚本及 Markdown 项目模板。随包的 `examples/Template.docx` 来自公开上游，与本机默认模板的 SHA-256 一致。其余本机 Word 样例未收入。移除了通用格式之外的重复 `描述` 字段。[论文 Skill 上游](https://github.com/darksider-9/master-thesis-studio-skill)
- `literature-synthesis-guide` 来自本机工作台。可用的本机副本未附带公开仓库地址或再分发许可，按个人私有备份管理。
