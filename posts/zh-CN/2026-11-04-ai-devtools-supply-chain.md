---
title: AI 编程工具的扩展后门与恶意指引文件
description: 太平洋时间 10 月 29 日从 Cursor 自家市场安装或更新 Claude Code 扩展 2.1.312、2.1.313 的 Windows 与 macOS 用户，可能装到含后门的版本。依 Anthropic 方面的说法，官方渠道的版本不受影响。另一份 10 月 22 日的研究记录了放进下载文件夹、诱使 Codex 安装恶意软件包的 Markdown 指引文件。
date: 2026-11-04T00:00:00+08:00
slug: ai-devtools-supply-chain
categories:
  - security
sources:
  - title: Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace
    url: https://cursor.com/blog/claude-code-extension-security-notice
    publisher: Cursor
    date: 2026-10-29
  - title: "Markdown Is the New Executable: Attackers Are Dropping Agent Instructions Into Your Downloads Folder From the Web"
    url: https://forever.security/blog/hijacking-ai-agents-via-downloads-folder/
    publisher: Forever Security
    date: 2026-10-22
  - title: Anthropic VS code extension on Cursor backdoored for nearly 12 hours
    url: https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/
    publisher: Ars Technica
    date: 2026-10-30
  - title: "Anthropic: That Claude Code extension compromise… couldn't be us"
    url: https://www.theregister.com/cyber-crime/2026/10/30/anthropic-that-claude-code-extension-compromise-couldnt-be-us/5306682
    publisher: The Register
    date: 2026-10-30
  - title: "Official Claude Code Extension Compromise: Security Advisory"
    url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
    publisher: Phorion
    date: 2026-10-30
  - title: Anthropic hacked to deliver remote access trojan to claude developer laptops worldwide
    url: https://doublepulsar.com/anthropic-hacked-to-deliver-remote-access-trojan-to-claude-developer-laptops-worldwide-1148a92baae2
    publisher: DoublePulsar
    date: 2026-10-30
  - title: AI coding agents fall for malicious instructions planted in the Downloads folder
    url: https://www.helpnetsecurity.com/2026/10/26/ai-coding-agents-malware-openai-codex/
    publisher: Help Net Security
    date: 2026-10-26
  - title: 惡意Markdown指引檔企圖誘使Codex安裝惡意套件，AI程式開發代理面臨攻擊風險
    url: https://www.ithome.com.tw/news/180033
    publisher: iThome
    date: 2026-10-30
  - title: Supported Regions Policy
    url: https://www.anthropic.com/supported-countries
    publisher: Anthropic
  - title: Regions
    url: https://cursor.com/docs/account/regions
    publisher: Cursor
authors:
  - anoni-net
---

10 月 29 日，AI 编程编辑器 Cursor 自家的扩展市场上出现被篡改过的 Claude Code 扩展（extension，装进编辑器、增加功能的插件），停留约 11 小时。依 Cursor 的公告，受影响的是 Windows 与 macOS 版的 `Anthropic.claude-code` 2.1.312 与 2.1.313，只有在那段时间从 Cursor 市场安装或更新的人需要处理。依 The Register 转引 Anthropic 一位技术人员在 X 的帖子，Anthropic 官方渠道的版本没有问题，只有 Cursor 的用户受影响。另一件是安全公司 Forever Security 10 月 22 日公开的案例，一份出现在下载文件夹的 Markdown 指引文件试图让 OpenAI 的编程代理 Codex 安装恶意软件包。

依 Cursor 的公告，恶意版本在市场上的时间是太平洋时间 10 月 29 日 02:27 到 13:35（台北时间 10 月 29 日 17:27 到 10 月 30 日 04:35）。Ars Technica 的报道引述 Cursor，受影响的用户最多 5,000 人。安全公司 Phorion 的首席技术官向 Ars 表示，恶意版本是用 Anthropic 在 Cursor 市场的官方账号发布的。他也提到 Cursor 默认会自动更新扩展，用户可以在设置里调整。

Cursor 10 月 30 日更新公告时列出 2.1.312 与 2.1.313 两版，Ars、The Register 与 Phorion 一开始都只写 2.1.313。Phorion 10 月 30 日把原本写的 Open VSX（VS Code 衍生编辑器共用的开放扩展市场）更正为 Cursor 的市场，10 月 31 日又依 Cursor 的更新补上 2.1.312。Phorion 与 Ars 都写到恶意代码也有针对 Linux 的部分，Cursor 列出的受影响平台只有 Windows 与 macOS。依 Ars 引述一位独立安全研究者的说法，Anthropic 在恶意版本上架数小时后发布了 2.1.314。

依 Cursor 的公告与 Phorion 的分析，恶意代码在扩展加载时就会执行，用户不必打开它。程序会把电脑名称、用户名、操作系统、公开 IP、Git 设置的 email 与环境变量的名称（不含值）回传给攻击者。它也试着加入攻击者的 SSH（远程登录电脑用的协议）密钥、建立反向连接的通道，并设置成在后台持续重试。Cursor 的公告提到开启 SSH 服务需要管理员权限，多数 macOS 与 Windows 电脑上这一步会失败，攻击者也就无法经由通道登录。

即使通道没有建立，攻击者的密钥与持续运行的设置仍会留在电脑上，电脑的数据也已经送出。Cursor 与托管服务商合作，让攻击者的服务器下线。Cursor 的公告列出的处置还包括移除恶意版本、暂时关闭整个市场，以及审计访问日志、确认没有其他扩展被篡改。Cursor 也更换了密钥，重建市场后重新上线。

到 11 月 2 日，Cursor 与 Anthropic 都没有公开恶意版本如何以 Anthropic 的已验证账号上架到 Cursor 市场。前面引述的那位独立安全研究者 10 月 30 日的文章标题写“Anthropic hacked”，之后在文中补上 Anthropic 方面把问题归到 Cursor 市场的回应。依 The Register 转引，Anthropic 那位技术人员写 Anthropic 的系统与员工电脑都没有被入侵。他写到有人利用 Cursor 市场的访问权限，上传了 Anthropic 没有制作、也没有发布的篡改版本。

Markdown 指引文件那件，依 Forever 的文章，客户电脑的下载文件夹里出现一份约 13 KB、伪装成一般工程规范的 `AGENTS.md`。`AGENTS.md` 是开发者放在项目文件夹里、给编程代理读的指引文件，代理会自动读取并照着做。文件要求 Codex 修改自己的全机设置、注册攻击者指定的 MCP 服务器（Model Context Protocol，让代理对接外部工具的接口），再安装 npm 软件包 `function-color`。Forever 用自家产品在软件包安装前拦下，依 Help Net Security 的报道，npm 已经移除该软件包。

依 Help Net Security 的报道，研究者发现时不知道文件是怎么进到下载文件夹的。研究者写到，网站不需要用户点击或授权，就能把文件放进下载文件夹。Codex 只照做它信任的文件夹里的 `AGENTS.md`，用户在下载文件夹工作过之后，那里就算是信任的文件夹。研究者在隔离环境重现整条攻击，Codex 在超过九成的尝试里执行了文件要它执行的程序（多数测试用只会打开计算器的无害替身）。

研究者也仿照同样的写法自行写了一份 `CLAUDE.md`，测试 Anthropic 的 Claude Code，这份文件没有在客户电脑上出现过。约一半的测试里，Claude Code 照文件改了设置，把 API 连接导向研究者的服务器。研究者写到登录令牌会因此外泄，用截取的令牌可以接管账号。Forever 的文章主张 OpenAI 与 Anthropic 都没有东西可以修补，到 11 月 2 日，本文没有查到两家公司对这份研究的公开回应。

## 导读观点 {#perspective}

两起事件的来源没有把它们连在一起，本文放在同一篇，是因为两者都利用了开发工具自动加载、自动信任的文件。Ars 的报道提到，Cursor 的扩展以编辑器本身的权限运行，装上之后很可能可以访问本机文件、源代码与开发工具。本文推论，市场的已验证账号加上默认的自动更新，让发布账号成为用户与恶意版本之间唯一的关卡。依 The Register 与 DoublePulsar 的文章，更新到 2.1.314 也不会清掉已经装好的持续运行设置。

指引文件的攻击属于间接提示注入（indirect prompt injection，把指令藏在 AI 会读进来的内容里），代理照设计会把指引文件当成用户的指示照做。Forever 把问题归在两件各自合理的事交会的地方，一是代理信任它所在的文件夹，二是网页长久以来就能把文件放进下载文件夹。依 Help Net Security 的报道，很多浏览工作已经交给代理自行完成。代理自己打开的网页也可能放下文件，屏幕前没有人看得到。

自动更新与指引文件都有取舍。本文推论，关掉扩展的自动更新可以避开类似的时间窗，代价是安全补丁也会晚到。Forever 建议保持代理的操作批准与沙箱（限制程序能访问的范围）开启，依 iThome 的整理，Codex 那份指引文件就试图让代理绕过这两道限制。

Anthropic 的 Supported Regions Policy 页面标示 2026 年 11 月 12 日才生效，晚于本文查证时的 11 月 2 日。页面写明不在清单内的国家与地区不受支持，清单含日本、新加坡、韩国、台湾，没有中国大陆、香港与澳门。Cursor 的文档提到部分模型提供商有地区限制，页面没有点名中国大陆，Open VSX 与 Cursor 市场在中国大陆的连接状况到 11 月 2 日没有查到。

在台北时间 10 月 29 日傍晚到 30 日清晨从 Cursor 市场安装或更新过 Claude Code 扩展的 Windows 与 macOS 用户，第一步是照 Cursor 公告里的方法检查 SSH 的授权密钥列表，有攻击者的密钥就代表电脑受影响。公告附有 macOS 与 Windows 的检查与清除脚本。同一份公告提醒只移除扩展可能不够，要从另一台可信任的电脑更换受影响电脑能访问的密码、令牌与登录会话，并评估是否重装系统。

用 Codex、Claude Code 这类代理的人，Forever 建议的第一步是不要在下载文件夹启动代理（本文推论不写代码、只让代理整理文档或浏览网页的人也适用），不需要另外购买工具。打开刚克隆的代码库或别人给的文件夹之前，先读过里面不是自己写的 `AGENTS.md` 与 `CLAUDE.md`，也检查代理的设置文件有没有自己没加过的服务器或网址。发现被植入文件时，依 Forever 的建议，要当作登录令牌已经外泄并立即更换。本文推论这些做法只能降低被诱导的机会，代理照指引文件行事的设计不会因此改变。
